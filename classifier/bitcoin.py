from bloxplorer.transactions import Transactions
from json import JSONEncoder
from classifier.opcodes import *
from classifier.opcodes import get_opcode_by_name
import queue


def get_opcodes_from_string(opcode_str: str):
    if opcode_str == "":
        return []
    res = []

    splitted = opcode_str.split()
    op = splitted[0]
    data = []

    for o in splitted[1:]:
        if o[:2] == "OP":
            res.append(get_opcode_by_name(op)(op, data))
            op = o
            data = []
        else:
            data.append(o)

    res.append(get_opcode_by_name(op)(op, data))
    return res

class Script:
    opcodes = None
    opcode_str = None
    classifier = None

    def __init__(self, script: dict):
        isInputScript = 'txid' in script
        script_str = script["scriptsig_asm"] if isInputScript else script["scriptpubkey_asm"]

        if isInputScript:
            if "prevout" in script and script["prevout"]:
                self.prevout = Script(script["prevout"])
            if "inner_redeemscript_asm" in script and script["inner_redeemscript_asm"]:
                self.inner_redeemscript = Script({"scriptpubkey_asm": script["inner_redeemscript_asm"]})
            if "inner_witnessscript_asm" in script and script["inner_witnessscript_asm"]:
                self.inner_witnessscript_asm = Script({"scriptpubkey_asm": script["inner_witnessscript_asm"]})

        from classifier.classifier import Classifier

        self.opcode_str = script_str
        self.opcodes = get_opcodes_from_string(script_str)
        self.classifier = Classifier(self.opcodes)

        if isInputScript and self.classifier.classification == 'unknown':
            if "is_coinbase" in script and script["is_coinbase"]:
                self.classifier.data = { "type": "coinbase"}
            elif "prevout" in script and script["prevout"]:
                self.classifier = self.prevout.classifier

    def __str__(self):
        return "Script: {}".format(self.opcode_str)


class Transaction:
    txid = 0
    input_scripts = None
    output_scripts = None

    def __init__(self, trans: Transactions):
        data = trans.data
        self.txid = data["txid"]
        self.input_scripts = [Script(inputs) for inputs in data["vin"]]
        self.output_scripts = [Script(outputs) for outputs in data["vout"]]

    def __str__(self):
        return "Transaction with id: {}".format(self.txid)


class DefaultEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class HexStack(queue.LifoQueue):

    def put(self, item, block=True, timeout=None):
        if type(item) == int:
            super().put("0x{:02x}".format(item), block, timeout)
            return
        super().put(item, block, timeout)

    def put_hex(self, item, block=True, timeout=None):
        if item[:2] != "0x":
            item = "0x" + item
        super().put(item, block, timeout)

    def get_nowait(self):
        temp = super().get_nowait()
        return int(temp, 0)

    def get_hex_nowait(self):
        return super().get_nowait()


class ScriptStep:
    id = 0
    pop = -1
    push = -1
    remaining_script = ""
    current_opcode = ""
    stack = []
    error = ""

    def __init__(self, id: int, current_line: int, stack: [str], pop: int = 0, push: int = 0, error: str = None):
        self.id = id
        self.current_line = current_line
        self.stack = stack
        self.error = error
        self.pop = pop
        self.push = push


class ScriptInterpreter:
    stack = None
    opcodes = None

    def __init__(self, opcodes: [OpCode]):
        self.stack = HexStack()
        self.opcodes = opcodes

    def calculate_remaining_script(self, opcodes: [OpCode]):
        return " ".join([str(o) for o in opcodes])

    def execute(self):
        counter = 0
        res = []
        opc = self.opcodes

        res.append(ScriptStep(
            counter,
            counter - 1,
            list(self.stack.queue),
            0,
            0
        ))

        for o in opc:
            counter += 1
            try:
                o.execute(self.stack)
                res.append(ScriptStep(
                    counter,
                    counter - 1,
                    list(self.stack.queue),
                    o.pop,
                    o.push
                ))
            except NotImplementedError as nie:
                res.append(ScriptStep(
                    counter,
                    counter - 1,
                    list(self.stack.queue),
                    o.pop,
                    o.push,
                    "This OP-code is not implemented"
                ))
                break
            except DisabledOpCodeException as dce:
                res.append(ScriptStep(
                    counter,
                    counter - 1,
                    list(self.stack.queue),
                    o.pop,
                    o.push,
                    "This OP-code is disabled"
                ))
                break
            except InvalidTransactionException as ite:
                res.append(ScriptStep(
                    counter,
                    counter - 1,
                    list(self.stack.queue),
                    o.pop,
                    o.push,
                    "This OP-code marked the transaction as invalid"
                ))
                break
            except CheckSignatureException as cse:
                res.append(ScriptStep(
                    counter,
                    counter - 1,
                    list(self.stack.queue),
                    o.pop,
                    o.push,
                    "This is a OP-code that checks signatures. However, signatures are not checked and all signatures are regarded as valid."
                ))
            except queue.Empty as empty:
                res.append(ScriptStep(
                    counter,
                    counter - 1,
                    list(self.stack.queue),
                    o.pop,
                    o.push,
                    "There are not enough items on the stack to execute this OP-code"
                ))
            except Exception as e:
                res.append(ScriptStep(
                    counter,
                    counter - 1,
                    list(self.stack.queue),
                    o.pop,
                    o.push,
                    "Something went wrong!"
                ))
                break

        return res



import re

from classifier.protocols import KNOWN_PROTOCOL_IDENTIFIERS


class Classifier:
    from classifier.bitcoin import OpCode
    classification: str

    def __init__(self, opcodes: [OpCode]):
        self.classification = 'unknown'
        if len(opcodes) == 0:
            return
        if opcodes[-1].code == 'OP_CHECKMULTISIG':
            self.classification = 'checkmultisig'
            required = re.match('OP_PUSHNUM_(\d+)', opcodes[0].code)
            required = required.group(1) if required else required
            total = re.match('OP_PUSHNUM_(\d+)', opcodes[-2].code)
            total = total.group(1) if total else total
            self.data = [required, total]
        elif opcodes[0].code == 'OP_RETURN':
            self.classification = 'null_data_unspendable'
            if len(opcodes) >= 2:
                self.data = {
                    'protocol': self.identify_op_return_parotocol(opcodes[1].data)
                }
        elif len(opcodes) >= 2 and opcodes[-1].code == 'OP_CHECKSIG':
            if opcodes[-2].code == "OP_EQUALVERIFY":
                self.classification = 'pay_to_public_key_hash'
            else:
                self.classification = 'pay_to_public_key'
        elif len(opcodes) == 3 and \
                opcodes[0].code.startswith('OP_HASH') and \
                opcodes[1].code.startswith('OP_PUSHBYTES') and \
                opcodes[2].code == 'OP_EQUAL':
            self.classification = 'pay_to_script_hash'
        elif len(opcodes) == 2 and opcodes[0].code == 'OP_0':
            if opcodes[1].code == 'OP_PUSHBYTES_20':
                self.classification = 'pay_to_witness_public_key_hash'
            elif opcodes[1].code == 'OP_PUSHBYTES_32':
                self.classification = 'pay_to_witness_script_hash'

    def __str__(self):
        return "{} {}".format(self.classification, " ".join(self.data) if hasattr(self, 'data') else "")

    def identify_op_return_parotocol(self, data: [str]):
        length = 2
        protocol = ''
        try:
            while length <= len(data[0]):
                protocol = bytearray.fromhex(data[0][:length]).decode()
                length += 2
        except:
            if not protocol:
                return 'unknown'
            # raise

        for (key,value) in KNOWN_PROTOCOL_IDENTIFIERS.items():
            if protocol.startswith(key):
                return value

        return 'unknown'

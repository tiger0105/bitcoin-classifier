import hashlib

class OpCode:
    code = None
    data = []
    push = 0
    pop = 0

    def __init__(self, opcode: str, data: [str], push: int=0, pop: int=0):
        self.code = opcode
        self.data = data
        self.push = push
        self.pop = pop

    def __str__(self):
        return "{} {}".format(self.code, " ".join(self.data))

    def execute(self, stack):
        raise NotImplementedError


class DisabledOpCodeException(Exception):
    def __init__(self):
        super()
        self.message = "This OP-Code is disabled"


class IncorrectOpCodeDataException(Exception):
    def __init__(self):
        super()
        self.message = "The data for this OP-Code is incorrect!"


class InvalidTransactionException(Exception):
    def __init__(self):
        super()
        self.message = "This transaction is invalid"


class CheckSignatureException(Exception):
    def __init__(self):
        super()
        self.message = "This transaction contains a signature check that is not evaluated"


class OP_0(OpCode):
    code = "OP_0"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        stack.put(0x0)


class OP_FALSE(OpCode):
    code = "OP_FALSE"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        stack.put(0x0)


class OP_PUSHDATA1(OpCode):
    code = "OP_PUSHDATA1"

    def execute(self, stack):
        raise NotImplementedError


class OP_PUSHDATA2(OpCode):
    code = "OP_PUSHDATA2"

    def execute(self, stack):
        raise NotImplementedError


class OP_PUSHDATA4(OpCode):
    code = "OP_PUSHDATA4"

    def execute(self, stack):
        raise NotImplementedError


class OP_1NEGATE(OpCode):
    code = "OP_1NEGATE"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        stack.put(-1)


class OP_RESERVED(OpCode):
    code = "OP_RESERVED"

    def execute(self, stack):
        raise NotImplementedError


class OP_1(OpCode):
    code = "OP_1"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        stack.put(1)


class OP_TRUE(OpCode):
    code = "OP_TRUE"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        stack.put(1)


class OP_2(OpCode):
    code = "OP_2"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        stack.put(2)


class OP_3(OpCode):
    code = "OP_3"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        stack.put(3)


class OP_4(OpCode):
    code = "OP_4"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        stack.put(4)


class OP_5(OpCode):
    code = "OP_5"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        stack.put(5)


class OP_6(OpCode):
    code = "OP_6"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        stack.put(6)


class OP_7(OpCode):
    code = "OP_7"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        stack.put(7)


class OP_8(OpCode):
    code = "OP_8"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        stack.put(8)


class OP_9(OpCode):
    code = "OP_9"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        stack.put(9)


class OP_10(OpCode):
    code = "OP_10"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        stack.put(10)


class OP_11(OpCode):
    code = "OP_11"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        stack.put(11)


class OP_12(OpCode):
    code = "OP_12"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        stack.put(12)


class OP_13(OpCode):
    code = "OP_13"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        stack.put(13)


class OP_14(OpCode):
    code = "OP_14"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        stack.put(14)


class OP_15(OpCode):
    code = "OP_15"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        stack.put(15)


class OP_16(OpCode):
    code = "OP_16"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        stack.put(16)


class OP_NOP(OpCode):
    code = "OP_NOP"

    def execute(self, stack):
        pass


class OP_VER(OpCode):
    code = "OP_VER"

    def execute(self, stack):
        raise NotImplementedError


class OP_IF(OpCode):
    code = "OP_IF"

    def execute(self, stack):
        raise NotImplementedError


class OP_NOTIF(OpCode):
    code = "OP_NOTIF"

    def execute(self, stack):
        raise NotImplementedError


class OP_VERIF(OpCode):
    code = "OP_VERIF"

    def execute(self, stack):
        raise NotImplementedError


class OP_VERNOTIF(OpCode):
    code = "OP_VERNOTIF"

    def execute(self, stack):
        raise NotImplementedError


class OP_ELSE(OpCode):
    code = "OP_ELSE"

    def execute(self, stack):
        raise NotImplementedError


class OP_ENDIF(OpCode):
    code = "OP_ENDIF"

    def execute(self, stack):
        raise NotImplementedError


class OP_VERIFY(OpCode):
    code = "OP_VERIFY"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 0, 1)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        if temp1 != 1:
            raise InvalidTransactionException


class OP_RETURN(OpCode):
    code = "OP_RETURN"

    def execute(self, stack):
        raise InvalidTransactionException


class OP_TOALTSTACK(OpCode):
    code = "OP_TOALTSTACK"

    def execute(self, stack):
        raise NotImplementedError


class OP_FROMALTSTACK(OpCode):
    code = "OP_FROMALTSTACK"

    def execute(self, stack):
        raise NotImplementedError


class OP_2DROP(OpCode):
    code = "OP_2DROP"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 0, 2)

    def execute(self, stack):
        stack.get_nowait()
        stack.get_nowait()


class OP_2DUP(OpCode):
    code = "OP_2DUP"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 4, 2)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        stack.put(temp2)
        stack.put(temp1)
        stack.put(temp2)
        stack.put(temp1)


class OP_3DUP(OpCode):
    code = "OP_3DUP"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 6, 3)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        temp3 = stack.get_nowait()
        stack.put(temp3)
        stack.put(temp2)
        stack.put(temp1)
        stack.put(temp3)
        stack.put(temp2)
        stack.put(temp1)


class OP_2OVER(OpCode):
    code = "OP_2OVER"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 6, 4)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        temp3 = stack.get_nowait()
        temp4 = stack.get_nowait()
        stack.put(temp4)
        stack.put(temp3)
        stack.put(temp2)
        stack.put(temp1)
        stack.put(temp4)
        stack.put(temp3)

class OP_2ROT(OpCode):
    code = "OP_2ROT"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 6, 6)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        temp3 = stack.get_nowait()
        temp4 = stack.get_nowait()
        temp5 = stack.get_nowait()
        temp6 = stack.get_nowait()
        stack.put(temp4)
        stack.put(temp3)
        stack.put(temp2)
        stack.put(temp1)
        stack.put(temp6)
        stack.put(temp5)


class OP_2SWAP(OpCode):
    code = "OP_2SWAP"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 4, 4)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        temp3 = stack.get_nowait()
        temp4 = stack.get_nowait()
        stack.put(temp2)
        stack.put(temp1)
        stack.put(temp4)
        stack.put(temp3)


class OP_IFDUP(OpCode):
    code = "OP_IFDUP"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 0, 1)


    def execute(self, stack):
        temp = stack.get_nowait()
        if temp != 0:
            stack.put(temp)
            stack.put(temp)
            self.push = 2
        else:
            stack.put(temp)
            self.push = 1


class OP_DEPTH(OpCode):
    code = "OP_DEPTH"

    def execute(self, stack):
        stack.put(len(stack))


class OP_DROP(OpCode):
    code = "OP_DROP"
    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 0, 1)


    def execute(self, stack):
        stack.get_nowait()


class OP_DUP(OpCode):
    code = "OP_DUP"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 2, 1)

    def execute(self, stack):
        temp = stack.get_hex_nowait()
        stack.put_hex(temp)
        stack.put_hex(temp)


class OP_NIP(OpCode):
    code = "OP_NIP"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 2)

    def execute(self, stack):
        temp = stack.get_nowait()
        stack.get_nowait()
        stack.put(temp)


class OP_OVER(OpCode):
    code = "OP_OVER"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 3, 2)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        stack.put(temp2)
        stack.put(temp1)
        stack.put(temp2)


class OP_PICK(OpCode):
    code = "OP_PICK"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 0, 0)

    def execute(self, stack):
        n = stack.get_nowait()
        popped_items = []
        for _ in range(n - 1):
            popped_items.append(stack.get_nowait())
        item_to_copy = stack.get_nowait()
        stack.put(item_to_copy)
        for i in popped_items[::-1]:
            stack.put(i)
        stack.put(item_to_copy)

        self.push = n + 1
        self.pop = n


class OP_ROLL(OpCode):
    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 0, 0)

    code = "OP_ROLL"

    def execute(self, stack):
        n = stack.get_nowait()
        popped_items = []
        for _ in range(n - 1):
            popped_items.append(stack.get_nowait())
        item_to_roll = stack.get_nowait()
        for i in popped_items[::-1]:
            stack.put(i)
        stack.put(item_to_roll)

        self.push = n
        self.pop = n


class OP_ROT(OpCode):
    code = "OP_ROT"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 3, 3)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        temp3 = stack.get_nowait()
        stack.put(temp2)
        stack.put(temp1)
        stack.put(temp3)


class OP_SWAP(OpCode):
    code = "OP_SWAP"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 2, 2)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        stack.put(temp1)
        stack.put(temp2)


class OP_TUCK(OpCode):
    code = "OP_TUCK"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 3, 2)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        stack.put(temp1)
        stack.put(temp2)
        stack.put(temp1)


class OP_CAT(OpCode):
    code = "OP_CAT"

    def execute(self, stack):
        raise DisabledOpCodeException


class OP_SUBSTR(OpCode):
    code = "OP_SUBSTR"

    def execute(self, stack):
        raise DisabledOpCodeException


class OP_LEFT(OpCode):
    code = "OP_LEFT"

    def execute(self, stack):
        raise DisabledOpCodeException


class OP_RIGHT(OpCode):
    code = "OP_RIGHT"

    def execute(self, stack):
        raise DisabledOpCodeException


class OP_SIZE(OpCode):
    code = "OP_SIZE"

    def execute(self, stack):
        raise NotImplementedError


class OP_INVERT(OpCode):
    code = "OP_INVERT"

    def execute(self, stack):
        raise DisabledOpCodeException


class OP_AND(OpCode):
    code = "OP_AND"

    def execute(self, stack):
        raise DisabledOpCodeException


class OP_OR(OpCode):
    code = "OP_OR"

    def execute(self, stack):
        raise DisabledOpCodeException


class OP_XOR(OpCode):
    code = "OP_XOR"

    def execute(self, stack):
        raise DisabledOpCodeException


class OP_EQUAL(OpCode):
    code = "OP_EQUAL"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 2)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        if temp1 == temp2:
            stack.put(1)
        else:
            stack.put(0)


class OP_EQUALVERIFY(OpCode):
    code = "OP_EQUALVERIFY"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 0, 2)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        if temp1 == temp2:
            stack.put(1)
        else:
            stack.put(0)
        temp3 = stack.get_nowait()
        if temp3 != 1:
            raise InvalidTransactionException


class OP_RESERVED1(OpCode):
    code = "OP_RESERVED1"

    def execute(self, stack):
        raise NotImplementedError


class OP_RESERVED2(OpCode):
    code = "OP_RESERVED2"

    def execute(self, stack):
        raise NotImplementedError


class OP_1ADD(OpCode):
    code = "OP_1ADD"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 1)

    def execute(self, stack):
        temp = stack.get_nowait()
        stack.put(temp + 1)


class OP_1SUB(OpCode):
    code = "OP_1SUB"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 1)

    def execute(self, stack):
        temp = stack.get_nowait()
        stack.put(temp - 1)


class OP_2MUL(OpCode):
    code = "OP_2MUL"

    def execute(self, stack):
        raise DisabledOpCodeException


class OP_2DIV(OpCode):
    code = "OP_2DIV"

    def execute(self, stack):
        raise DisabledOpCodeException


class OP_NEGATE(OpCode):
    code = "OP_NEGATE"

    def execute(self, stack):
        raise NotImplementedError


class OP_ABS(OpCode):
    code = "OP_ABS"

    def execute(self, stack):
        raise NotImplementedError


class OP_NOT(OpCode):
    code = "OP_NOT"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 1)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        if temp1 == 0:
            stack.put(1)
        else:
            stack.put(0)


class OP_0NOTEQUAL(OpCode):
    code = "OP_0NOTEQUAL"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 1)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        if temp1 == 0:
            stack.put(0)
        else:
            stack.put(1)


class OP_ADD(OpCode):
    code = "OP_ADD"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 2)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        stack.put(temp1 + temp2)


class OP_SUB(OpCode):
    code = "OP_SUB"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 2)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        stack.put(temp2 - temp1)


class OP_MUL(OpCode):
    code = "OP_MUL"

    def execute(self, stack):
        raise DisabledOpCodeException


class OP_DIV(OpCode):
    code = "OP_DIV"

    def execute(self, stack):
        raise DisabledOpCodeException


class OP_MOD(OpCode):
    code = "OP_MOD"

    def execute(self, stack):
        raise DisabledOpCodeException


class OP_LSHIFT(OpCode):
    code = "OP_LSHIFT"

    def execute(self, stack):
        raise DisabledOpCodeException


class OP_RSHIFT(OpCode):
    code = "OP_RSHIFT"

    def execute(self, stack):
        raise DisabledOpCodeException


class OP_BOOLAND(OpCode):
    code = "OP_BOOLAND"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 2)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        if temp1 == 1 and temp2 == 1:
            stack.put(1)
        else:
            stack.put(0)


class OP_BOOLOR(OpCode):
    code = "OP_BOOLOR"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 2)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        if temp1 == 1 or temp2 == 1:
            stack.put(1)
        else:
            stack.put(0)


class OP_NUMEQUAL(OpCode):
    code = "OP_NUMEQUAL"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 2)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        if temp1 == temp2:
            stack.put(1)
        else:
            stack.put(0)


class OP_NUMEQUALVERIFY(OpCode):
    code = "OP_NUMEQUALVERIFY"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 0, 2)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        if temp1 != temp2:
            raise InvalidTransactionException


class OP_NUMNOTEQUAL(OpCode):
    code = "OP_NUMNOTEQUAL"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 2)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        if temp1 != temp2:
            stack.put(1)
        else:
            stack.put(0)


class OP_LESSTHAN(OpCode):
    code = "OP_LESSTHAN"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 2)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        if temp1 > temp2:
            stack.put(1)
        else:
            stack.put(0)


class OP_GREATERTHAN(OpCode):
    code = "OP_GREATERTHAN"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 2)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        if temp1 < temp2:
            stack.put(1)
        else:
            stack.put(0)


class OP_LESSTHANOREQUAL(OpCode):
    code = "OP_LESSTHANOREQUAL"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 2)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        if temp1 >= temp2:
            stack.put(1)
        else:
            stack.put(0)


class OP_GREATERTHANOREQUAL(OpCode):
    code = "OP_GREATERTHANOREQUAL"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 2)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        if temp1 <= temp2:
            stack.put(1)
        else:
            stack.put(0)


class OP_MIN(OpCode):
    code = "OP_MIN"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 2)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        if temp1 > temp2:
            stack.put(temp2)
        else:
            stack.put(temp1)


class OP_MAX(OpCode):
    code = "OP_MAX"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 2)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        if temp1 < temp2:
            stack.put(temp2)
        else:
            stack.put(temp1)


class OP_WITHIN(OpCode):
    code = "OP_WITHIN"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 3)

    def execute(self, stack):
        max = stack.get_nowait()
        min = stack.get_nowait()
        x = stack.get_nowait()
        if min <= x < max:
            stack.put(1)
        else:
            stack.put(0)


class OP_RIPEMD160(OpCode):
    code = "OP_RIPEMD160"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        temp = stack.get_hex_nowait()[2:]
        if len(temp) %2 != 0:
            temp = "0" + temp
        ripemd160 = hashlib.new("ripemd160")
        ripemd160.update(bytes.fromhex(temp))
        stack.put(int(ripemd160.digest().hex(), 16))


class OP_SHA1(OpCode):
    code = "OP_SHA1"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        temp = stack.get_hex_nowait()[2:]
        if len(temp) %2 != 0:
            temp = "0" + temp
        sha1 = hashlib.sha1(bytes.fromhex(temp)).digest()
        stack.put(int(sha1.hex(), 16))


class OP_SHA256(OpCode):
    code = "OP_SHA256"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        temp = stack.get_hex_nowait()[2:]
        if len(temp) %2 != 0:
            temp = "0" + temp
        sha256 = hashlib.sha256(bytes.fromhex(temp)).digest()
        stack.put(int(sha256.hex(), 16))


class OP_HASH160(OpCode):
    code = "OP_HASH160"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        temp = stack.get_hex_nowait()[2:]
        if len(temp) %2 != 0:
            temp = "0" + temp
        print(temp)
        ripemd160 = hashlib.new("ripemd160")
        sha256 = hashlib.sha256(bytes.fromhex(temp)).digest()
        ripemd160.update(sha256)
        stack.put(int(ripemd160.digest().hex(), 16))


class OP_HASH256(OpCode):
    code = "OP_HASH256"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        temp = stack.get_hex_nowait()[2:]
        if len(temp) %2 != 0:
            temp = "0" + temp
        sha1 = hashlib.sha256(bytes.fromhex(temp)).digest()
        sha2 = hashlib.sha256(sha1).digest()
        stack.put(int(sha2.hex(), 16))


class OP_CODESEPARATOR(OpCode):
    code = "OP_CODESEPARATOR"

    def execute(self, stack):
        pass


class OP_CHECKSIG(OpCode):
    code = "OP_CHECKSIG"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 2)

    def execute(self, stack):
        stack.get_nowait()
        stack.get_nowait()
        stack.put(1)
        raise CheckSignatureException


class OP_CHECKSIGVERIFY(OpCode):
    code = "OP_CHECKSIGVERIFY"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 0, 2)

    def execute(self, stack):
        temp1 = stack.get_nowait()
        temp2 = stack.get_nowait()
        raise CheckSignatureException


class OP_CHECKMULTISIG(OpCode):
    code = "OP_CHECKMULTISIG"

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, push, pop)

    def execute(self, stack):
        nr_public_keys = stack.get_nowait()
        for _ in range(nr_public_keys):
            stack.get_nowait()
        nr_signatures = stack.get_nowait()
        for _ in range(nr_signatures):
            stack.get_nowait()
        # just pop one more element because it is a bug
        stack.get_nowait()
        # put the return value on the stack
        stack.put(1)
        self.push = 1
        self.pop = nr_signatures + nr_public_keys + 3
        raise CheckSignatureException


class OP_CHECKMULTISIGVERIFY(OpCode):
    code = "OP_CHECKMULTISIGVERIFY"
    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, push, pop)

    def execute(self, stack):
        nr_public_keys = stack.get_nowait()
        for _ in range(nr_public_keys):
            stack.get_nowait()
        nr_signatures = stack.get_nowait()
        for _ in range(nr_signatures):
            stack.get_nowait()
        # just pop one more element because it is a bug
        stack.get_nowait()
        self.push = 0
        self.pop = nr_signatures + nr_public_keys + 3
        raise CheckSignatureException


class OP_NOP1(OpCode):
    code = "OP_NOP1"

    def execute(self, stack):
        pass


class OP_NOP2(OpCode):
    code = "OP_NOP2"

    def execute(self, stack):
        pass


class OP_CHECKLOCKTIMEVERIFY(OpCode):
    code = "OP_CHECKLOCKTIMEVERIFY"

    def execute(self, stack):
        pass


class OP_NOP3(OpCode):
    code = "OP_NOP3"

    def execute(self, stack):
        pass


class OP_CHECKSEQUENCEVERIFY(OpCode):
    code = "OP_CHECKSEQUENCEVERIFY"

    def execute(self, stack):
        raise NotImplementedError


class OP_NOP4(OpCode):
    code = "OP_NOP4"

    def execute(self, stack):
        pass


class OP_NOP5(OpCode):
    code = "OP_NOP5"

    def execute(self, stack):
        pass


class OP_NOP6(OpCode):
    code = "OP_NOP6"

    def execute(self, stack):
        pass


class OP_NOP7(OpCode):
    code = "OP_NOP7"

    def execute(self, stack):
        pass


class OP_NOP8(OpCode):
    code = "OP_NOP8"

    def execute(self, stack):
        pass


class OP_NOP9(OpCode):
    code = "OP_NOP9"

    def execute(self, stack):
        pass


class OP_NOP10(OpCode):
    code = "OP_NOP10"

    def execute(self, stack):
        pass


class OP_SMALLINTEGER(OpCode):
    code = "OP_SMALLINTEGER"

    def execute(self, stack):
        raise NotImplementedError


class OP_PUBKEYS(OpCode):
    code = "OP_PUBKEYS"

    def execute(self, stack):
        raise InvalidTransactionException


class OP_PUBKEYHASH(OpCode):
    code = "OP_PUBKEYHASH"

    def execute(self, stack):
        raise InvalidTransactionException


class OP_PUBKEY(OpCode):
    code = "OP_PUBKEY"

    def execute(self, stack):
        raise InvalidTransactionException


class OP_INVALIDOPCODE(OpCode):
    code = "OP_INVALIDOPCODE"

    def execute(self, stack):
        raise InvalidTransactionException


class OP_PUSHBYTES(OpCode):

    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        if len(self.data) != 1:
            raise IncorrectOpCodeDataException()
        stack.put_hex(self.data[0])


class OP_PUSHNUM(OpCode):
    def __init__(self, opcode: str, data: [str], push: int = 0, pop: int = 0):
        super().__init__(opcode, data, 1, 0)

    def execute(self, stack):
        stack.put(int(self.code.split("_")[-1]))


opcode_by_name = {
    'OP_0': OP_0,
    'OP_FALSE': OP_FALSE,
    'OP_PUSHDATA1': OP_PUSHDATA1,
    'OP_PUSHDATA2': OP_PUSHDATA2,
    'OP_PUSHDATA4': OP_PUSHDATA4,
    'OP_1NEGATE': OP_1NEGATE,
    'OP_RESERVED': OP_RESERVED,
    'OP_1': OP_1,
    'OP_TRUE': OP_TRUE,
    'OP_2': OP_2,
    'OP_3': OP_3,
    'OP_4': OP_4,
    'OP_5': OP_5,
    'OP_6': OP_6,
    'OP_7': OP_7,
    'OP_8': OP_8,
    'OP_9': OP_9,
    'OP_10': OP_10,
    'OP_11': OP_11,
    'OP_12': OP_12,
    'OP_13': OP_13,
    'OP_14': OP_14,
    'OP_15': OP_15,
    'OP_16': OP_16,
    'OP_NOP': OP_NOP,
    'OP_VER': OP_VER,
    'OP_IF': OP_IF,
    'OP_NOTIF': OP_NOTIF,
    'OP_VERIF': OP_VERIF,
    'OP_VERNOTIF': OP_VERNOTIF,
    'OP_ELSE': OP_ELSE,
    'OP_ENDIF': OP_ENDIF,
    'OP_VERIFY': OP_VERIFY,
    'OP_RETURN': OP_RETURN,
    'OP_TOALTSTACK': OP_TOALTSTACK,
    'OP_FROMALTSTACK': OP_FROMALTSTACK,
    'OP_2DROP': OP_2DROP,
    'OP_2DUP': OP_2DUP,
    'OP_3DUP': OP_3DUP,
    'OP_2OVER': OP_2OVER,
    'OP_2ROT': OP_2ROT,
    'OP_2SWAP': OP_2SWAP,
    'OP_IFDUP': OP_IFDUP,
    'OP_DEPTH': OP_DEPTH,
    'OP_DROP': OP_DROP,
    'OP_DUP': OP_DUP,
    'OP_NIP': OP_NIP,
    'OP_OVER': OP_OVER,
    'OP_PICK': OP_PICK,
    'OP_ROLL': OP_ROLL,
    'OP_ROT': OP_ROT,
    'OP_SWAP': OP_SWAP,
    'OP_TUCK': OP_TUCK,
    'OP_CAT': OP_CAT,
    'OP_SUBSTR': OP_SUBSTR,
    'OP_LEFT': OP_LEFT,
    'OP_RIGHT': OP_RIGHT,
    'OP_SIZE': OP_SIZE,
    'OP_INVERT': OP_INVERT,
    'OP_AND': OP_AND,
    'OP_OR': OP_OR,
    'OP_XOR': OP_XOR,
    'OP_EQUAL': OP_EQUAL,
    'OP_EQUALVERIFY': OP_EQUALVERIFY,
    'OP_RESERVED1': OP_RESERVED1,
    'OP_RESERVED2': OP_RESERVED2,
    'OP_1ADD': OP_1ADD,
    'OP_1SUB': OP_1SUB,
    'OP_2MUL': OP_2MUL,
    'OP_2DIV': OP_2DIV,
    'OP_NEGATE': OP_NEGATE,
    'OP_ABS': OP_ABS,
    'OP_NOT': OP_NOT,
    'OP_0NOTEQUAL': OP_0NOTEQUAL,
    'OP_ADD': OP_ADD,
    'OP_SUB': OP_SUB,
    'OP_MUL': OP_MUL,
    'OP_DIV': OP_DIV,
    'OP_MOD': OP_MOD,
    'OP_LSHIFT': OP_LSHIFT,
    'OP_RSHIFT': OP_RSHIFT,
    'OP_BOOLAND': OP_BOOLAND,
    'OP_BOOLOR': OP_BOOLOR,
    'OP_NUMEQUAL': OP_NUMEQUAL,
    'OP_NUMEQUALVERIFY': OP_NUMEQUALVERIFY,
    'OP_NUMNOTEQUAL': OP_NUMNOTEQUAL,
    'OP_LESSTHAN': OP_LESSTHAN,
    'OP_GREATERTHAN': OP_GREATERTHAN,
    'OP_LESSTHANOREQUAL': OP_LESSTHANOREQUAL,
    'OP_GREATERTHANOREQUAL': OP_GREATERTHANOREQUAL,
    'OP_MIN': OP_MIN,
    'OP_MAX': OP_MAX,
    'OP_WITHIN': OP_WITHIN,
    'OP_RIPEMD160': OP_RIPEMD160,
    'OP_SHA1': OP_SHA1,
    'OP_SHA256': OP_SHA256,
    'OP_HASH160': OP_HASH160,
    'OP_HASH256': OP_HASH256,
    'OP_CODESEPARATOR': OP_CODESEPARATOR,
    'OP_CHECKSIG': OP_CHECKSIG,
    'OP_CHECKSIGVERIFY': OP_CHECKSIGVERIFY,
    'OP_CHECKMULTISIG': OP_CHECKMULTISIG,
    'OP_CHECKMULTISIGVERIFY': OP_CHECKMULTISIGVERIFY,
    'OP_NOP1': OP_NOP1,
    'OP_NOP2': OP_NOP2,
    'OP_CHECKLOCKTIMEVERIFY': OP_CHECKLOCKTIMEVERIFY,
    'OP_NOP3': OP_NOP3,
    'OP_CHECKSEQUENCEVERIFY': OP_CHECKSEQUENCEVERIFY,
    'OP_NOP4': OP_NOP4,
    'OP_NOP5': OP_NOP5,
    'OP_NOP6': OP_NOP6,
    'OP_NOP7': OP_NOP7,
    'OP_NOP8': OP_NOP8,
    'OP_NOP9': OP_NOP9,
    'OP_NOP10': OP_NOP10,
    'OP_SMALLINTEGER': OP_SMALLINTEGER,
    'OP_PUBKEYS': OP_PUBKEYS,
    'OP_PUBKEYHASH': OP_PUBKEYHASH,
    'OP_PUBKEY': OP_PUBKEY,
    'OP_INVALIDOPCODE': OP_INVALIDOPCODE,
}


def get_opcode_by_name(opcode):
    if "OP_PUSHBYTES" in opcode:
        return OP_PUSHBYTES
    if "OP_PUSHNUM_" in opcode:
        return OP_PUSHNUM
    if opcode not in opcode_by_name.keys():
        return OpCode
    return opcode_by_name[opcode]

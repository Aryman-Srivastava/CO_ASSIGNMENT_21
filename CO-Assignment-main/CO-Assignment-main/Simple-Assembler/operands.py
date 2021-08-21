import instruction as ins

# var = {}


def add(tok):
    # var[tok[1]] = var[tok[2]] + var[tok[3]]
    # if var[tok[1]] > 65535:
    #     ins.FLAGS = "1000"
    return ins.op_codes[tok[0]] + "00" + str(ins.reg_addr[tok[1]]) + str(ins.reg_addr[tok[2]]) + str(
        ins.reg_addr[tok[3]])


def sub(tok):
    return ins.op_codes[tok[0]] + "00" + str(ins.reg_addr[tok[1]]) + str(ins.reg_addr[tok[2]]) + str(
        ins.reg_addr[tok[3]])


def mul(tok):
    return ins.op_codes[tok[0]] + "00" + str(ins.reg_addr[tok[1]]) + str(ins.reg_addr[tok[2]]) + str(
        ins.reg_addr[tok[3]])


def div(tok):
    return ins.op_codes[tok[0]] + "00000" + str(ins.reg_addr[tok[1]]) + str(ins.reg_addr[tok[2]])


def mov_imm(tok):
    # var[tok[1]] = int(tok[2][1:])
    reg = int(tok[2][1:])
    value = bin(reg)[2:]
    res = value.rjust(8, '0')
    return ins.op_codes[tok[0]][0] + str(ins.reg_addr[tok[1]]) + res


def mov_reg(tok):
    # if tok[2] == "FLAGS":
    #     var[tok[1]] = ins.FLAGS
    # else:
    #     var[tok[1]] = var[tok[2]]
    return ins.op_codes[tok[0]][1] + "00000" + ins.reg_addr[tok[1]] + ins.reg_addr[tok[2]]


def rs(tok):
    # reg = var[tok[1]]
    # reg = reg // 2 ** (int(tok[2][1:]))
    imm = int(tok[2][1:])
    reg = bin(imm)[2:]
    res = reg.rjust(8, '0')
    return ins.op_codes[tok[0]] + ins.reg_addr[tok[1]] + res


def ls(tok):
    # reg = var[tok[1]]
    # reg = reg * (2 ** (int(tok[2][1:])))
    # if reg <= 255:
    #     reg = bin(reg)[2:]
    #     res = reg.rjust(8, '0')
    #     return ins.op_codes[tok[0]] + ins.reg_addr[tok[1]] + str(res)
    # else:
    #     reg = bin(reg)
    #     reg = reg[len(reg) - 8:]
    #     return ins.op_codes[tok[0]] + ins.reg_addr[tok[1]] + str(reg)
    imm = int(tok[2][1:])
    reg = bin(imm)[2:]
    res = reg.rjust(8, '0')
    return ins.op_codes[tok[0]] + ins.reg_addr[tok[1]] + res



def xor(tok):
    # var[tok[1]] = var[tok[2]] ^ var[tok[3]]
    return ins.op_codes[tok[0]] + "00" + ins.reg_addr[tok[1]] + ins.reg_addr[tok[2]] + ins.reg_addr[tok[3]]


def or_(tok):
    # var[tok[1]] = var[tok[2]] | var[tok[3]]
    return ins.op_codes[tok[0]] + "00" + ins.reg_addr[tok[1]] + ins.reg_addr[tok[2]] + ins.reg_addr[tok[3]]


def and_(tok):
    # var[tok[1]] = var[tok[2]] & var[tok[3]]
    return ins.op_codes[tok[0]] + "00" + ins.reg_addr[tok[1]] + ins.reg_addr[tok[2]] + ins.reg_addr[tok[3]]


def not_(tok):
    # var[tok[1]] = ~var[tok[2]]
    return ins.op_codes[tok[0]] + "00000" + ins.reg_addr[tok[1]] + ins.reg_addr[tok[2]]


def ld(tok, var_line):
    var_line = bin(var_line)[2:]
    res = var_line.rjust(8, '0')
    return str(ins.op_codes[tok[0]]) + str(ins.reg_addr[tok[1]]) + str(res)


def st(tok, var_line):
    var_line = bin(var_line)[2:]
    res = var_line.rjust(8, '0')
    return ins.op_codes[tok[0]] + ins.reg_addr[tok[1]] + str(res)


def var_line_finder(dic, var_name):
    for i in dic.keys():
        if var_name == dic[i]:
            return i
    return -1


def cmp_(tok):
    # if var[tok[1]] < var[tok[2]]:
    #     ins.FLAGS = "0100"
    # elif var[tok[1]] > var[tok[2]]:
    #     ins.FLAGS = "0010"
    # elif var[tok[1]] == var[tok[2]]:
    #     ins.FLAGS = "0001"
    # var["FLAGS"] = ins.FLAGS
    return ins.op_codes[tok[0]] + "00000" + ins.reg_addr[tok[1]] + ins.reg_addr[tok[2]]

def jmp(tok, line_no):
    return ins.op_codes[tok[0]] + "000" + bin(line_no)[2:].rjust(8, '0')
def jgt(tok, line_no):
    return ins.op_codes[tok[0]] + "000" + bin(line_no)[2:].rjust(8, '0')
def jlt(tok, line_no):
    return ins.op_codes[tok[0]] + "000" + bin(line_no)[2:].rjust(8, '0')
def je(tok, line_no):
    return ins.op_codes[tok[0]] + "000" + bin(line_no)[2:].rjust(8, '0')

def hlt(tok):
    return ins.op_codes[tok[0]] + "00000000000"

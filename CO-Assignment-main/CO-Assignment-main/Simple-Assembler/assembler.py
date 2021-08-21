import operands as op
import instruction as ins
import error as err
import sys
import os

try:
    f = open("instruction.txt", 'w+')
    line = input()
    f.write(line + "\n")
    f.close()
    f = open("instruction.txt", 'a')
    while True:
        l = input()
        f.write(l + "\n")
        if "hlt" in l:
            break
    hlt_line = 0
    hlt_flag = False
    errors = {}
    var_names = []
    out_dict = {}
    lineno = 0
    labels = {}  # key --> label_name | value --> line_no
    f = open("instruction.txt", 'r+')
    for line in f.readlines():
        if line == '\n':
            continue
        tok = line.split()
        if tok[0] == "var":
            continue
        elif tok[0][-1] == ':':
            labels[tok[0][:-1]] = lineno
        lineno += 1
    f.close()
    # finding hlt position
    f = open("instruction.txt", 'r+')
    hlt_line = 0
    hlt_flag = False
    for line in f.readlines():
        if line == '\n':
            continue
        tok = line.split()
        if tok[0] == "var":
            continue
        if "hlt" in tok:
            hlt_flag = True
            break
        else:
            hlt_line += 1
    f.close()
    error_msg = {
        "illegal flag": "Illegal use of FLAG register",
        "illegal label": "Label not found",
        "halt error": "Termination error",
        "illegal variable": "Variable not found",
        "op error": "Instruction not defined",
        "imm error": "Immediate value out of range",
        "misc error": "General Syntax Error",
        "illegal register": "illegal use of register name",
        "typo": "illegal declaration of instruction",
        "syntax": "syntax error"
    }
    lineno = 0
    f = open("instruction.txt", 'r+')
    for line in f.readlines():
        if line == '\n':
            continue
        tok = line.split()
        if tok[0][:-1] in labels.keys():
            tok = tok[1:]

        elif tok[0] == "var":
            if lineno == 0:
                var_names.append(tok[1])
                continue
            elif lineno > 0:
                errors[lineno] = error_msg["misc error"]
                continue
        if tok[0] in ins.op_codes and len(tok) != err.tok_length[tok[0]]:
            errors[lineno] = error_msg["syntax"]
        if tok[0] == "mov" and '$' in tok[2] and (int(tok[2][1:]) > 255 or int(tok[2][1:]) < 0):
            errors[lineno] = error_msg["imm error"]
        elif tok[0] not in ins.op_codes.keys():
            errors[lineno] = error_msg["op error"]
        elif tok[0] in ["ld", "st"] and tok[2] not in var_names:
            errors[lineno] = error_msg["illegal variable"]
        elif hlt_flag == False or lineno > hlt_line:
            errors[lineno] = error_msg["halt error"]
        elif "FLAGS" in tok and tok[0] != "mov":
            errors[lineno] = error_msg["illegal flag"]
        elif tok[0] == "st" or tok[0] == "ld":
            if tok[1] not in ins.reg_addr.keys() and tok[2] not in var_names:
                errors[lineno] = error_msg["typo"]
        elif tok[0] not in "jmpjltjgtjehlt":
            if "$" not in line:
                if tok[1] not in ins.reg_addr.keys() or tok[2] not in ins.reg_addr.keys():
                    errors[lineno] = error_msg["typo"]
            else:
                if tok[1] not in ins.reg_addr.keys():
                    errors[lineno] = error_msg["typo"]
            # for i in range(1, len(tok)):
            #     if tok[i] not in ins.reg_addr.keys():
            #         print(1)
            #         errors[lineno] = error_msg["typo"]
            #     elif '$' not in tok[i]:
            #         print(0)
            #         errors[lineno] = error_msg["typo"]
        elif tok[0] in "jmpjltjgtje" and tok[1] not in labels.keys():
            errors[lineno] = error_msg["illegal label"]
        lineno += 1
    f.close()
    lineno = 0
    if len(errors) == 0:
        f = open("instruction.txt", 'r')
        var_line = hlt_line + 1
        for line in f.readlines():
            if line == '':
                continue
            tok = line.split()
            if tok[0][:len(tok[0]) - 1] in labels.keys():
                tok = tok[1:]
            if tok[0] == "hlt":
                out_dict[lineno] = op.hlt(tok)
                break
            if tok[0] == "var":
                out_dict[var_line] = tok[1]
                var_line += 1
            else:
                if tok[0] == "add":
                    out_dict[lineno] = op.add(tok)
                elif tok[0] == "sub":
                    out_dict[lineno] = op.sub(tok)
                elif tok[0] == "mul":
                    out_dict[lineno] = op.mul(tok)
                elif tok[0] == "div":
                    out_dict[lineno] = op.div(tok)
                elif tok[0] == "mov" and ("$" in tok[2]):
                    out_dict[lineno] = op.mov_imm(tok)
                elif tok[0] == "mov":
                    out_dict[lineno] = op.mov_reg(tok)
                elif tok[0] == "rs":
                    out_dict[lineno] = op.rs(tok)
                elif tok[0] == "ls":
                    out_dict[lineno] = op.ls(tok)
                elif tok[0] == "xor":
                    out_dict[lineno] = op.xor(tok)
                elif tok[0] == "and":
                    out_dict[lineno] = op.and_(tok)
                elif tok[0] == "or":
                    out_dict[lineno] = op.or_(tok)
                elif tok[0] == "not":
                    out_dict[lineno] = op.not_(tok)
                elif tok[0] == "ld":
                    line = op.var_line_finder(out_dict, tok[2])
                    out_dict[lineno] = op.ld(tok, line)
                elif tok[0] == "st":
                    line = op.var_line_finder(out_dict, tok[2])
                    out_dict[lineno] = op.st(tok, line)
                elif tok[0] == "cmp":
                    out_dict[lineno] = op.cmp_(tok)
                elif tok[0] == "jmp":
                    out_dict[lineno] = op.jmp(tok, labels[tok[1]])
                elif tok[0] == "jlt":
                    out_dict[lineno] = op.jlt(tok, labels[tok[1]])
                elif tok[0] == "jgt":
                    out_dict[lineno] = op.jgt(tok, labels[tok[1]])
                elif tok[0] == "je":
                    out_dict[lineno] = op.je(tok, labels[tok[1]])
                lineno += 1
        f.close()
    else:
        print(errors)
        sys.exit()
    for i in range(hlt_line+1):
        print(out_dict[i])
    if os.path.exists("instruction.txt"):
        os.remove("instruction.txt")
except EOFError:
    print("Termination error")
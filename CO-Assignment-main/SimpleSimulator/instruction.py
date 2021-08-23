op_codes = {
    "00000": "add", "00001": "sub", "00010": "mov_Imm", "00011":"mov_reg", "00100": "ld", "00101": "st",
    "00110": "mul", "00111": "div", "01000": "rs", "01001": "ls", "01010": "xor",
    "01011": "or", "01100": "and", "01101": "not", "01110": "cmp", "01111": "jmp",
    "10000": "jlt", "10001": "jgt", "10010": "je", "10011": "hlt"
}

reg_addr = {"000": "R0", "001": "R1", "010": "R2", "011": "R3", "100": "R4", "101": "R6", "110": "R6", "111": "FLAGS"}
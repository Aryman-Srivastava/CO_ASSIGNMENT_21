# main_file
import os
#
#
def main():
    from ExecutionEngine import ExecutionEngine
    from ProgramCounter import ProgramCounter
    from RegisterFile import RegisterFile
    regf = RegisterFile()
    memory = regf.get_mem()
    progc = ProgramCounter()
    ee = ExecutionEngine(regf, progc)

    cycle = 0
    halted = False

    while not halted:
        instruction = memory.fetch(progc.getVal(), cycle)
        halted, nextPC = ee.execute(instruction, cycle)
        progc.dump()
        regf.dump()
        regf.resFlag()
        cycle += 1

    memory.dump()
    memory.show_traces()


if __name__ == '__main__':

    try:
        IF = open("InstructionFile.txt", 'w+')
        lineIN = input()
        IF.write(lineIN)
        IF.write('\n')
        IF.close()
        IF = open("InstructionFile.txt", 'a+')
        while True:
            try:
                lineIN = input()
                IF.write(lineIN)
                IF.write('\n')
            except EOFError:
                break
            # lineIN = input()
            # if lineIN != "":
            #     IF.write(lineIN)
            #     IF.write('\n')
            # else:
            #     break
        IF.close()
        main()
        os.remove("InstructionFile.txt")
    except EOFError:
        main()
        os.remove("InstructionFile.txt")

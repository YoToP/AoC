from time import time


def part1(path):
    with open(path) as f:
        lines = f.readlines()
    acc = 0
    PC = 0
    maxPC = len(lines)
    loop = True
    while loop:
        ins, arg = str.strip(lines[PC]).split(" ")
        if ins == 'acc':
            acc += int(arg)
            lines[PC]="xxx 0"
            PC += 1
        elif ins == 'jmp':
            lines[PC]="xxx 0"
            PC = PC + int(arg)
        elif ins == 'nop':
            lines[PC]="xxx 0"
            PC += 1
        else:
            print(f"ALU ERROR: Invalid Instruction found: {ins} acc:{acc}")
            return acc
            loop = False
        if PC >= maxPC:
                loop = False

def part2(path):
    with open(path) as f:
        program = f.readlines()
    correctionPC = 0
    while program[correctionPC][0] == 'a': #check for a in acc
        correctionPC += 1
    exitFound = False
    while correctionPC < len(program) and not exitFound:
        copyProgram = program.copy()

        if copyProgram[correctionPC][0] == 'j':
            copyProgram[correctionPC] = copyProgram[correctionPC].replace("jmp", "nop")
        elif copyProgram[correctionPC][0] == 'n':
            copyProgram[correctionPC] = copyProgram[correctionPC].replace("nop", "jmp")
        acc = 0
        PC = 0
        maxPC = len(copyProgram)
        programLoop = True
        while programLoop:
            ins, arg = str.strip(copyProgram[PC]).split(" ")
            if ins == 'acc':
                acc += int(arg)
                copyProgram[PC]="xxx 0"
                PC += 1
            elif ins == 'jmp':
                copyProgram[PC]="xxx 0"
                PC = PC + int(arg)
            elif ins == 'nop':
                copyProgram[PC]="xxx 0"
                PC += 1
            else:
                #print(f"ALU ERROR: Invalid Instruction found: {ins} acc:{acc}")
                programLoop = False
            if PC >= maxPC:
                exitFound = True #GOAL OF PROGRAM
                return acc
                programLoop = False
        correctionPC += 1
        while program[correctionPC][0] == 'a': #check for a in acc
            correctionPC += 1
        

# Run when this script is not imported by another script(e.g. Unittest)
if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', part1("2020/08/inputs/input.txt"))
    print('part 2:', part2("2020/08/inputs/input.txt"))
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))

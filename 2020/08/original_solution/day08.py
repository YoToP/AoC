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
            loop = False
        if PC >= maxPC:
                loop = False



# Run when this script is not imported by another script(e.g. Unittest)
if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', part1("2020/08/inputs/input.txt"))
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))

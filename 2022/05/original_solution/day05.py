from time import time


def part1(path):
    with open(path) as f:
        lines = f.readlines()
    sum = 0
    stacks = []
    for x in range(0,9):
        stacks.append([])
    for x in range(0,8):
        cline = lines[x]
        if cline[1] != ' ':
            stacks[0].append(cline[1])
        if cline[5] != ' ':
            stacks[1].append(cline[5])
        if cline[9] != ' ':
            stacks[2].append(cline[9])
        if cline[13] != ' ':
            stacks[3].append(cline[13])
        if cline[17] != ' ':
            stacks[4].append(cline[17])
        if cline[21] != ' ':
            stacks[5].append(cline[21])
        if cline[25] != ' ':
            stacks[6].append(cline[25])
        if cline[29] != ' ':
            stacks[7].append(cline[29])
        if cline[33] != ' ':
            stacks[8].append(cline[33])
    for x in range(0,9):
        stacks[x].reverse()
    
    bAtinstruction = False
    for line in lines:
        if line =='\n':
            bAtinstruction = True
        elif  bAtinstruction:
            #move 3 from 2 to 5
            _,amount,_,van,_,naar = line.strip().split(" ")
            for x in range(0,int(amount)):
                stacks[int(naar)-1].append(stacks[int(van)-1].pop())

    #calc answer:
    s = ''
    for x in range(0,9):
        s = s+ stacks[x].pop()
    return s


def part2(path):
    with open(path) as f:
        lines = f.readlines()
    sum = 0
    stacks = []
    for x in range(0,9):
        stacks.append([])
    for x in range(0,8):
        cline = lines[x]
        if cline[1] != ' ':
            stacks[0].append(cline[1])
        if cline[5] != ' ':
            stacks[1].append(cline[5])
        if cline[9] != ' ':
            stacks[2].append(cline[9])
        if cline[13] != ' ':
            stacks[3].append(cline[13])
        if cline[17] != ' ':
            stacks[4].append(cline[17])
        if cline[21] != ' ':
            stacks[5].append(cline[21])
        if cline[25] != ' ':
            stacks[6].append(cline[25])
        if cline[29] != ' ':
            stacks[7].append(cline[29])
        if cline[33] != ' ':
            stacks[8].append(cline[33])
    for x in range(0,9):
        stacks[x].reverse()
    
    bAtinstruction = False
    for line in lines:
        if line =='\n':
            bAtinstruction = True
        elif  bAtinstruction:
            #move 3 from 2 to 5
            _,amount,_,van,_,naar = line.strip().split(" ")
            _tempstack = []
            for x in range(0,int(amount)):
                _tempstack.append(stacks[int(van)-1].pop())
            _tempstack.reverse()
            stacks[int(naar)-1].extend(_tempstack)

    #calc answer:
    s = ''
    for x in range(0,9):
        s = s+ stacks[x].pop()
    return s


# Run when this script is not imported by another script(e.g. Unittest)
if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', part1("2022/05/inputs/input.txt"))
    print('part 2:', part2("2022/05/inputs/input.txt"))
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))

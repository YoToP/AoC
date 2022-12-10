from time import time
from collections import deque
cycleCost = {
    'addx': 2,
    'noop': 1,
}


def ParseInstruction(line):
    line = line.strip()
    if len(line) < 5:
        instruction = line
        value = 0
    else:
        instruction, value = line.split()
    return (cycleCost[instruction], int(value))


def part1(path, maxCycles):
    with open(path) as f:
        instructions = deque(map(ParseInstruction, f.readlines()))  # new stuff
    xr = 1  # X register
    cc = 0  # cyclecount
    lastcccomplete = 0
    nextInstruction = instructions.popleft()
    ss = 0  # signal strength list
    while True:
        cc += 1
        if (cc+20) % 40 == 0:
            ss += cc*xr
        if nextInstruction[0]+lastcccomplete == cc:
            lastcccomplete = cc
            xr += nextInstruction[1]
            if len(instructions) == 0:
                break  # no more instructions, so stop the loop
            nextInstruction = instructions.popleft()
    return ss


def part2(path):
    with open(path) as f:
        instructions = deque(map(ParseInstruction, f.readlines()))
    xr = 1  # X register
    cc = 0  # cyclecount
    lastcccomplete = 0
    nextInstruction = instructions.popleft()
    screen = [''for _ in range(0, 6)]
    blockChar = chr(9608)  # looks nicer and more readable than '#'
    while True:
        screen[cc//40] += blockChar if cc % 40 in range(xr-1, xr+2) else ' '

        cc += 1
        if nextInstruction[0]+lastcccomplete == cc:
            lastcccomplete = cc
            xr += nextInstruction[1]
            if len(instructions) == 0:
                break  # no more instructions, so stop the loop
            nextInstruction = instructions.popleft()
    for sl in screen:
        print(sl)


if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', part1("2022/10/inputs/input.txt", 220))
    print('part 2:')
    part2("2022/10/inputs/input.txt")
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))

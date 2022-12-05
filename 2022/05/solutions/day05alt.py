from time import time
import sys


def ParseGridInput(grid):
    grid = grid.split("\n")
    stackCount = int(grid.pop().strip().split(" ").pop())
    stackHeight = len(grid)
    stacks = []
    y = 1
    for _ in range(0, stackCount):
        stack = []

        for j in range(0, stackHeight):
            char = grid[j][y]
            if char != ' ':
                stack.append(grid[j][y])
        y += 4
        stack.reverse()
        stacks.append(stack)
    return stacks


def part1(path):
    with open(path) as f:
        data = f.read()
    grid, instrs = data.split("\n\n")
    stacks = ParseGridInput(grid)

    instrs = instrs.strip().split("\n")
    for line in instrs:
        # move 3 from 2 to 5
        _, amount, _, src, _, dest = line.strip().split(" ")
        sliceStart = 0
        sliceEnd = len(stacks[int(src)-1])-int(amount)
        keep = stacks[int(src)-1][sliceStart:sliceEnd]

        sliceStart = len(stacks[int(src)-1])-int(amount)
        sliceEnd = len(stacks[int(src)-1])
        copyAndRemove = stacks[int(src)-1][sliceStart:sliceEnd]

        stacks[int(src)-1] = keep
        copyAndRemove.reverse() #only difference beetween part 1 and two
        stacks[int(dest)-1].extend(copyAndRemove)
    # calc answer:
    s = ''
    for x in range(0, len(stacks)):
        s = s + stacks[x].pop()
    return s


def part2(path):
    with open(path) as f:
        data = f.read()
    grid, instrs = data.split("\n\n")
    stacks = ParseGridInput(grid)

    instrs = instrs.strip().split("\n")
    for line in instrs:
        # move 3 from 2 to 5
        _, amount, _, src, _, dest = line.strip().split(" ")
        sliceStart = 0
        sliceEnd = len(stacks[int(src)-1])-int(amount)
        keep = stacks[int(src)-1][sliceStart:sliceEnd]

        sliceStart = len(stacks[int(src)-1])-int(amount)
        sliceEnd = len(stacks[int(src)-1])
        
        stacks[int(dest)-1].extend(stacks[int(src)-1][sliceStart:sliceEnd])
        stacks[int(src)-1] = keep
        
    # calc answer:
    s = ''
    for x in range(0, len(stacks)):
        s = s + stacks[x].pop()
    return s


# Run when this script is not imported by another script(e.g. Unittest)
if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', part1("2022/05/inputs/input.txt"))
    print("### part 1 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    print('part 2:', part2("2022/05/inputs/input.txt"))
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))

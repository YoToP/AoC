from time import time
from math import lcm

def p1():
    with open("2023/08/inputs/input.txt") as f:
        lines = f.read()

    steps, nodes = lines.split('\n\n')
    nodes = nodes.split('\n')
    puzzleMap = dict()
    for node in nodes:
        source, dest = node.split(' = ')
        left, right = dest.split(', ')
        left = left.replace('(','')
        right = right.replace(')','')
        puzzleMap[source] = (left,right)
    currentPos = 'AAA'
    stepCount = 0
    while currentPos != 'ZZZ':
        for step in steps:
            if step == 'L':
                currentPos = puzzleMap[currentPos][0]
            else:
                currentPos = puzzleMap[currentPos][1]
            stepCount += 1
            if currentPos == 'ZZZ':
                break
    return stepCount


def p2():
    with open("2023/08/inputs/input.txt") as f:
        lines = f.read()
    steps, nodes = lines.split('\n\n')
    nodes = nodes.split('\n')
    puzzleMap = dict()
    currentPositions = []
    for node in nodes:
        source, dest = node.split(' = ')
        left, right = dest.split(', ')
        left = left.replace('(','')
        right = right.replace(')','')
        puzzleMap[source] = (left,right)
        if source[2] == 'A':
            currentPositions.append(source) # fill with startpositions
    commonStepCount = 0
    stepCounts = []
    for i in range(0,len(currentPositions)):
        currentPos = currentPositions[i]
        stepCount = 0
        while currentPos[2] != 'Z':
            for step in steps:
                if step == 'L':
                    currentPos = puzzleMap[currentPos][0]
                else:
                    currentPos = puzzleMap[currentPos][1]
                stepCount += 1
                if currentPos[2] == 'Z':
                    break
        stepCounts.append(stepCount)
    return lcm(*stepCounts)

if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', p1())
    print("### p1 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    start_time = int(round(time() * 1000))
    print('part 2:', p2())
    print("### p2 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
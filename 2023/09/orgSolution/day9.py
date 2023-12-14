from time import time
from collections import deque

def calcDifference(numberList):
    if len(numberList) == 0:
        return []
    elif len(numberList) == 1:
        return [0]
    else:
        returnList = []
        for i in range(0,len(numberList)-1):
            returnList.append(numberList[i+1]-numberList[i])
        return returnList

def makeInt(numberList):
    returnArray = []
    for nr in numberList:
        returnArray.append(int(nr))
    return returnArray

def allZero(numberList):
    for nr  in numberList:
        if nr != 0:
            return False
    return True

def p1():
    with open("2023/09/inputs/input.txt") as f:
        lines = f.readlines()
    score = 0
    for line in lines:
        line = makeInt(line.strip().split()) #individual numbers, as Int

        lastNrStack = deque()
        while not allZero(line):
            lastNrStack.append(line[len(line)-1])
            line = calcDifference(line)
        while len(lastNrStack)>1:
            lastNrStack.append(lastNrStack.pop()+lastNrStack.pop())
        score += lastNrStack.pop()

    return score


def p2():
    with open("2023/09/inputs/input.txt") as f:
        lines = f.readlines()
    score = 0
    for line in lines:
        line = makeInt(line.strip().split()) #individual numbers, as Int

        lastNrStack = deque()
        while not allZero(line):
            lastNrStack.append(line[0])
            line = calcDifference(line)
        while len(lastNrStack)>1:
            last = lastNrStack.pop()
            beforelast = lastNrStack.pop()
            lastNrStack.append(beforelast-last)
        score += lastNrStack.pop()
    return score

if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', p1())
    print("### p1 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    start_time = int(round(time() * 1000))
    print('part 2:', p2())
    print("### p2 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
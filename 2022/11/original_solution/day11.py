from time import time
from collections import deque


def addition(num1, num2):
    return num1 + num2


def multiply(num1, num2):
    return num1 * num2


# Defining the switch function

def switch(operation, num1, num2):

    dict = {
        '+': addition(num1, num2),
        '*': multiply(num1, num2),
    }
    return dict.get(operation, 'Invalid Operation')


def part1(path):
    with open(path) as f:
        data = f.read()
    MonkeyRawData = data.split("\n\n")
    MonkeyItemList = [deque()for _ in range(0, len(MonkeyRawData))]
    MonkeyOperationList = []
    MonkeyTestDivList = []
    MonkeyTrowToList = []
    MonkeyInspectionCounterList = [0 for _ in range(0, len(MonkeyRawData))]
    '''
    Read and process input
    '''
    monkeynr = 0
    for rawMonkeyDataBlock in MonkeyRawData:
        rawMonkeyDataLines = rawMonkeyDataBlock.split("\n")
        # 1/4fill itemlist
        for worrylvl in rawMonkeyDataLines[1].strip().split(":")[1].split(","):
            MonkeyItemList[monkeynr].append(int(worrylvl))
        # 2/4 OperationsList
        MonkeyOperationList.append(rawMonkeyDataLines[2].strip().split(":")[
                                   1].split("=")[1].strip().split(" "))

        # 3/4 MonkeyTestDivList
        MonkeyTestDivList.append(
            int(rawMonkeyDataLines[3].strip().split(" by ")[1]))

        # 4/4 MonkeyTestDivList
        MonkeyTrowToList.append((int(rawMonkeyDataLines[4].strip().split(" monkey ")[
                                1]), int(rawMonkeyDataLines[5].strip().split(" monkey ")[1])))
        monkeynr += 1

    '''
    calc steps
    '''
    round = 0
    while round < 20:
        # per monkey
        for monkeynr in range(0, len(MonkeyRawData)):
            # for each item in monkey worrylist apply worry penalty // 3
            monkerange = len(MonkeyItemList[monkeynr])
            while len(MonkeyItemList[monkeynr]) > 0:
                MonkeyInspectionCounterList[monkeynr] += 1
                item = MonkeyItemList[monkeynr].popleft()
                if MonkeyOperationList[monkeynr][2] == 'old':
                    op2 = item
                else:
                    op2 = int(MonkeyOperationList[monkeynr][2])
                item = switch(MonkeyOperationList[monkeynr][1], item, op2)//3
                # and test if should be trown:
                if item % MonkeyTestDivList[monkeynr] == 0:
                    MonkeyItemList[MonkeyTrowToList[monkeynr][0]].append(item)
                else:
                    MonkeyItemList[MonkeyTrowToList[monkeynr][1]].append(item)
        round += 1

    MonkeyInspectionCounterList.sort(reverse=True)
    return MonkeyInspectionCounterList[0]*MonkeyInspectionCounterList[1]


def part2(path):
    with open(path) as f:
        data = f.read()
    MonkeyRawData = data.split("\n\n")
    MonkeyItemList = [deque()for _ in range(0, len(MonkeyRawData))]
    MonkeyOperationList = []
    MonkeyTestDivList = []
    MonkeyTrowToList = []
    MonkeyInspectionCounterList = [0 for _ in range(0, len(MonkeyRawData))]
    '''
    Read and process input
    '''
    monkeynr = 0
    for rawMonkeyDataBlock in MonkeyRawData:
        rawMonkeyDataLines = rawMonkeyDataBlock.split("\n")
        # 1/4fill itemlist
        for worrylvl in rawMonkeyDataLines[1].strip().split(":")[1].split(","):
            MonkeyItemList[monkeynr].append(int(worrylvl))
        # 2/4 OperationsList
        MonkeyOperationList.append(rawMonkeyDataLines[2].strip().split(":")[
                                   1].split("=")[1].strip().split(" "))

        # 3/4 MonkeyTestDivList
        MonkeyTestDivList.append(
            int(rawMonkeyDataLines[3].strip().split(" by ")[1]))

        # 4/4 MonkeyTestDivList
        MonkeyTrowToList.append((int(rawMonkeyDataLines[4].strip().split(" monkey ")[
                                1]), int(rawMonkeyDataLines[5].strip().split(" monkey ")[1])))
        monkeynr += 1

    '''
    calc steps
    '''
    round = 0
    while round < 10000:
        # per monkey
        for monkeynr in range(0, len(MonkeyRawData)):
            # for each item in monkey worrylist apply worry penalty
            monkerange = len(MonkeyItemList[monkeynr])
            while len(MonkeyItemList[monkeynr]) > 0:
                MonkeyInspectionCounterList[monkeynr] += 1
                item = MonkeyItemList[monkeynr].popleft()
                # check if higher than 1000, then we need to use the magic
                if item > 1000:
                    item = calcMagic(
                        item, monkeynr, MonkeyOperationList, MonkeyTrowToList, MonkeyTestDivList)
                if MonkeyOperationList[monkeynr][2] == 'old':
                    op2 = item
                else:
                    op2 = int(MonkeyOperationList[monkeynr][2])
                item = switch(MonkeyOperationList[monkeynr][1], item, op2)
                # and test if should be trown:
                if item % MonkeyTestDivList[monkeynr] == 0:
                    MonkeyItemList[MonkeyTrowToList[monkeynr][0]].append(item)
                else:
                    MonkeyItemList[MonkeyTrowToList[monkeynr][1]].append(item)
        round += 1
        if round % 10 == 0:
            print(round)

    MonkeyInspectionCounterList.sort(reverse=True)
    return MonkeyInspectionCounterList[0]*MonkeyInspectionCounterList[1]


def calcMagic(item, monkeynr, OpList, TrowToList, TestDivList):
    copyitem = item
    SimItemList = [deque()for _ in range(0, len(OpList))]
    SimItemList[monkeynr].append(item)
    HistItemValue = []
    HistItemRestValue = []
    HistModValue = []
    HistItemOp = []
    HistItemOp2 = []
    # first we need to play all the steps for one item during a round
    # length of oplist tell us how many monkeys there are
    for simMonkeyNr in range(monkeynr, len(OpList)):
        if len(SimItemList[simMonkeyNr]) > 0:
            item = SimItemList[simMonkeyNr].popleft()
            if OpList[simMonkeyNr][2] == 'old':
                op2 = item
            else:
                op2 = int(OpList[simMonkeyNr][2])
            item = switch(OpList[simMonkeyNr][1], item, op2)
            HistItemOp.append(OpList[simMonkeyNr][1])
            HistItemOp2.append(op2)
            # and test if should be thrown:
            if item % TestDivList[simMonkeyNr] == 0:
                SimItemList[TrowToList[simMonkeyNr][0]].append(item)
            else:
                SimItemList[TrowToList[simMonkeyNr][1]].append(item)
            HistModValue.append(TestDivList[simMonkeyNr])
            HistItemValue.append(item)
            HistItemRestValue.append(item % TestDivList[simMonkeyNr])
    leftover = item % TestDivList[simMonkeyNr]
    rangestart = (item - leftover)//TestDivList[simMonkeyNr]
    rangeend = item - leftover
    for x in range(rangestart, rangeend, TestDivList[simMonkeyNr]):
        lastToCheck = x + leftover
        substituteFound = True
        for y in range(0, len(HistItemOp)-1):
            y = len(HistItemOp) - y - 1
            if HistItemOp[y] == '*':
                lastToCheck = lastToCheck / HistItemOp2[y]
            elif HistItemOp[y] == '+':
                lastToCheck = lastToCheck - HistItemOp2[y]
            if lastToCheck % HistModValue[y-1] != HistItemRestValue[y-1]:
                substituteFound = False
                break
            else:
                pass
        if substituteFound:
            return lastToCheck
    print("Something wrong")
    exit()


# Run when this script is not imported by another script(e.g. Unittest)
if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', part1("2022/11/inputs/input.txt"))
    print("### part 1 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    print('part 2:', part2("2022/11/inputs/input.txt"))
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))

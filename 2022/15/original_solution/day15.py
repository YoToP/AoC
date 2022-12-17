from time import time
from collections import deque
''' 
day15
'''
def mhd(x_value,y_value,x_goal,y_goal):
    return abs(x_value - x_goal) + abs(y_value - y_goal)

def inside(a_start,a_end,b_start,b_end): # is b inside a?
    if (a_start <= b_start) and (a_end >= b_end):
        return True
    return False

def extends(a_start,a_end,b_start,b_end):
    if (a_end >= b_start) and (a_start <= b_start) and ( a_end < b_end): #does b extends a?
        return True
    return False

def calcPositionsInRow(sensorList,beaconList,ypos):
    rangesOnTarget = deque()
    for i in range(0,len(sensorList)):
        maxrange = mhd(sensorList[i][0],sensorList[i][1],beaconList[i][0],beaconList[i][1])
        if sensorList[i][1] in range(ypos-maxrange,ypos+maxrange):
            over = maxrange - abs(sensorList[i][1] - ypos)
            if over == 0:
                rangesOnTarget.append((sensorList[i][0],sensorList[i][0]))
            else:
                rangesOnTarget.append((sensorList[i][0]-over,sensorList[i][0]+over))

    bUsed = True
    rangesToCheck = len(rangesOnTarget)
    while rangesToCheck > 0:
        bUsed = False
        _tempRange = rangesOnTarget.pop()
        for i in range(0,len(rangesOnTarget)):
            if inside(rangesOnTarget[i][0], rangesOnTarget[i][1], _tempRange[0], _tempRange[1]):
                bUsed = True
            elif extends(rangesOnTarget[i][0], rangesOnTarget[i][1], _tempRange[0], _tempRange[1]):
                rangesOnTarget[i] = (rangesOnTarget[i][0],_tempRange[1])
                bUsed = True
            elif extends(_tempRange[0],_tempRange[1],rangesOnTarget[i][0], rangesOnTarget[i][1]):
                rangesOnTarget[i] = (_tempRange[0],rangesOnTarget[i][1])
                bUsed = True
        if bUsed:
            rangesToCheck = len(rangesOnTarget)
        elif not bUsed:
            rangesToCheck -= 1
            rangesOnTarget.appendleft(_tempRange)

    return rangesOnTarget

def part1(path,ypos):
    with open(path) as f:
        lines = f.readlines()
    sensorList = []
    beaconList = []
    for line in lines:
        sensor,beacon = line.strip().split(":")
        sensorX,sensorY = sensor.split(", ")
        sensorX = int(sensorX.split("=")[1])
        sensorY = int(sensorY.split("=")[1])
        sensorList.append((sensorX,sensorY))

        beaconX,beaconY = beacon.split(", ")
        beaconX = int(beaconX.split("=")[1])
        beaconY = int(beaconY.split("=")[1])
        beaconList.append((beaconX,beaconY))
    return calcPositionsInRow(sensorList,beaconList,ypos)

    


def part2(path):
    with open(path) as f:
        lines = f.readlines()
    sensorList = []
    beaconList = []
    for line in lines:
        sensor,beacon = line.strip().split(":")
        sensorX,sensorY = sensor.split(", ")
        sensorX = int(sensorX.split("=")[1])
        sensorY = int(sensorY.split("=")[1])
        sensorList.append((sensorX,sensorY))

        beaconX,beaconY = beacon.split(", ")
        beaconX = int(beaconX.split("=")[1])
        beaconY = int(beaconY.split("=")[1])
        beaconList.append((beaconX,beaconY))

    for ypos in range(1,4000000):
        rangeList = calcPositionsInRow(sensorList,beaconList,ypos)
        if len(rangeList) > 1:
            return (rangeList[0][1]+1) * 4000000 + ypos
    return 0


if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    r1,r2 = part1("2022/15/inputs/input.txt",2000000)[0]
    p1answer = abs(r1) + abs(r2)
    print(f'part 1:{p1answer}')
    print('part 2:', part2("2022/15/inputs/input.txt"))
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))

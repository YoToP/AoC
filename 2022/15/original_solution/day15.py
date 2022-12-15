from time import time
from collections import deque
''' 
day15
'''
def mhd(x_value,y_value,x_goal,y_goal):
    return abs(x_value - x_goal) + abs(y_value - y_goal)

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


    rangesOnTarget = []

    for i in range(0,len(sensorList)):
        maxrange = mhd(sensorList[i][0],sensorList[i][1],beaconList[i][0],beaconList[i][1])
        if sensorList[i][1] in range(ypos-maxrange,ypos+maxrange):
            over = maxrange - abs(sensorList[i][1] - ypos)
            if over == 0:
                rangesOnTarget.append((sensorList[i][0],sensorList[i][0]))
            else:
                rangesOnTarget.append((sensorList[i][0]-over,sensorList[i][0]+over))
    
    for xrange in rangesOnTarget:
        pass
    return rangesOnTarget


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

    for ypos in range(0,4000000):
        takenXlist = set()
        xMin = 10000000
        xMax = 0
        for i in range(0,len(sensorList)):
            maxrange = mhd(sensorList[i][0],sensorList[i][1],beaconList[i][0],beaconList[i][1])
            if sensorList[i][1] in range(ypos-maxrange,ypos+maxrange):
                over = maxrange - abs(sensorList[i][1] - ypos)
                if over == 0:
                    x = sensorList[i][0]
                    if x > xMax:
                        xMax = x
                    elif x <xMin:
                        xMin = x
                    takenXlist.add(sensorList[i][0])
                else:
                    for x in range(sensorList[i][0]-over,sensorList[i][0]+over):
                        if x > xMax:
                            xMax = x
                        elif x <xMin:
                            xMin = x
                        takenXlist.add(x)
        if xMin < 0:
            xMin = 0
        diff = xMax - xMin
    return 0


if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', len(part1("2022/15/inputs/input.txt",2000000)))
    #print('part 2:', part2("2022/15/inputs/input.txt"))
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))

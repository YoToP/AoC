from time import time
from collections import deque
''' 
day16
'''

class Node:
    def __init__(self, data,ppm):
        self.nodes = []
        self.name = name
        self.ppm = ppm
    
    def __repr__(self):
        return f'Node("{self.name}","{self.nodes})'

    def addNode(self,node):
        self.nodes.append(node)

def alreadyVisited(pList,currentValve,nextValve):
    maxRange = len(pList)
    for i in range(0,maxRange):
        if pList[i] == currentValve:
            if i+1 < maxRange:
                if pList[i+1] == nextValve:
                    return True
    return False


    def checkPosibilitiesNG(valveList,minutes,currentValve):
        if minutes < 2:
            for valve in valveList[currentValve][1]:
                if not alreadyVisited(allPosibillities, currentValve, valve):
                    _list = checkPosibilities(valveList,minutes+1,valve)
                    for _plist in _list:
                        _temp = [currentValve]
                        _temp.extend(_plist)
                        allPosibillities.append(_temp)
        else:
            for _plist in allPosibillities:
                _plist.append([currentValve])


def checkPosibilities(valveList,history,minutes,currentValve):
    history.append(currentValve)
    pList = []
    if minutes < 30:
        for valve in valveList[currentValve][1]:
            if not alreadyVisited(history, currentValve, valve):
                _list = checkPosibilities(valveList,history,minutes+1,valve)
                for _plist in _list:
                    _temp = [currentValve]
                    _temp.extend(_plist)
                    pList.append(_temp)
    else:
        pList.append([currentValve])

    return pList

#https://hellokoding.com/shortest-paths/
def part1(path):
    with open(path) as f:
        lines = f.readlines()
    valveList = {}
    startingValve = None
    for line in lines:
        valveandflow,leadsTo = line.strip().split("; ")
        valve = valveandflow.split(" ")[1]
        if startingValve == None:
            startingValve = valve
        flow = int(valveandflow.split("=")[1])
        leadsTo = leadsTo.split(" ")
        leadsTo = leadsTo[4:len(leadsTo)]
        for i in range(0,len(leadsTo)):
            leadsTo[i] = leadsTo[i][0:2]
        valveList[valve] = (flow,leadsTo)

    allPosibillities = checkPosibilities(valveList,[],1,startingValve)

    return 0


def part2(path):
    with open(path) as f:
        lines = f.readlines()

    return 0


if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', part1("2022/16/inputs/example.txt"))
    #print('part 2:', part2("2022/16/inputs/input.txt"))
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))

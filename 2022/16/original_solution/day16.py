from time import time
from collections import deque,defaultdict
''' 
day16
test
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


def ShortestPathByBFS(g, source):
        INFINITE = int(len(g) * 2)
        UNDEFINED = -1
        distances = defaultdict(lambda:INFINITE)
        predecessors = defaultdict(lambda:UNDEFINED)

        distances[source] = 0

        visited = defaultdict(lambda:False)
        visited[source] = True

        queue = deque()
        queue.append(source)

        while len(queue) > 0:
            u = queue.popleft()

            for v in g[u][1]:
                if visited[v] != True:
                    visited[v] = True
                    distances[v] = distances[u] + 1
                    predecessors[v] = u
                    queue.append(v)

        return distances







def checkPosibilities(valveList,minutes,currentValve):
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
    valveListWithFlow = []
    startingValve = None
    for line in lines:
        valveandflow,leadsTo = line.strip().split("; ")
        valve = valveandflow.split(" ")[1]
        if startingValve == None:
            startingValve = valve
        flow = int(valveandflow.split("=")[1])
        if flow > 0:
            valveListWithFlow.append((valve,flow))
        leadsTo = leadsTo.split(" ")
        leadsTo = leadsTo[4:len(leadsTo)]
        for i in range(0,len(leadsTo)):
            leadsTo[i] = leadsTo[i][0:2]
        valveList[valve] = (flow,leadsTo)

    def CalcFlow(valveListWithFlow,currentflow,minutes,currentVale):
        highestFlow = currentflow
        if minutes < 2:
            Distances = ShortestPathByBFS(valveList,currentVale)
            for i in range(0,len(valveListWithFlow)):
                valve,flow = valveListWithFlow[i]
                _tempValveList = valveListWithFlow.copy()
                _tempValveList.remove((valve,flow))
                _tempDist = CalcFlow(_tempValveList, currentflow*Distances[valve], minutes+Distances[valve], valve)
                if _tempDist > highestFlow:
                    highestFlow = _tempDist

        return highestFlow

    highestValue = CalcFlow(valveListWithFlow.copy(),0,0,startingValve)

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


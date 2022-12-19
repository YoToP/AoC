from time import time
from collections import defaultdict, deque


def ShortestPathByBFS(g, source):
    INFINITE = int(1e8)
    UNDEFINED = -1
    distances = defaultdict(lambda: INFINITE)
    predecessors = defaultdict(lambda: UNDEFINED)

    distances[source] = 0

    visited = defaultdict(lambda: False)
    visited[source] = True

    queue = deque()
    queue.append(source)

    while len(queue) > 0:
        u = queue.popleft()

        for v in g[u]:
            if visited[v] != True:
                visited[v] = True
                distances[v] = distances[u] + 1
                predecessors[v] = u
                queue.append(v)

    return distances


def minVertex(queue, distance):
    INFINITE = int(1e8)
    UNDEFINED = -1
    for v in queue:
        if minDistance > distance[v]:
            minDistance = distance[v]
            minVertex = v
    return minVertex


def part1(path):
    with open(path) as f:
        lines = f.readlines()
    matrix = []
    height = 0
    width = 0
    startI = 0
    startJ = 0
    endI = 0
    endJ = 0
    for line in lines:  # load playing field into matrix
        height += 1
        line = line.replace('\n', '')
        width = len(line)
        lstLine = []
        for nr in line:
            if nr == 'S':
                lstLine.append(0)
                startI = height-1
                startJ = len(lstLine)-1
            elif nr == 'E':
                endI = height-1
                lstLine.append(ord(('z'))-ord('a')+2)
                endJ = len(lstLine)-1
            else:
                lstLine.append(ord((nr))-ord('a')+1)
        matrix.append(lstLine)

    # create Adjeceny list
    #(0,0), [(0,1),(1,0)]
    AList = defaultdict(lambda: [])
    for i in range(0, height):
        for j in range(0, width):
            _currentValue = matrix[i][j]
            if i > 0:
                if matrix[i-1][j] - _currentValue < 2:
                    AList[(i, j)].append((i-1, j))
            if i < height-1:
                if matrix[i+1][j] - _currentValue < 2:
                    AList[(i, j)].append((i+1, j))
            if j < width-1:
                if matrix[i][j+1] - _currentValue < 2:
                    AList[(i, j)].append((i, j+1))
            if j > 0:
                if matrix[i][j-1] - _currentValue < 2:
                    AList[(i, j)].append((i, j-1))

    out = ShortestPathByBFS(AList, (startI, startJ))[(endI, endJ)]

    return out


def part2(path):
    with open(path) as f:
        lines = f.readlines()
    matrix = []
    height = 0
    width = 0
    endI = 0
    endJ = 0
    StartingPointsList = []
    for line in lines:  # load playing field into matrix
        height += 1
        line = line.replace('\n', '')
        width = len(line)
        lstLine = []
        for nr in line:
            if nr == 'S':
                lstLine.append(0)
                StartingPointsList.append((height-1, len(lstLine)-1))
            elif nr == 'E':
                endI = height-1
                lstLine.append(ord(('z'))-ord('a')+2)
                endJ = len(lstLine)-1
            else:
                lstLine.append(ord((nr))-ord('a')+1)
                if nr == 'a':
                    StartingPointsList.append((height-1, len(lstLine)-1))
        matrix.append(lstLine)

    # create Adjeceny list
    #(0,0), [(0,1),(1,0)]
    AList = defaultdict(lambda: [])
    for i in range(0, height):
        for j in range(0, width):
            _currentValue = matrix[i][j]
            if i > 0:
                if matrix[i-1][j] - _currentValue < 2:
                    AList[(i, j)].append((i-1, j))
            if i < height-1:
                if matrix[i+1][j] - _currentValue < 2:
                    AList[(i, j)].append((i+1, j))
            if j < width-1:
                if matrix[i][j+1] - _currentValue < 2:
                    AList[(i, j)].append((i, j+1))
            if j > 0:
                if matrix[i][j-1] - _currentValue < 2:
                    AList[(i, j)].append((i, j-1))
    lowest = 1000
    for sp in StartingPointsList:
        out = ShortestPathByBFS(AList, sp)[(endI, endJ)]
        if out < lowest:
            lowest = out

    return lowest


# Run when this script is not imported by another script(e.g. Unittest)
if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    p1time = start_time
    path = "2022/12/inputs/input.txt"
    print("part 1:", part1(path))
    print("### run time p1 is %s miliseconds" %
          (int(round(time() * 1000)) - p1time))
    p2time = int(round(time() * 1000))
    print("part 2:", part2("2022/12/inputs/input.txt"))
    print("### run time p2 is %s miliseconds" %
          (int(round(time() * 1000)) - p2time))
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))

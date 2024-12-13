from time import time
from collections import defaultdict

matrix = [] #main playing field
foundCoords = set() #Set for storing unique positions
def isTrailhead(position, prevValue: int):
    _score = 0
    if position[0] > 0: #then check up
        nextPosition = (position[0]-1,position[1])
        nextValue = matrix[nextPosition[0]][nextPosition[1]]
        if nextValue - prevValue == 1:
            if nextValue == 9:
                _score += 1
                foundCoords.add(nextPosition)
            else:
                _score += isTrailhead(nextPosition,nextValue)
    if position[1] < len(matrix[0])-1: #then check right
        nextPosition = (position[0],position[1]+1)
        nextValue = matrix[nextPosition[0]][nextPosition[1]]
        if nextValue - prevValue == 1:
            if nextValue == 9:
                _score += 1
                foundCoords.add(nextPosition)
            else:
                _score += isTrailhead((position[0],position[1]+1),nextValue)
    if position[0] < len(matrix)-1: #then check down
        nextPosition = (position[0]+1,position[1])
        nextValue = matrix[nextPosition[0]][nextPosition[1]]
        if nextValue - prevValue == 1:
            if nextValue == 9:
                _score += 1
                foundCoords.add(nextPosition)
            else:
                _score += isTrailhead((position[0]+1,position[1]),nextValue)
    if position[1] > 0: #then check left
        nextPosition = (position[0],position[1]-1)
        nextValue = matrix[nextPosition[0]][nextPosition[1]]
        if nextValue - prevValue == 1:
            if nextValue == 9:
                _score += 1
                foundCoords.add(nextPosition)
            else:
                _score += isTrailhead((position[0],position[1]-1),nextValue)
    return _score

def p1():
    trailStarts = []
    with open("2024/10/inputs/input.txt") as f:
        i = 0
        for line in f.read().split('\n'):
            j = 0
            row = []
            for char in line:
                if char == '0':
                    trailStarts.append((i,j))
                row.append(int(char))
                j += 1
            matrix.append(row)
            i += 1
    score = 0
    for _trailStart in trailStarts:
        foundCoords.clear()
        isTrailhead(_trailStart,0)
        score += len(foundCoords)
    return score

def p2():
    trailStarts = []
    with open("2024/10/inputs/input.txt") as f:
        i = 0
        for line in f.read().split('\n'):
            j = 0
            row = []
            for char in line:
                if char == '0':
                    trailStarts.append((i,j))
                row.append(int(char))
                j += 1
            matrix.append(row)
            i += 1
    score = 0
    for _trailStart in trailStarts:
        foundCoords.clear()
        score += isTrailhead(_trailStart,0)
    return score

if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', p1())
    print("### p1 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    matrix.clear()
    start_time = int(round(time() * 1000))
    print('part 2:', p2())
    print("### p2 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
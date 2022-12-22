from time import time
from collections import defaultdict

def calcSurface(cubeList):
    visList = [6] * len(cubeList)
    for i in range(0,len(cubeList)):
        x,y,z = cubeList[i]
        for j in range(0,len(cubeList)):
            k,l,m = cubeList[j]
            if abs(x-k) == 1 and y ==l and z == m:
                visList[i] -= 1
            elif x == k and abs(y-l) == 1 and z == m:
                visList[i] -= 1    
            elif x == k and y ==l and abs(z-m) == 1:
                visList[i] -= 1   
    result = 0
    for v in visList:
        result += v
    return result

def addMissingBlock(cubeList):
    pockets = defaultdict(int) # if counter = 6, then should be added to as block
    for i in range(0,len(cubeList)):
        x,y,z = cubeList[i]
        pockets[f"{x+1},{y},{z}"] += 1
        pockets[f"{x-1},{y},{z}"] += 1
        pockets[f"{x},{y+1},{z}"] += 1
        pockets[f"{x},{y-1},{z}"] += 1
        pockets[f"{x},{y},{z+1}"] += 1
        pockets[f"{x},{y},{z-1}"] += 1
    copyPockets = pockets.copy()
    returnList = []
    for pocket in pockets:

        if pockets[pocket] == 5:
            items = pocket.split(",")
            items = [int(items[0]),int(items[1]),int(items[2])]
            x,y,z = items
            if copyPockets[f"{x+1},{y},{z}"] == 5: pockets[pocket] = 6
            if copyPockets[f"{x-1},{y},{z}"] == 5: pockets[pocket] = 6
            if copyPockets[f"{x},{y+1},{z}"] == 5: pockets[pocket] = 6
            if copyPockets[f"{x},{y-1},{z}"] == 5: pockets[pocket] = 6
            if copyPockets[f"{x},{y},{z+1}"] == 5: pockets[pocket] = 6
            if copyPockets[f"{x},{y},{z-1}"] == 5: pockets[pocket] = 6
        if pockets[pocket] == 6:
            items = pocket.split(",")
            items = [int(items[0]),int(items[1]),int(items[2])]
            if items not in cubeList:
                returnList.append(items)
    
    return returnList

def isAdjecentValue(xyz,value):
    z,y,z = xyz
    global matrix
    if matrix[x-1][y][z] == value:
        return True
    elif matrix[x+1][y][z] == value:
        return True
    elif matrix[x][y+1][z] == value:
        return True
    elif matrix[x][y-1][z] == value:
        return True
    elif matrix[x][y][z+1] == value:
        return True
    elif matrix[x][y][z-1] == value:
        return True
    return False



def part1(path):
    with open(path) as f:
        lines = f.readlines()
    cubeList = []
    for line in lines:
        items = line.strip().split(",")
        cubeList.append([int(items[0]),int(items[1]),int(items[2])])

    return calcSurface(cubeList)


def part2(path):
    with open(path) as f:
        lines = f.readlines()
    cubeList = []
    global matrix
    matrix = [[ [0 for col in range(2)] for col in range(2)] for row in range(3)]
    for line in lines:
        items = line.strip().split(",")
        cubeList.append([int(items[0]),int(items[1]),int(items[2])])

    xHigh = 0
    yHigh = 0
    zHigh = 0
    for x,y,z in cubeList:
        if x > xHigh:
            xHigh = x
        if y > yHigh:
            yHigh = y
        if z > zHigh:
            zHigh = z
    xHigh += 1
    yHigh += 1
    zHigh += 1
    matrix = [[ [0 for col in range(xHigh)] for col in range(yHigh)] for row in range(zHigh)]
    for x,y,z in cubeList:
        matrix[x][y][z] = 1
    
    for j in range(yHigh):
        for k in range(zHigh):
            if matrix[0][j][k] != 1:
                matrix[0][j][k] = -1
            if matrix[xHigh-1][j][k] != 1:
                matrix[xHigh-1][j][k] = -1
    for i in range(xHigh):
        for k in range(zHigh):
            if matrix[i][0][k] != 1:
                matrix[i][0][k] = -1
            if matrix[i][yHigh-1][k] != 1:
                matrix[i][yHigh-1][k] = -1
    for i in range(xHigh):
        for j in range(yHigh):
            if matrix[i][j][0] != 1:
                matrix[i][j][0] = -1
            if matrix[i][j][zHigh-1] != 1:
                matrix[i][j][zHigh-1] = -1
    start = 1
    end = xHigh-2
    while start < end:
        for j in range(start,end+1):
            for k in range(start,end+1):
                if matrix[start-1][j][k] == -1:
                    if matrix[start][j][k] != 1:
                        matrix[start][j][k] = -1
                elif matrix[start+1][j][k] == -1:
                    if matrix[start][j][k] != 1:
                        matrix[start][j][k] = -1
                elif matrix[start][j-1][k] == -1:
                    if matrix[start][j][k] != 1:
                        matrix[start][j][k] = -1
                elif matrix[start][j+1][k] == -1:
                    if matrix[start][j][k] != 1:
                        matrix[start][j][k] = -1
                elif matrix[start][j][k-1] == -1:
                    if matrix[start][j][k] != 1:
                        matrix[start][j][k] = -1
                elif matrix[start][j][k+1] == -1:
                    if matrix[start][j][k] != 1:
                        matrix[start][j][k] = -1
                if matrix[end-1][j][k] == -1:
                    if matrix[end][j][k] != 1:
                        matrix[end][j][k] = -1
                elif matrix[end+1][j][k] == -1:
                    if matrix[end][j][k] != 1:
                        matrix[end][j][k] = -1
                elif matrix[end][j-1][k] == -1:
                    if matrix[end][j][k] != 1:
                        matrix[end][j][k] = -1
                elif matrix[end][j+1][k] == -1:
                    if matrix[end][j][k] != 1:
                        matrix[end][j][k] = -1
                elif matrix[end][j][k-1] == -1:
                    if matrix[end][j][k] != 1:
                        matrix[end][j][k] = -1
                elif matrix[end][j][k+1] == -1:
                    if matrix[end][j][k] != 1:
                        matrix[end][j][k] = -1
        for i in range(start,end+1):
            for k in range(start,end+1):
                if matrix[i-1][start][k] == -1:
                    if matrix[i][start][k] != 1:
                        matrix[i][start][k] = -1
                elif matrix[i+1][start][k] == -1:
                    if matrix[i][start][k] != 1:
                        matrix[i][start][k] = -1
                elif matrix[i][start+1][k] == -1:
                    if matrix[i][start][k] != 1:
                        matrix[i][start][k] = -1
                elif matrix[i][start-1][k] == -1:
                    if matrix[i][start][k] != 1:
                        matrix[i][start][k] = -1
                elif matrix[i][start][k+1] == -1:
                    if matrix[i][start][k] != 1:
                        matrix[i][start][k] = -1
                elif matrix[i][start][k-1] == -1:
                    if matrix[i][start][k] != 1:
                        matrix[i][start][k] = -1
                if matrix[i-1][end][k] == -1:
                    if matrix[i][end][k] != 1:
                        matrix[i][end][k] = -1
                elif matrix[i+1][end][k] == -1:
                    if matrix[i][end][k] != 1:
                        matrix[i][end][k] = -1
                elif matrix[i][end+1][k] == -1:
                    if matrix[i][end][k] != 1:
                        matrix[i][end][k] = -1
                elif matrix[i][end-1][k] == -1:
                    if matrix[i][end][k] != 1:
                        matrix[i][end][k] = -1
                elif matrix[i][end][k+1] == -1:
                    if matrix[i][end][k] != 1:
                        matrix[i][end][k] = -1
                elif matrix[i][end][k-1] == -1:
                    if matrix[i][end][k] != 1:
                        matrix[i][end][k] = -1
        for i in range(start,end+1):
            for j in range(start,end+1):
                if matrix[i-1][j][start] == -1:
                    if matrix[i][j][start] != 1:
                        matrix[i][j][start] = -1
                elif matrix[i+1][j][start] == -1:
                    if matrix[i][j][start] != 1:
                        matrix[i][j][start] = -1
                elif matrix[i][j-1][start] == -1:
                    if matrix[i][j][start] != 1:
                        matrix[i][j][start] = -1
                elif matrix[i][j+1][start] == -1:
                    if matrix[i][j][start] != 1:
                        matrix[i][j][start] = -1
                elif matrix[i][j][start-1] == -1:
                    if matrix[i][j][start] != 1:
                        matrix[i][j][start] = -1
                elif matrix[i][j][start+1] == -1:
                    if matrix[i][j][start] != 1:
                        matrix[i][j][start] = -1
                if matrix[i-1][j][end] == -1:
                    if matrix[i][j][end] != 1:
                        matrix[i][j][end] = -1
                elif matrix[i+1][j][end] == -1:
                    if matrix[i][j][end] != 1:
                        matrix[i][j][end] = -1
                elif matrix[i][j-1][end] == -1:
                    if matrix[i][j][end] != 1:
                        matrix[i][j][end] = -1
                elif matrix[i][j+1][end] == -1:
                    if matrix[i][j][end] != 1:
                        matrix[i][j][end] = -1
                elif matrix[i][j][end-1] == -1:
                    if matrix[i][j][end] != 1:
                        matrix[i][j][end] = -1
                elif matrix[i][j][end+1] == -1:
                    if matrix[i][j][end] != 1:
                        matrix[i][j][end] = -1
        start += 1
        end -= 1
    extra = []
    for i in range(xHigh):
        for j in range(yHigh):
            for k in range(zHigh):
                if matrix[i][j][k] == 0:
                    if [i,j,k] not in extra:
                        extra.append([i,j,k])
                if matrix[i][j][k] == 1:
                    if [i,j,k] not in extra:
                        extra.append([i,j,k])        
    extra.extend(addMissingBlock(extra))
    extra.extend(addMissingBlock(extra))
    return calcSurface(extra)


# Run when this script is not imported by another script(e.g. Unittest)
if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    p1time = start_time
    path = "2022/18/inputs/input.txt"
    #print("part 1:", part1(path))
    print("### run time p1 is %s miliseconds" %
          (int(round(time() * 1000)) - p1time))
    
    p2time = int(round(time() * 1000))
    print("part 2:", part2("2022/18/inputs/input.txt"))
    print("### run time p2 is %s miliseconds" %
          (int(round(time() * 1000)) - p2time))
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))

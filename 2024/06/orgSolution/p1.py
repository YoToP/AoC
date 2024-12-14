from time import time

matrix = []
startingPos = (0,0)
visitedPlacesP2 = set() #used for part2 where we need direction info to know if we are looping
def createMatrixAndFindStartPos():
    _startPos = (0,0)
    with open("2024/06/inputs/input.txt") as f:
        i = 0
        for line in f.readlines():
            if '^' in line:
                j = line.find('^')
                _startPos = (i,j)
            matrix.append(list(line.strip()))
            i += 1
    return _startPos

visitedPlaces = set() #used in P1 to count, but in P2 to loop over because these are all the places we need to put a block for testing
def p1(currentPos=(0,0)):
    direction = '^' #others are '>' 'v' '<'
    outOfBounds = False
    while not outOfBounds:
        rotated = False
        if direction == '^': # go up until obstacle or oob
            i = currentPos[0]
            j = currentPos[1]
            while i >= 0:
                char = matrix[i][j]
                if matrix[i][j] != '#':
                    currentPos = (i,j)
                    visitedPlaces.add(currentPos)
                    i -= 1
                elif matrix[i][j] == '#':
                    direction = '>'
                    rotated = True
                    break
        elif direction == '>':
            i = currentPos[0]
            j = currentPos[1]
            while j < len(matrix[0]):
                if matrix[i][j] != '#':
                    currentPos = (i,j)
                    visitedPlaces.add(currentPos)
                    j += 1
                elif matrix[i][j] == '#':
                    direction = 'v'
                    rotated = True
                    break
        elif direction == 'v': # go down until obstacle or oob
            i = currentPos[0]
            j = currentPos[1]
            while i < len(matrix):
                if matrix[i][j] != '#':
                    currentPos = (i,j)
                    visitedPlaces.add(currentPos)
                    i += 1
                elif matrix[i][j] == '#':
                    direction = '<'
                    rotated = True
                    break
        elif direction == '<':
            i = currentPos[0]
            j = currentPos[1]
            while j >= 0:
                if matrix[i][j] != '#':
                    currentPos = (i,j)
                    visitedPlaces.add(currentPos)
                    j -= 1
                elif matrix[i][j] == '#':
                    direction = '^'
                    rotated = True
                    break
        if not rotated:
            outOfBounds = True
    return len(visitedPlaces)

#datastruct ((i,j)direction)
def isLoop(currentPos=(0,0)) -> bool:
    direction = '^' #others are '>' 'v' '<'
    outOfBounds = False
    isLoop = False
    _visited = set()
    currentPosAndDir = (currentPos,'.')
    while (not outOfBounds) or (not isLoop):
        rotated = False
        if direction == '^': # go up until obstacle or oob
            i = currentPosAndDir[0][0]
            j = currentPosAndDir[0][1]
            while i >= 0:
                char = matrix[i][j]
                if matrix[i][j] != '#':
                    currentPosAndDir = ((i,j),'^')
                    if currentPosAndDir in _visited:
                        isLoop = True
                        break
                    _visited.add(currentPosAndDir)
                    i -= 1
                elif matrix[i][j] == '#':
                    direction = '>'
                    rotated = True
                    break
        elif direction == '>':
            i = currentPosAndDir[0][0]
            j = currentPosAndDir[0][1]
            while j < len(matrix[0]):
                if matrix[i][j] != '#':
                    currentPosAndDir = ((i,j),'>')
                    if currentPosAndDir in _visited:
                        isLoop = True
                        break
                    _visited.add(currentPosAndDir)
                    j += 1
                elif matrix[i][j] == '#':
                    direction = 'v'
                    rotated = True
                    break
        elif direction == 'v': # go down until obstacle or oob
            i = currentPosAndDir[0][0]
            j = currentPosAndDir[0][1]
            while i < len(matrix):
                if matrix[i][j] != '#':
                    currentPosAndDir = ((i,j),'v')
                    if currentPosAndDir in _visited:
                        isLoop = True
                        break
                    _visited.add(currentPosAndDir)
                    i += 1
                elif matrix[i][j] == '#':
                    direction = '<'
                    rotated = True
                    break
        elif direction == '<':
            i = currentPosAndDir[0][0]
            j = currentPosAndDir[0][1]
            while j >= 0:
                if matrix[i][j] != '#':
                    currentPosAndDir = ((i,j),'<')
                    if currentPosAndDir in _visited:
                        isLoop = True
                        break
                    _visited.add(currentPosAndDir)
                    j -= 1
                elif matrix[i][j] == '#':
                    direction = '^'
                    rotated = True
                    break
        if not rotated:
            outOfBounds = True
            break
    return isLoop


def p2(currentPos=(0,0)):
    score = 0
    for coordinate in visitedPlaces:
        if startingPos != coordinate:
            matrix[coordinate[0]][coordinate[1]] = '#'
            if isLoop(currentPos):
                score += 1
            matrix[coordinate[0]][coordinate[1]] = '.'
    

    return score

if __name__ == '__main__':
    _startPos = createMatrixAndFindStartPos()
    startingPos = _startPos
    start_time = int(round(time() * 1000))
    print('part 1:', p1(_startPos))
    print("### p1 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    start_time = int(round(time() * 1000))
    print('part 2:', p2(_startPos))
    print("### p2 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
from time import time

def p1():
    matrix = []
    currentPos = ()
    with open("2024/06/inputs/input.txt") as f:
        i = 0
        for line in f.readlines():
            if '^' in line:
                j = line.find('^')
                currentPos = (i,j)
            matrix.append(list(line.strip()))
            i += 1
    
    visitedPlaces = set()
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

def p2():

    return 0

if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', p1())
    print("### p1 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    start_time = int(round(time() * 1000))
    print('part 2:', p2())
    print("### p2 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
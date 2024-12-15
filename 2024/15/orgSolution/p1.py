from time import time

def p1():
    matrix = []
    instructionList = []
    currentPos = (0,0)
    with open("2024/15/inputs/input.txt") as f:
        board, instructions = f.read().split("\n\n")
        i = 0
    for line in board.split('\n'):
        if '@' in line:
            currentPos = (i,line.find('@'))
        matrix.append(list(line))
        i += 1
    for ins in instructions.split('\n'):
        instructionList.extend(list(ins))

    for ins in instructionList:
        if ins == '^': # go up until obstacle or oob
            #search free
            hasFreeSpot = False
            freeI = currentPos[0]-1
            nextPos = matrix[freeI][currentPos[1]]
            while nextPos != '#':
                if nextPos == '.':
                    hasFreeSpot = True
                    break
                elif nextPos == 'O':
                    freeI -= 1
                nextPos = matrix[freeI][currentPos[1]]
            if hasFreeSpot:
                for i in range(freeI,currentPos[0]):
                    matrix[i][currentPos[1]] = matrix[i+1][currentPos[1]]
                matrix[currentPos[0]][currentPos[1]] = '.'
                currentPos = (currentPos[0]-1,currentPos[1])
        elif ins == '>':
            hasFreeSpot = False
            freeJ = currentPos[1]+1
            nextPos = matrix[currentPos[0]][freeJ]
            while nextPos != '#':
                if nextPos == '.':
                    hasFreeSpot = True
                    break
                elif nextPos == 'O':
                    freeJ += 1
                nextPos = matrix[currentPos[0]][freeJ]
            if hasFreeSpot:
                for j in range(freeJ,currentPos[1],-1):
                    matrix[currentPos[0]][j] = matrix[currentPos[0]][j-1]
                matrix[currentPos[0]][currentPos[1]] = '.'
                currentPos = (currentPos[0],currentPos[1]+1)
        elif ins == 'v': # go down until obstacle or oob
            hasFreeSpot = False
            freeI = currentPos[0]+1
            nextPos = matrix[freeI][currentPos[1]]
            while nextPos != '#':
                if nextPos == '.':
                    hasFreeSpot = True
                    break
                elif nextPos == 'O':
                    freeI += 1
                nextPos = matrix[freeI][currentPos[1]]
            if hasFreeSpot:
                for i in range(freeI,currentPos[0],-1):
                    matrix[i][currentPos[1]] = matrix[i-1][currentPos[1]]
                matrix[currentPos[0]][currentPos[1]] = '.'
                currentPos = (currentPos[0]+1,currentPos[1])
        elif ins == '<':
            hasFreeSpot = False
            freeJ = currentPos[1]-1
            nextPos = matrix[currentPos[0]][freeJ]
            while nextPos != '#':
                if nextPos == '.':
                    hasFreeSpot = True
                    break
                elif nextPos == 'O':
                    freeJ -= 1
                nextPos = matrix[currentPos[0]][freeJ]
            if hasFreeSpot:
                for j in range(freeJ,currentPos[1]):
                    matrix[currentPos[0]][j] = matrix[currentPos[0]][j+1]
                matrix[currentPos[0]][currentPos[1]] = '.'
                currentPos = (currentPos[0],currentPos[1]-1)

    score = 0
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if matrix[i][j] == 'O':
                score += (100 * i + j)

    return score

def p2():
    matrix = []
    instructionList = []
    currentPos = (0,0)
    with open("2024/15/inputs/example.txt") as f:
        board, instructions = f.read().split("\n\n")
        i = 0
    for line in board.split('\n'):
        row = []
        for char in line:
            if char == '#':
                row.extend(['#','#'])
            elif char == '.':
                row.extend(['.','.'])
            elif char == 'O':
                row.extend(['[',']'])
            elif char == '@':
                row.extend(['@','.'])
                currentPos = (i,line.find('@')*2)
        matrix.append(row)
        i += 1
    for ins in instructions.split('\n'):
        instructionList.extend(list(ins))

    for ins in instructionList:
        if ins == '^': # go up until obstacle or oob
            #search free
            hasFreeSpot = False
            freeI = currentPos[0]-1
            nextPos = matrix[freeI][currentPos[1]]
            while nextPos != '#':
                if nextPos == '.':
                    hasFreeSpot = True
                    break
                elif nextPos == 'O':
                    freeI -= 1
                nextPos = matrix[freeI][currentPos[1]]
            if hasFreeSpot:
                for i in range(freeI,currentPos[0]):
                    matrix[i][currentPos[1]] = matrix[i+1][currentPos[1]]
                matrix[currentPos[0]][currentPos[1]] = '.'
                currentPos = (currentPos[0]-1,currentPos[1])
        elif ins == '>':
            hasFreeSpot = False
            freeJ = currentPos[1]+1
            nextPos = matrix[currentPos[0]][freeJ]
            while nextPos != '#':
                if nextPos == '.':
                    hasFreeSpot = True
                    break
                elif (nextPos == '[') | (nextPos == ']'):
                    freeJ += 1
                nextPos = matrix[currentPos[0]][freeJ]
            if hasFreeSpot:
                for j in range(freeJ,currentPos[1],-1):
                    matrix[currentPos[0]][j] = matrix[currentPos[0]][j-1]
                matrix[currentPos[0]][currentPos[1]] = '.'
                currentPos = (currentPos[0],currentPos[1]+1)
        elif ins == 'v': # go down until obstacle or oob
            hasFreeSpot = False
            freeI = currentPos[0]+1
            nextPos = matrix[freeI][currentPos[1]]
            while nextPos != '#':
                if nextPos == '.':
                    hasFreeSpot = True
                    break
                elif nextPos == 'O':
                    freeI += 1
                nextPos = matrix[freeI][currentPos[1]]
            if hasFreeSpot:
                for i in range(freeI,currentPos[0],-1):
                    matrix[i][currentPos[1]] = matrix[i-1][currentPos[1]]
                matrix[currentPos[0]][currentPos[1]] = '.'
                currentPos = (currentPos[0]+1,currentPos[1])
        elif ins == '<':
            hasFreeSpot = False
            freeJ = currentPos[1]-1
            nextPos = matrix[currentPos[0]][freeJ]
            while nextPos != '#':
                if nextPos == '.':
                    hasFreeSpot = True
                    break
                elif (nextPos == '[') | (nextPos == ']'):
                    freeJ -= 1
                nextPos = matrix[currentPos[0]][freeJ]
            if hasFreeSpot:
                for j in range(freeJ,currentPos[1]):
                    matrix[currentPos[0]][j] = matrix[currentPos[0]][j+1]
                matrix[currentPos[0]][currentPos[1]] = '.'
                currentPos = (currentPos[0],currentPos[1]-1)

    score = 0
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if matrix[i][j] == '[':
                score += (100 * i + j)

    return score

if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', p1())
    print("### p1 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    start_time = int(round(time() * 1000))
    print('part 2:', p2())
    print("### p2 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
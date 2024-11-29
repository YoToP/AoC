from time import time

def p1():
    with open("2023/10/inputs/input.txt") as f:
        _lines = f.readlines()

    #find S
    i = 0
    startFound = False
    for line in _lines:
        j = 0
        for char in line:
            if char == 'S':
                startFound = True
                break
            j += 1
        if startFound:
            break
        i += 1
    
    matrix = []
    for line in _lines:
        matrix.append(list(line.strip()))
    score = 0

    currentSegment = 'S'
    matrix[i][j] = score
    OneMoreRound = True
    nogoCounter = 0
    while True:
        #check north
        if i > 0 and (currentSegment == 'S' or currentSegment == '|' or currentSegment == 'L' or currentSegment == 'J'): # dont go above matrix
            if matrix[i-1][j] == 0:
                if OneMoreRound:
                    OneMoreRound = False
                else:
                    score += 1
                    return score / 2
            elif matrix[i-1][j] == '|' or matrix[i-1][j] == '7' or matrix[i-1][j] == 'F':
                nogoCounter = 0
                score += 1
                currentSegment = matrix[i-1][j]
                matrix[i-1][j] = score
                i = i - 1
            else:
                nogoCounter += 1
        #check east
        if j < len(matrix[0])-1 and (currentSegment == 'S' or currentSegment == '-' or currentSegment == 'L' or currentSegment == 'F'):
            if matrix[i][j+1] == 0:
                if OneMoreRound:
                    OneMoreRound = False
                else:
                    score += 1
                    return score / 2
            elif matrix[i][j+1] == '-' or matrix[i][j+1] == '7' or matrix[i][j+1] == 'J':
                nogoCounter = 0
                score += 1
                currentSegment = matrix[i][j+1]
                matrix[i][j+1] = score
                j = j + 1
            else:
                nogoCounter += 1
        #check south
        if i < len(matrix) and (currentSegment == 'S' or currentSegment == '|' or currentSegment == '7' or currentSegment == 'F'):
            if matrix[i+1][j] == 0: #we are back at start
                if OneMoreRound:
                    OneMoreRound = False
                else:
                    score += 1
                    return score / 2
            elif matrix[i+1][j] == '|' or matrix[i+1][j] == 'J' or matrix[i+1][j] == 'L':
                nogoCounter = 0
                score += 1
                currentSegment = matrix[i+1][j]
                matrix[i+1][j] = score
                i = i + 1
            else:
                nogoCounter += 1
        #check west
        if j > 0 and (currentSegment == 'S' or currentSegment == '-' or currentSegment == '7' or currentSegment == 'J'):
            if matrix[i][j-1] == 0: #we are back at start
                if OneMoreRound:
                    OneMoreRound = False
                else:
                    score += 1
                    return score / 2
            elif matrix[i][j-1] == '-' or matrix[i][j-1] == 'L' or matrix[i][j-1] == 'F':
                nogoCounter = 0
                score += 1
                currentSegment = matrix[i][j-1]
                matrix[i][j-1] = score
                j = j - 1
            else:
                nogoCounter += 1
        if nogoCounter > 10:
            for line in matrix:
                print(line)
            pass
        



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
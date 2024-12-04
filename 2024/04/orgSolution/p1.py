from time import time

def p1():
    matrix = []
    with open("2024/04/inputs/input.txt") as f:
        for line in f.readlines():
            matrix.append(list(line.strip()))
    score = 0
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            if matrix[i][j] == 'X':
                #check forward
                if j < (len(matrix[i]) - 3):
                    if matrix[i][j+1] == 'M':
                        if matrix[i][j+2] == 'A':
                            if matrix[i][j+3] == 'S':
                                score += 1
                #check reverse
                if j > 2:
                    if matrix[i][j-1] == 'M':
                        if matrix[i][j-2] == 'A':
                            if matrix[i][j-3] == 'S':
                                score += 1                
                #check up
                if i > 2:
                    if matrix[i-1][j] == 'M':
                        if matrix[i-2][j] == 'A':
                            if matrix[i-3][j] == 'S':
                                score += 1    
                #check down
                if i < (len(matrix) - 3):
                    if matrix[i+1][j] == 'M':
                        if matrix[i+2][j] == 'A':
                            if matrix[i+3][j] == 'S':
                                score += 1    
                #check diagonal NW
                if (j > 2) and (i > 2):
                    if matrix[i-1][j-1] == 'M':
                        if matrix[i-2][j-2] == 'A':
                            if matrix[i-3][j-3] == 'S':
                                score += 1
                #check diagonal NE
                if (j < (len(matrix[i]) - 3)) and (i > 2):
                    if matrix[i-1][j+1] == 'M':
                        if matrix[i-2][j+2] == 'A':
                            if matrix[i-3][j+3] == 'S':
                                score += 1   
                #check diagonal SW
                if (j > 2) and (i < (len(matrix) - 3)):
                    if matrix[i+1][j-1] == 'M':
                        if matrix[i+2][j-2] == 'A':
                            if matrix[i+3][j-3] == 'S':
                                score += 1
                #check diagonal SE
                if (j < (len(matrix[i]) - 3)) and (i < (len(matrix) - 3)):
                    if matrix[i+1][j+1] == 'M':
                        if matrix[i+2][j+2] == 'A':
                            if matrix[i+3][j+3] == 'S':
                                score += 1   
            j += 1
        i += 1

    return score

def p2():
    matrix = []
    with open("2024/04/inputs/input.txt") as f:
        for line in f.readlines():
            matrix.append(list(line.strip()))
    score = 0
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            if matrix[i][j] == 'A': 
                NWSE = False
                NESW = False
                #check diagonal NW-SE
                if (j > 0) and (i > 0) and (j < (len(matrix[i]) - 1)) and (i < (len(matrix) - 1)):
                    if matrix[i-1][j-1] == 'M':
                        if matrix[i+1][j+1] == 'S':
                            NWSE = True
                    elif matrix[i-1][j-1] == 'S':
                        if matrix[i+1][j+1] == 'M':
                            NWSE = True
                    
                    if matrix[i-1][j+1] == 'M':
                        if matrix[i+1][j-1] == 'S':
                            NESW = True
                    elif matrix[i-1][j+1] == 'S':
                        if matrix[i+1][j-1] == 'M':
                            NESW = True
                else:
                    j += 1
                    continue
                if NWSE and NESW:
                    score +=1
            j += 1
        i += 1

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
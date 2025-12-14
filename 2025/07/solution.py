from time import time

def p1(matrix = []):
    score = 0
    startingPos = 0
    for j in range(len(matrix[0])):
        if matrix[0][j] == 'S':
            startingPos = j
    matrix[1][startingPos] = '|'
    for i in range(2,len(matrix)):
        for j in range(0,len(matrix[i])):
            if matrix[i-1][j] == '|':
                if matrix[i][j] == '.':
                    matrix[i][j] = '|'
                elif matrix[i][j] == '^':
                    if j > 0:
                        matrix[i][j-1] = '|'
                    if j < (len(matrix[i])-1):
                        matrix[i][j+1] = '|'
                    score += 1
    return score

def p2(matrix = []):
    
    return 0

if __name__ == '__main__':
    stringmatrix = []
    with open("2025/07/input.txt") as f:
        stringmatrix = f.read().split(f"{f.newlines}")
    matrix = []
    for string in stringmatrix:
        charArray = []
        for char in string:
            charArray.append(char)
        matrix.append(charArray)
    start_time = int(round(time() * 1000))
    print('part 1:', p1(matrix.copy()))
    print("### p1 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    start_time = int(round(time() * 1000))
    print('part 2:', p2(matrix.copy()))
    print("### p2 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
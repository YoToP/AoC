from time import time

def p1(matrix = []):
    debugList = []
    def hasRoll(x,y) -> int:
        
        if x < 0:               #check above OOB(Out of Bounds)
            return 0
        if x >= len(matrix):    #check right OOB(Out of Bounds)
            return 0
        if y < 0:               #check left OOB(Out of Bounds)
            return 0
        if y >= len(matrix[0]): #check below OOB(Out of Bounds)
            return 0
        if matrix[x][y] == '@':
            return 1
        else:
            return 0
    score = 0
    maxI = len(matrix)
    maxJ = len(matrix[0])
    for i in range(0,maxI):
        for j in range(0,maxJ):
            amountAdjecentRolls = 0
            if matrix[i][j] == '@':
                #above
                amountAdjecentRolls += hasRoll(i-1,j-1)
                amountAdjecentRolls += hasRoll(i-1,j)
                amountAdjecentRolls += hasRoll(i-1,j+1)
                #in line
                amountAdjecentRolls += hasRoll(i,j-1)
                #amountAdjecentRolls += hasRoll(i,j)
                amountAdjecentRolls += hasRoll(i,j+1)
                #below
                amountAdjecentRolls += hasRoll(i+1,j-1)
                amountAdjecentRolls += hasRoll(i+1,j)
                amountAdjecentRolls += hasRoll(i+1,j+1)
                if amountAdjecentRolls < 4:
                    score += 1
                    debugList.append((i,j))
    return score

def p2(banks = []):
    score = 0

    return score

if __name__ == '__main__':
    matrix = []
    with open("2025/04/input.txt") as f:
        matrix = f.read().split(f"{f.newlines}")
    start_time = int(round(time() * 1000))
    print('part 1:', p1(matrix.copy()))
    print("### p1 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    start_time = int(round(time() * 1000))
    print('part 2:', p2(matrix.copy()))
    print("### p2 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
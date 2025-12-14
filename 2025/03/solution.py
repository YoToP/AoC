from time import time
from math import floor

def p1(banks = []):
    score = 0
    for i in range(0,len(banks)):
        high = 0
        highPos = 0
        for j in range(0,len(banks[i])-1):
            if int(banks[i][j]) > high:
                high = int(banks[i][j])
                highPos = j
            if high == 9:
                break
        low = 0
        for j in range(highPos+1,len(banks[i])):
            if int(banks[i][j]) > low:
                low = int(banks[i][j])
            if low == 9:
                break
        score += (high*10)+low

    return score

def p2(banks = []):
    score = 0
    
    return score

if __name__ == '__main__':
    banks = []
    with open("2025/03/input.txt") as f:
        banks = f.read().split(f"{f.newlines}")
    start_time = int(round(time() * 1000))
    print('part 1:', p1(banks.copy()))
    print("### p1 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    start_time = int(round(time() * 1000))
    print('part 2:', p2(banks.copy()))
    print("### p2 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
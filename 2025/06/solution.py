from time import time

def p1(lines = []):
    lastLinePos = len(lines)-1
    endPos = len(lines[0])
    startPos = endPos-1
    score = 0
    #find sign
    sign = ''
    while startPos >= 0:
        test = lines[lastLinePos][startPos]
        if lines[lastLinePos][startPos] == '+':
            sign = '+'
        elif lines[lastLinePos][startPos] == '*':
            sign = '*'
        else:
            startPos -= 1
            continue
        if sign == '+':
            partTotal = 0
        if sign == '*':
            partTotal = 1
        for i in range(len(lines)-1):
            if sign == '+':
                partTotal += int(lines[i][startPos:endPos])
            if sign == '*':
                partTotal *= int(lines[i][startPos:endPos])
        score += partTotal
        endPos = startPos-1
        startPos=endPos-1
    return score

def p2(lines = []):

    return 0

if __name__ == '__main__':
    with open("2025/06/input.txt") as f:
        lines = f.read().split(f"{f.newlines}")
    start_time = int(round(time() * 1000))
    print('part 1:', p1(lines))
    print("### p1 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    start_time = int(round(time() * 1000))
    print('part 2:', p2(lines))
    print("### p2 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
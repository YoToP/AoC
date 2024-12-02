from time import time

def isScore(_levels):
    allInc = True
    allDec = True
    safeChange = True
    last = int(_levels[0])
    for i in range(1,len(_levels)):
        current = int(_levels[i])
        delta = abs(current - last)
        if delta > 3:
            safeChange = False
        if current > last:
            allDec = False
        elif current < last:
            allInc = False
        elif current == last:
            allDec = False
            allInc = False
        last = current
    if (allInc or allDec) and safeChange:
        return True
    return False

def p1():
    with open("2024/02/inputs/input.txt") as f:
        score = 0
        for line in f.readlines():
            if isScore(line.strip().split(" ")):
                score += 1
    return score

def p2():
    with open("2024/02/inputs/input.txt") as f:
        score = 0
        for line in f.readlines():
            levels = line.strip().split(" ")
            lineSafe = isScore(levels) # check whole line
            if not lineSafe: # if whole line is not good, check every line with one removed
                for i in range(0, len(levels)):
                    subLevels = levels.copy()
                    subLevels.pop(i)
                    if isScore(subLevels):
                        lineSafe = True
                        break
            if lineSafe:
                score += 1
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
from time import time
def p1():
    TimeDist= []
    TimeDist.append((61,430))
    TimeDist.append((67,1036))
    TimeDist.append((75,1307))
    TimeDist.append((71,1150))
    game = 0

    winList = []
    while game < len(TimeDist):
        possibleWins = 0
        for speed in range (1,TimeDist[game][0]):
            possibleDist = (TimeDist[game][0] -speed) *speed
            if possibleDist > TimeDist[game][1]:
                possibleWins += 1
        game += 1
        winList.append(possibleWins)

    score = 1
    for win in winList:
        score *= win
    return score


def p2(): 
    TimeDist = (61677571,430103613071150)
    game = 0

    winStart = 0
    winEnd = 0
    for speed in range (1,TimeDist[0]):
        possibleDist = (TimeDist[0] -speed) *speed
        if possibleDist > TimeDist[1]:
            winStart = speed
            break
    for i in range (1,TimeDist[0]):
        speed = TimeDist[0] - i
        possibleDist = (TimeDist[0] -speed) *speed
        if possibleDist > TimeDist[1]:
            winEnd = speed
            break

    return winEnd-winStart+1

if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', p1())
    print("### p1 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    start_time = int(round(time() * 1000))
    print('part 2:', p2())
    print("### p2 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
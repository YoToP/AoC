from time import time
''' 
In part 2 I created function calcNextKnot.
This code has been refactored to use this function in part 1 as well.
also fixing some commenting mistakes.
'''

def calcNextKnot(head, tail):
    newTailX = tail[0]
    newTailY = tail[1]
    if head[0]-tail[0] == 2 and head[1]-tail[1] == 2:  # UP/R diagonal check
        newTailX += 1
        newTailY += 1
    elif head[0]-tail[0] == -2 and head[1]-tail[1] == 2:  # UP/L diagonal check
        newTailX -= 1
        newTailY += 1
    elif head[0]-tail[0] == 2 and head[1]-tail[1] == -2:  # DOWN/R diagonal check
        newTailX += 1
        newTailY -= 1
    elif head[0]-tail[0] == -2 and head[1]-tail[1] == -2:  # DOWN/L diagonal check
        newTailX -= 1
        newTailY -= 1
    elif head[1]-tail[1] > 1 and abs(head[0]-tail[0]) == 1:  # UP L check
        newTailX = head[0]
        newTailY += 1
    elif head[1]-tail[1] < -1 and abs(head[0]-tail[0]) == 1:  # DOWN L check
        newTailX = head[0]
        newTailY -= 1
    elif (head[1] != tail[1]) and head[0]-tail[0] > 1:  # Right L check
        newTailX += 1
        newTailY = head[1]
    elif (head[1] != tail[1]) and head[0]-tail[0] < -1:  # Left L check
        newTailX -= 1
        newTailY = head[1]
    elif head[0]-tail[0] == 2:  # moved 1 up
        newTailX += 1
    elif head[0]-tail[0] == -2:  # moved 1 down
        newTailX -= 1
    elif head[1]-tail[1] == 2:  # moved 1 right
        newTailY += 1
    elif head[1]-tail[1] == -2:  # moved 1 left
        newTailY -= 1
    return (newTailX, newTailY)


def part1(path):
    with open(path) as f:
        lines = f.readlines()
    posHeadX = 0  # LEFT/RIGHT
    posHeadY = 0  # UP/DOWN
    posTailX = 0
    posTailY = 0
    tailVisited = set()
    for line in lines:
        direction, steps = line.strip().split(" ")
        for _ in range(0, int(steps)):
            if direction == 'U':
                posHeadY += 1
            elif direction == 'D':
                posHeadY -= 1
            elif direction == 'R':
                posHeadX += 1
            elif direction == 'L':
                posHeadX -= 1
            posTailX, posTailY = calcNextKnot(
                (posHeadX, posHeadY), (posTailX, posTailY))
            tailVisited.add((posTailX, posTailY))
    return len(tailVisited)


def part2(path):
    with open(path) as f:
        lines = f.readlines()
    posHeadX = 0  # LEFT/RIGHT
    posHeadY = 0  # UP/DOWN
    lstKnots = []
    for _ in range(0, 9):
        lstKnots.append((0, 0))
    tailVisited = set()

    for line in lines:
        direction, steps = line.strip().split(" ")
        for _ in range(0, int(steps)):
            if direction == 'U':
                posHeadY += 1
            elif direction == 'D':
                posHeadY -= 1
            elif direction == 'R':
                posHeadX += 1
            elif direction == 'L':
                posHeadX -= 1
            lstKnots[0] = calcNextKnot((posHeadX, posHeadY), lstKnots[0])

            for i in range(1, len(lstKnots)):
                lstKnots[i] = calcNextKnot(lstKnots[i-1], lstKnots[i])
            tailVisited.add((lstKnots[8][0], lstKnots[8][1]))

    return len(tailVisited)


if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', part1("2022/09/inputs/input.txt"))
    print('part 2:', part2("2022/09/inputs/input.txt"))
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))

from time import time
directions = { #new stuff
    'U': (-1,  0),
    'D': (+1,  0),
    'L': (0, -1),
    'R': (0, +1),
}

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
    return [newTailX, newTailY]


def ParseInstruction(line):
    direction, distance = line.split()
    return (direction, int(distance))


def part2(path):
    with open(path) as f:
        instructions = list(map(ParseInstruction, f.readlines())) #new stuff
    lstRope = [[0,0] for _ in range(0,10)]#new stuff
    tailVisited0 = set()
    tailVisited8 = set()

    for direction, steps in instructions:
        _y, _x = directions[direction]
        for _ in range(0, int(steps)):
            lstRope[0][0] += _x
            lstRope[0][1] += _y

            for i in range(1, len(lstRope)):
                if abs(lstRope[i-1][0] - lstRope[i][0]) >1 or abs(lstRope[i-1][1] - lstRope[i][1]) >1:
                    lstRope[i] = calcNextKnot(lstRope[i-1], lstRope[i])
                else:
                    break
            tailVisited0.add((lstRope[1][0],lstRope[1][1]))
            tailVisited8.add((lstRope[9][0],lstRope[9][1]))

    return (len(tailVisited0), len(tailVisited8))


if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1/2:', part2("2022/09/inputs/input.txt"))
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))

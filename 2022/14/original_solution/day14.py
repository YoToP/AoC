from time import time
from collections import defaultdict
''' 
day14
'''

def part1(path):
    with open(path) as f:
        lines = f.readlines()
    #Create matrix
    # 0 = empty
    # 1 = blocked
    matrix = defaultdict(int)
    abyssStart = 0
    for line in lines:
        rockCorners = line.strip().split(' -> ')
        i = 0
        while i < len(rockCorners)-1:
            x1,y1 = rockCorners[i].split(',')
            x2,y2 = rockCorners[i+1].split(',')
            x1 = int(x1)
            y1 = int(y1)
            x2 = int(x2)
            y2 = int(y2)
            #check Start of Abyss
            if y1 > abyssStart:
                abyssStart = y1
            if y2 > abyssStart:
                abyssStart = y2

            if x1 == x2: #hor same, vertical formation
                if y1 < y2:
                    for y in range(y1,y2+1):
                        matrix[(x1,y)] = 1
                else:
                    for y in range(y2,y1+1):
                        matrix[(x1,y)] = 1
            else: #ver same, horizontal formation
                if x1 < x2:
                    for x in range(x1,x2+1):
                        matrix[(x,y1)] = 1
                else:
                    for x in range(x2,x1+1):
                        matrix[(x,y1)] = 1
            i += 1
    #Playing field loaded
    #start playing the game
    activeSand = (500,0)
    restCounter = 0
    while activeSand[1]< abyssStart:
        #try to move down
        if matrix[(activeSand[0],activeSand[1]+1)] == 1: #cannot move down,
            #check if can move to left/down
            if matrix[(activeSand[0]-1,activeSand[1]+1)] == 1: #cannot move left/down,
                #check if can move right/down
                if matrix[(activeSand[0]+1,activeSand[1]+1)] == 1: #cannot move right/down
                    #sand cannot move, so will set at current position
                    matrix[activeSand] = 1
                    restCounter += 1
                    activeSand = (500,0) # spawn new sand
                else: # can move to right/down
                    activeSand = (activeSand[0]+1,activeSand[1]+1)
            else: # can move to left/down
                activeSand = (activeSand[0]-1,activeSand[1]+1)
        else: # can move down
            activeSand = (activeSand[0],activeSand[1]+1)
    return restCounter


def part2(path):
    with open(path) as f:
        lines = f.readlines()
    #Create matrix
    # 0 = empty
    # 1 = blocked
    matrix = defaultdict(int)
    abyssStart = 0
    for line in lines:
        rockCorners = line.strip().split(' -> ')
        i = 0
        while i < len(rockCorners)-1:
            x1,y1 = rockCorners[i].split(',')
            x2,y2 = rockCorners[i+1].split(',')
            x1 = int(x1)
            y1 = int(y1)
            x2 = int(x2)
            y2 = int(y2)
            #check Start of Abyss
            if y1 > abyssStart:
                abyssStart = y1
            if y2 > abyssStart:
                abyssStart = y2

            if x1 == x2: #hor same, vertical formation
                if y1 < y2:
                    for y in range(y1,y2+1):
                        matrix[(x1,y)] = 1
                else:
                    for y in range(y2,y1+1):
                        matrix[(x1,y)] = 1
            else: #ver same, horizontal formation
                if x1 < x2:
                    for x in range(x1,x2+1):
                        matrix[(x,y1)] = 1
                else:
                    for x in range(x2,x1+1):
                        matrix[(x,y1)] = 1
            i += 1
    #Playing field loaded
    #start playing the game
    activeSand = (500,0)
    restCounter = 0
    gameOver = False
    while not gameOver:
        #try to move down
        if matrix[(activeSand[0],activeSand[1]+1)] == 1 or activeSand[1] == abyssStart+1: #cannot move down,
            #check if can move to left/down
            if matrix[(activeSand[0]-1,activeSand[1]+1)] == 1 or activeSand[1] == abyssStart+1: #cannot move left/down,
                #check if can move right/down
                if matrix[(activeSand[0]+1,activeSand[1]+1)] == 1 or activeSand[1] == abyssStart+1: #cannot move right/down
                    if activeSand[0] == 500 and activeSand[1] == 0:
                        gameOver = True
                        restCounter += 1
                    else:
                        #sand cannot move, so will set at current position
                        matrix[activeSand] = 1
                        restCounter += 1
                        activeSand = (500,0) # spawn new sand
                else: # can move to right/down
                    activeSand = (activeSand[0]+1,activeSand[1]+1)
            else: # can move to left/down
                activeSand = (activeSand[0]-1,activeSand[1]+1)
        else: # can move down
            activeSand = (activeSand[0],activeSand[1]+1)
    return restCounter


if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', part1("2022/14/inputs/input.txt"))
    print('part 2:', part2("2022/14/inputs/input.txt"))
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))

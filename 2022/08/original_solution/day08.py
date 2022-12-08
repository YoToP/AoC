from time import time

def part1(path,maxX,maxY):
    with open(path) as f:
        data = f.readlines()
    totalVisible = 0
    for x in range(0,maxX):
        for y in range(0,maxY):
            if 0 < x < (maxX-1) and 0 < y < (maxY-1):
                tree = int(data[x][y])
                highestFromTop = False
                highestFromBottom = False
                highestFromLeft = False
                highestFromRight = False
                if tree >= int(data[x-1][y]):
                    highestFromTop = True
                    for i in range(0,x):
                        furtherTree = int(data[i][y])
                        if furtherTree >= tree:
                            highestFromTop = False
                if tree >= int(data[x][y-1]):
                    highestFromLeft = True
                    for j in range(0,y):
                        furtherTree = int(data[x][j])
                        if furtherTree >= tree:
                            highestFromLeft = False
                if tree >= int(data[x+1][y]):
                    highestFromBottom = True
                    for i in range(x+1,maxX):
                        furtherTree = int(data[i][y])
                        if furtherTree >= tree:
                            highestFromBottom = False
                if tree >= int(data[x][y+1]):
                    highestFromRight = True
                    for j in range(y+1,maxY):
                        furtherTree = int(data[x][j])
                        if furtherTree >= tree:
                            highestFromRight = False
                if highestFromTop or highestFromBottom or highestFromLeft or highestFromRight:
                    totalVisible += 1
            else:
                totalVisible += 1
    return totalVisible

def part2(path,maxX,maxY):
    with open(path) as f:
        data = f.readlines()
    Highscore = 0
    for x in range(0,maxX):
        for y in range(0,maxY):
            if  x < (maxX) and  y < (maxY):
                if x ==3 and y==2:
                    pass
                tree = int(data[x][y])
                distToTop = 0
                distToBottom = 0
                distToLeft = 0
                distToRight = 0
                if x > 0:
                    if tree >= int(data[x-1][y]):
                        i = x
                        while i > 0:
                            i -= 1
                            furtherTree = int(data[i][y])
                            distToTop +=1
                            if furtherTree >= tree:
                                break
                if y > 0:
                    if tree >= int(data[x][y-1]):
                        j = y
                        while j > 0:
                            j -= 1
                            furtherTree = int(data[x][j])
                            distToLeft +=1
                            if furtherTree >= tree:
                                break
                if x < maxX-1:
                    if tree >= int(data[x+1][y]):
                        i = x
                        while i < maxX-1:
                            i += 1
                            furtherTree = int(data[i][y])
                            distToBottom +=1
                            if furtherTree >= tree:
                                break
                if y < maxY-1:
                    if tree >= int(data[x][y+1]):
                        j = y
                        while j < maxY-1:
                            j += 1
                            furtherTree = int(data[x][j])
                            distToRight +=1
                            if furtherTree >= tree:
                                break
                score = distToTop * distToBottom * distToLeft * distToRight
                if score > Highscore:
                    Highscore = score
    return Highscore

if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', part1("2022/08/inputs/input.txt",99,99))
    #print('example part 1:', part1("2022/08/inputs/example.txt",5,5))
    print('part 2:', part2("2022/08/inputs/input.txt",99,99))
    #print('example part 2:', part2("2022/08/inputs/example.txt",5,5))
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
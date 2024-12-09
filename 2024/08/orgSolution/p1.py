from time import time
from collections import defaultdict

def p1():
    antinodeDict = defaultdict(int)
    pairDict = defaultdict(list)
    maxI = 0
    maxJ = 0
    with open("2024/08/inputs/input.txt") as f:
        i = 0
        for line in f.read().split('\n'):
            j = 0
            while j < len(line):
                char = line[j]
                if char != '.':
                    pairDict[char].append((i,j))
                j += 1
                maxJ = j
            i += 1
            maxI = i

    for k in pairDict:
        i = 0
        while i < len(pairDict[k])-1:
            copyList = pairDict[k][i:len(pairDict[k])]
            p1 = copyList.pop(0) 
            while len(copyList) > 0:
                p2 = copyList.pop(0)

                deltaI = p1[0] - p2[0]
                deltaJ = p1[1] - p2[1]

                targetI = p1[0]+deltaI
                targetJ = p1[1]+deltaJ
                if targetI >= 0 and targetI <= maxI and targetJ >= 0 and targetJ <= maxJ:
                    antinodeDict[(targetI,targetJ)] += 1
                
                targetI = p2[0]-deltaI
                targetJ = p2[1]-deltaJ
                if targetI >= 0 and targetI <= maxI and targetJ >= 0 and targetJ <= maxJ:
                    antinodeDict[(targetI,targetJ)] += 1
            i += 1
    return len(antinodeDict)

def p2():
    antinodeDict = defaultdict(int)
    pairDict = defaultdict(list)
    maxI = 0
    maxJ = 0
    with open("2024/08/inputs/example.txt") as f:
        i = 0
        for line in f.readlines():
            line = line.strip()
            j = 0
            while j < len(line):
                char = line[j]
                if char != '.':
                    pairDict[char].append((i,j))
                j += 1
                maxJ = j
            i += 1
            maxI = i
    pass
    for k in pairDict:
        i = 0
        while i < len(pairDict[k])-1:
            copyList = pairDict[k][i:len(pairDict[k])]
            p1 = copyList.pop(0) 
            while len(copyList) > 0:
                p2 = copyList.pop(0)

                deltaI = p1[0] - p2[0]
                deltaJ = p1[1] - p2[1]

                targetI = p1[0]+deltaI
                targetJ = p1[1]+deltaJ
                if targetI >= 0 and targetI <= maxI and targetJ >= 0 and targetJ <= maxI:
                    antinodeDict[(targetI,targetJ)] += 1
                
                targetI = p2[0]-deltaI
                targetJ = p2[1]-deltaJ
                if targetI >= 0 and targetI <= maxI and targetJ >= 0 and targetJ <= maxI:
                    antinodeDict[(targetI,targetJ)] += 1
            i += 1
    score = 0
    for k in antinodeDict.keys():
        score += antinodeDict[k]
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
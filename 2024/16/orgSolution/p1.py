from time import time
import sys
sys.setrecursionlimit(10**6)
matrix = []
scoreList = []
shortesVisitList = dict()
P2lowestScore = 1000000000
P2PositionList = set()

def findCrossPointOrEnd(visitedCrossroads: list, currentPosition:set,direction:str,score:int,visitedPlaces: list):
    if currentPosition in shortesVisitList.keys(): #If we arrive at a crossroad that another route has found in lower score, then skip this branch
        if score > shortesVisitList[currentPosition]:
            return
    global P2lowestScore, P2PositionList
    if score > P2lowestScore:
        return
    _score = 0
    _currentPosition = currentPosition
    nextI = _currentPosition[0]
    nextJ = _currentPosition[1]
    atCrossroad = False
    while not atCrossroad: #follow route until blocked or end has been found
        availableRoutes = [] #Every step check if we are at a crossroad/turn and add them in list
        if direction == '>':
            nextJ += 1
            if matrix[nextI-1][nextJ] == '.': #check UP for empty spot '.'
                atCrossroad = True
                availableRoutes.append('^')
            if matrix[nextI+1][nextJ] == '.': #check down for empty spot '.'
                atCrossroad = True
                availableRoutes.append('v')
            if matrix[nextI][nextJ+1] == '#': #check in same direction if blocked
                if not atCrossroad:
                    return #deadend
            elif matrix[nextI][nextJ+1] == 'E': #check in same direction if END
                _score += 1
                scoreList.append(score+_score)
                visitedPlaces.append((nextI,nextJ)) # this one
                visitedPlaces.append((nextI,nextJ+1)) # and next
                if (score+_score) < P2lowestScore:
                    P2lowestScore = score+_score
                    P2PositionList.clear()
                    [P2PositionList.add(e) for e in visitedPlaces]
                elif (score+_score) == P2lowestScore:
                    [P2PositionList.add(e) for e in visitedPlaces]
                #print(f"{score+_score}: {visitPlaces}")
                return #Found the end, stop branch
            else:
                if atCrossroad:
                    availableRoutes.append('>')
            _score += 1
            _currentPosition = (nextI,nextJ)
            visitedPlaces.append(_currentPosition)
        elif direction == 'v':
            nextI += 1
            #check LEFT for empty spot '.'
            if matrix[nextI][nextJ-1] == '.':
                atCrossroad = True
                availableRoutes.append('<')
            #check RIGHT for empty spot '.'
            if matrix[nextI][nextJ+1] == '.':
                atCrossroad = True
                availableRoutes.append('>')
            #check in same direction  for free spot
            if matrix[nextI+1][nextJ] == '#':
                if not atCrossroad:
                    return #deadend
            elif matrix[nextI+1][nextJ] == 'E':
                _score += 1
                scoreList.append(score+_score)
                visitedPlaces.append((nextI,nextJ)) # this one
                visitedPlaces.append((nextI+1,nextJ)) # and next
                if (score+_score) < P2lowestScore:
                    P2lowestScore = score+_score
                    P2PositionList.clear()
                    [P2PositionList.add(e) for e in visitedPlaces]
                elif (score+_score) == P2lowestScore:
                    [P2PositionList.add(e) for e in visitedPlaces]
                #print(f"{score+_score}: {visitPlaces}")
                return #Found the end, stop routine
            else:
                #_score += 1
                if atCrossroad:
                    availableRoutes.append('v')
            _score += 1
            _currentPosition = (nextI,nextJ)
            visitedPlaces.append(_currentPosition)
        elif direction == '<':
            nextJ -= 1
            #check UP for empty spot '.'
            if matrix[nextI-1][nextJ] == '.':
                atCrossroad = True
                availableRoutes.append('^')
            #check down for empty spot '.'
            if matrix[nextI+1][nextJ] == '.':
                atCrossroad = True
                availableRoutes.append('v')
            #check in same direction  for free spot
            if matrix[nextI][nextJ-1] == '#':
                if not atCrossroad:
                    return #deadend
            elif matrix[nextI][nextJ-1] == 'E':
                _score += 1
                visitedPlaces.append((nextI,nextJ)) # this one
                visitedPlaces.append((nextI,nextJ-1)) # and next
                scoreList.append(score+_score)
                if (score+_score) < P2lowestScore:
                    P2lowestScore = score+_score
                    P2PositionList.clear()
                    [P2PositionList.add(e) for e in visitedPlaces]
                elif (score+_score) == P2lowestScore:
                    [P2PositionList.add(e) for e in visitedPlaces]
                #print(f"{score+_score}: {visitPlaces}")
                return #Found the end, stop routine
            else:
                #_score += 1
                if atCrossroad:
                    availableRoutes.append('<')
            _score += 1
            _currentPosition = (nextI,nextJ)
            visitedPlaces.append(_currentPosition)
        elif direction == '^':
            nextI -= 1
            #check LEFT for empty spot '.'
            if matrix[nextI][nextJ-1] == '.':
                atCrossroad = True
                availableRoutes.append('<')
            #check RIGHT for empty spot '.'
            if matrix[nextI][nextJ+1] == '.':
                atCrossroad = True
                availableRoutes.append('>')
            #check in same direction  for free spot
            if matrix[nextI-1][nextJ] == '#':
                if not atCrossroad:
                    return #deadend
            elif matrix[nextI-1][nextJ] == 'E':
                _score += 1
                scoreList.append(score+_score)
                visitedPlaces.append((nextI,nextJ)) # this one
                visitedPlaces.append((nextI-1,nextJ)) # and next
                if (score+_score) < P2lowestScore:
                    P2lowestScore = score+_score
                    P2PositionList.clear()
                    [P2PositionList.add(e) for e in visitedPlaces]
                elif (score+_score) == P2lowestScore:
                    [P2PositionList.add(e) for e in visitedPlaces]
                #print(f"{score+_score}: {visitPlaces}")
                return #Found the end, stop routine
            else:
                #_score += 1
                if atCrossroad:
                    availableRoutes.append('^')
            _score += 1
            _currentPosition = (nextI,nextJ)
            visitedPlaces.append(_currentPosition)
    if _currentPosition in visitedCrossroads:
        return #we have arrived at a crossroad, we already visited
    #shortesVisitList[currentPosition] = score #add starting Cross now, because now we know that its on the path
    visitedCrossroads.append(_currentPosition)
    for route in availableRoutes:
        _interScore = _score + score
        if direction != route:
            _interScore += 1000
        if currentPosition == (8,0):
            pass
        findCrossPointOrEnd(visitedCrossroads.copy(),_currentPosition,route,_interScore,visitedPlaces.copy())
    return

def p1():
    startPos = (0,0)
    with open("2024/16/inputs/input.txt") as f:
        i = 0
        for line in f.read().split('\n'):
            if 'S' in line:
                startPos = (i,line.find('S')-1)
            matrix.append(list(line))
            i += 1
    _list = []
    findCrossPointOrEnd(_list,startPos,'>',0,[])

    minWaarde = min(scoreList)
    amount = 0
    for w in scoreList:
        if w == minWaarde:
            amount += 1
    print(f"Amount of fastest routes: {amount}")
    return (min(scoreList), len(P2PositionList))

def p2():

    return 0

if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    answer1,answer2 = p1()
    print(f'part 1: {answer1}, part 2: {answer2}')
    print("### p1&2 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    for i,j in P2PositionList:
        matrix[i][j] = 'O'
    for i in range(0,len(matrix)):  #█
        s = ''
        for j in range(0,len(matrix[0])):
            if matrix[i][j] == '#':
                s += '█'
            else:
                s += matrix[i][j]
        print(s)
            
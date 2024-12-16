from time import time
import sys
sys.setrecursionlimit(10**6)
matrix = []
scoreList = []
debugScoreList = []
shortesVisitList = dict()
def findCrossPointOrEnd(visitPlaces: list, currentPosition:set,direction:str,score:int):
    #follow route until blocked or end has been found
    _score = 0
    _currentPosition = currentPosition
    atCrossroad = False
    nextI = _currentPosition[0]
    nextJ = _currentPosition[1]
    if _currentPosition == (7,3):
        debugScoreList.append(score)
        pass
    if _currentPosition == (7,11):
        debugScoreList.append(score)
        pass
    while not atCrossroad:
        availableRoutes = []
        if direction == '>':
            nextJ += 1
            #check UP for empty spot '.'
            if matrix[nextI-1][nextJ] == '.':
                atCrossroad = True
                availableRoutes.append('^')
            #check down for empty spot '.'
            if matrix[nextI+1][nextJ] == '.':
                atCrossroad = True
                availableRoutes.append('v')
            #check in same direction  for free spot
            if matrix[nextI][nextJ+1] == '#':
                if not atCrossroad:
                    return #deadend
            elif matrix[nextI][nextJ+1] == 'E':
                _score += 1
                _intScore = score+_score
                if len(scoreList) == 0:
                    scoreList.append(_intScore)
                if _intScore <  min(scoreList):
                    scoreList.append(_intScore)
                    #print(f"{_intScore}: {visitPlaces}")
                return #Found the end, stop routine
            else:
                #_score += 1
                if atCrossroad:
                    availableRoutes.append('>')
            _score += 1
            _currentPosition = (nextI,nextJ)
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
                _intScore = score+_score
                if len(scoreList) == 0:
                    scoreList.append(_intScore)
                if _intScore <  min(scoreList):
                    scoreList.append(_intScore)
                    #print(f"{_intScore}: {visitPlaces}")
                return #Found the end, stop routine
            else:
                #_score += 1
                if atCrossroad:
                    availableRoutes.append('v')
            _score += 1
            _currentPosition = (nextI,nextJ)
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
                _intScore = score+_score
                if len(scoreList) == 0:
                    scoreList.append(_intScore)
                if _intScore <  min(scoreList):
                    scoreList.append(_intScore)
                return #Found the end, stop routine
            else:
                #_score += 1
                if atCrossroad:
                    availableRoutes.append('<')
            _score += 1
            _currentPosition = (nextI,nextJ)
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
                _intScore = score+_score
                if len(scoreList) == 0:
                    scoreList.append(_intScore)
                if _intScore <  min(scoreList):
                    scoreList.append(_intScore)
                return #Found the end, stop routine
            else:
                #_score += 1
                if atCrossroad:
                    availableRoutes.append('^')
            _score += 1
            _currentPosition = (nextI,nextJ)
    if _currentPosition in shortesVisitList.keys():
        _interScore = _score + score
        if _interScore > shortesVisitList[_currentPosition]:
            return
    if _currentPosition in visitPlaces:
        return #we have arrived at a crossroad, we already visited
    visitPlaces.append(_currentPosition)
    shortesVisitList[_currentPosition] = _score + score
    for route in availableRoutes:
        _interScore = _score + score
        if direction != route:
            _interScore += 1000
        findCrossPointOrEnd(visitPlaces.copy(),_currentPosition,route,_interScore)

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
    findCrossPointOrEnd(_list,startPos,'>',0)



    return min(scoreList)

def p2():

    return 0

if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', p1())
    print("### p1 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    start_time = int(round(time() * 1000))
    print('part 2:', p2())
    print("### p2 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
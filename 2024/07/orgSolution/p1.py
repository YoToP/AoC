from time import time

def calcAllPosibillities(_target:int,_currentTotal:int, _numbersLeft:list):
    if len(_numbersLeft) == 1:
        if _currentTotal + _numbersLeft[0] == _target:
            return _target
        elif _currentTotal * _numbersLeft[0] == _target:
            return _target
        else:
            return 0
    else:
        _number = _numbersLeft.pop(0)
        _plus = calcAllPosibillities(_target,_currentTotal+_number,_numbersLeft.copy())
        if _plus > 0:
            return _plus
        _mul = calcAllPosibillities(_target,_currentTotal*_number,_numbersLeft.copy())
        if _mul > 0:
            return _mul
        else:
            return 0



def p1():
    score = 0
    with open("2024/07/inputs/example.txt") as f:
        for line in f.read().split('\n'):
            testValue, remainingNumbers = line.split(": ")
            score += calcAllPosibillities(int(testValue),0,[int(s) for s in remainingNumbers.split(" ")])
    return score


def calcAllPosibillitiesP2(_target:int,_currentTotal:int, _numbersLeft:list):
    if len(_numbersLeft) == 1:
        if int(str(_currentTotal)+str(_numbersLeft[0])) == _target:
            return _target
        if _currentTotal + _numbersLeft[0] == _target:
            return _target
        elif _currentTotal * _numbersLeft[0] == _target:
            return _target
        else:
            return 0
    else:
        _number = _numbersLeft.pop(0)
        _and = calcAllPosibillitiesP2(_target,int(str(_currentTotal)+str(_number)),_numbersLeft.copy())
        if _and > 0:
            return _and
        _plus = calcAllPosibillitiesP2(_target,_currentTotal+_number,_numbersLeft.copy())
        if _plus > 0:
            return _plus
        _mul = calcAllPosibillitiesP2(_target,_currentTotal*_number,_numbersLeft.copy())
        if _mul > 0:
            return _mul
        else:
            return 0

def p2():
    score = 0
    with open("2024/07/inputs/input.txt") as f:
        for line in f.read().split('\n'):
            testValue, remainingNumbers = line.split(": ")
            remainingNumbers = [int(s) for s in remainingNumbers.split(" ")]
            firstValue = remainingNumbers.pop(0)
            score += calcAllPosibillitiesP2(int(testValue),firstValue,remainingNumbers)
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
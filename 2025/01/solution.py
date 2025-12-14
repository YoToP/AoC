from time import time
from math import floor

def p1(steps = []):
    dial = 50
    amountZero = 0
    for step in steps:
        if step[0] == 'L':
            dial -= int(step.replace('L',''))
        elif step[0] == 'R':
            dial += int(step.replace('R',''))
        if dial < 0:
            while dial < 0:
                dial += 100
        elif dial > 99:
            while dial > 99:
                dial -= 100
        if dial == 0:
            amountZero += 1
    return amountZero

def p2(steps = []):
    dial = 50
    amountZero = 0
    startAtZero = False
    for step in steps:
        if dial == 0:
            startAtZero = True
        else:
            startAtZero = False
        if step[0] == 'L':
            dial -= int(step.replace('L',''))
        elif step[0] == 'R':
            dial += int(step.replace('R',''))
        if dial < 0:
            while dial < 0:
                dial += 100
                if not startAtZero:
                    amountZero += 1
                else:
                    startAtZero = False
        elif dial > 99:
            while dial > 99:
                dial -= 100
                if not startAtZero:
                    amountZero += 1
                else:
                    startAtZero = False
        elif dial == 0:
            amountZero += 1
    return amountZero

if __name__ == '__main__':
    steps = []
    with open("2025/01/input.txt") as f:
        steps = f.read().split(f"{f.newlines}")
    start_time = int(round(time() * 1000))
    print('part 1:', p1(steps.copy()))
    print("### p1 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    start_time = int(round(time() * 1000))
    print('part 2:', p2(steps.copy()))
    print("### p2 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
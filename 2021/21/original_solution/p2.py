from time import time
from collections import defaultdict

class gameState:
    def __init__(self,p1, p2): #constructor
        p1Score = p1
        p2Score = p2
        p1Wins = 0
        p2Wins = 0

    def CalcNextState():
        if p1Score >= 21:
            p1Wins = 1
        elif p2Score >= 21:
            p2Wins = 1
        else:
            p1Wins = 1

def correctPos(pos):
    if pos > 10:
        returnvalue = pos % 10
        if returnvalue == 0 :
            return 10
        else:
            return returnvalue
    else:
        return pos

def getDiceValue():
    global diceValue
    if diceValue > 3:
        diceValue = 1
    returnValue = diceValue
    diceValue += 1
    global diceThrowCount
    diceThrowCount += 1
    return returnValue

def solvep2(p1,p2):
    lstScoreList = defaultdict(int) # the int is the shortest path
    lstScoreList[0] = 0
    #setup board
    p1Pos = p1
    p2Pos = p2
    
    #setup dice
    global diceValue
    diceValue = 1
    global diceThrowCount
    diceThrowCount = 0
    
    #setup player scores
    p1Score = 0
    p2Score = 0
    while True:
        #player 1
        p1Pos += getDiceValue()
        p1Pos += getDiceValue()
        p1Pos += getDiceValue()
        p1Pos = correctPos(p1Pos)

        p1Score += p1Pos
        if p1Score >= 1000:
            print("P1 Won. DC: ",diceThrowCount," p1s: ", p1Score,"p2s: ", p2Score)
            endScore = p2Score * diceThrowCount
            break
        #player 2
        p2Pos += getDiceValue()
        p2Pos += getDiceValue()
        p2Pos += getDiceValue()
        p2Pos = correctPos(p2Pos)

        p2Score += p2Pos

        if p2Score >= 1000:
            print("P2 Won. DC: ",diceThrowCount," p1s: ", p1Score,"p2s: ", p2Score)
            endScore = p1Score * diceThrowCount
            break
    return endScore

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print('p2:',solvep2(8,10))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))
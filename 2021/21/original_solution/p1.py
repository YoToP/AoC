from time import time

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
    if diceValue > 100:
        diceValue = 1
    returnValue = diceValue
    diceValue += 1
    global diceThrowCount
    diceThrowCount += 1
    return returnValue

def solvep1(p1,p2):
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
        if diceValue == 97:
            pass
        #player 1
        p1Pos += getDiceValue()
        p1Pos += getDiceValue()
        p1Pos += getDiceValue()
        p1Pos = correctPos(p1Pos)

        p1Score += p1Pos
        if diceValue == 100:
            pass
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
        if diceThrowCount == 993:
            pass
    return endScore

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print('p1:',solvep1(8,10))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))
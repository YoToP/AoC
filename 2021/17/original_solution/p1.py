from time import time
    
def solvep1(x: tuple=(0,0),y:tuple=(0,0)):
    print("Target: x:",x[0],x[1],"y:",y[0],y[1])
    Highscore = 0
    for i in range(1,x[1]):
        for j in range(1,1000):
            xVel = i
            yVel = j
            Highest = 0
            xPos = 0
            yPos = 0
            inZone = False
            while xPos <= x[1] and yPos >= y[0]:
                xPos += xVel
                yPos += yVel
                if xVel > 0:
                    xVel -= 1
                yVel -= 1
                if yPos > Highest:
                    Highest = yPos
                if (x[0] <= xPos <= x[1]) and (y[0] <= yPos <= y[1]):
                    inZone = True
            if inZone:
                if Highest > Highscore:
                    Highscore = Highest
    return Highscore

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print('p1:',solvep1((14,50),(-267,-225)))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))
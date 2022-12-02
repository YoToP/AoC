from time import time
from collections import defaultdict

def solvep1(path):
    lstCubesSpace = defaultdict(bool) # the bool represents ON or OFF
    
    with open(path) as f: lines = f.readlines()
    for line in lines:
        strippedLine = line.strip()
        strOn, strCubeData = strippedLine.split(" ")
        strX, strY, strZ = strCubeData.split(",")
        StrxMin,StrxMax = strX.split("=")[1].split("..")
        StryMin,StryMax = strY.split("=")[1].split("..")
        StrzMin,StrzMax = strZ.split("=")[1].split("..")
        if strOn == "on":
            bOn = True
        else:
            bOn = False
        #-----X-----
        xMin = int(StrxMin)
        xMax = int(StrxMax)
        if xMin > xMax:
            temp = xMin
            xMin = xMax
            xMax = temp
        #-----Y-----
        yMin = int(StryMin)
        yMax = int(StryMax)
        if yMin > yMax:
            temp = yMin
            yMin = yMax
            yMax = temp
        #-----Z-----
        zMin = int(StrzMin)
        zMax = int(StrzMax)
        if zMin > zMax:
            temp = zMin
            zMin = zMax
            zMax = temp
        for x in range(xMin,xMax+1):
            if x > 50:
                pass
            elif x < -50:
                pass
            else:
                for y in range(yMin,yMax+1):
                    if y > 50:
                        pass
                    elif y < -50:
                        pass
                    else:
                        for z in range(zMin,zMax+1):
                            if z > 50:
                                pass
                            elif z < -50:
                                pass
                            else:
                                lstCubesSpace[(x,(y,z))] = bOn
    counter = 0
    for cubeRow in lstCubesSpace.items():
        if cubeRow[1] == True:
            counter += 1
    return counter

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print('p1:',solvep1("22/input.txt"))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))
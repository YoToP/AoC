from time import time
from collections import defaultdict

class Cuboid:
    def __init__(self,on,x1,y1,z1,x2,y2,z2): #constructor
        self.On = on
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2
        self.inteferenceCuboid = []

    def envelops(self,cuboid):
        if self.x1 <= cuboid.x1 and self.x2 >= cuboid.x2:#X = inside
            if self.y1 <= cuboid.y1 and self.y2 >= cuboid.y2:#Y=inside
                if self.z1 <= cuboid.z1 and self.z2 >= cuboid.z2:#Z = inside
                    #all are inside this cuboid, so yes, this cuboid evelops the other
                    return True
        return False

def getSeperateCubiods(firstcuboid,secondcuboid):
    lstSeperateCuboidsList = []
    

def CalcCuboidIntersect(cuboid1,cuboid2):
    return CalcIntersect(cuboid1.x1,cuboid1.y1,cuboid1.z1,cuboid1.x2,cuboid1.y2,cuboid1.z2,cuboid2.x1,cuboid2.y1,cuboid2.z1,cuboid2.x2,cuboid2.y2,cuboid2.z2)

def CalcIntersect(x1,y1,z1,x2,y2,z2,a1,b1,c1,a2,b2,c2):
    return max(min(a2,x2)-max(a1,x1),0) * max(min(b2,y2)-max(b1,y1),0) * max(min(c2,z2)-max(c1,z1),0)

def solvep2(path):
    lstCuboidList = []
    
    with open(path) as f: lines = f.readlines()
    counter = 0
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
        newCuboid = Cuboid(bOn,xMin, yMin, zMin, xMax, yMax, zMax)
        
        for cuboid in lstCuboidList:
            if newCuboid.envelops(cuboid):
                lstCuboidList.remove(cuboid)
        lstCuboidList.append(newCuboid)
    
    lstNewCubiodList = []
    for firstcuboid in lstCuboidList.copy():
        lstCuboidList.remove(firstcuboid)
        for secondcuboid in lstCuboidList.copy():
            if CalcCuboidIntersect(firstcuboid,secondcuboid) > 0:
                getSeperateCubiods(firstcuboid,secondcuboid)

    
    #for j in range(0,len(lstCuboidList)):
    #    i= len(lstCuboidList) -1 - j
    #    for cuboid in lstCuboidList:
    #        if CalcCuboidIntersect(lstCuboidList[i],cuboid) > 0:
    #            cuboid.inteferenceCuboid.append(lstCuboidList[i])
    #step 2 check intersect and split the cubes in new cubes
    #for cuboid in lstCuboidList:
#
#    if CalcCuboidIntersect(newCuboid,cuboid) > 0:
#        cuboid.inteferenceCuboid.append(newCuboid)
#            counter +=1
        #for x in range(xMin,xMax+1):
        #    for y in range(yMin,yMax+1):
        #        for z in range(zMin,zMax+1):
        #            lstCubesSpace[(x,(y,z))] = bOn

   
    return counter


if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print('p2:',solvep2("22/example2.txt"))
    #print(CalcIntersect(-20,-36,-47,26,17,7,-20,-21,-26,33,23,28))
    #on x=-20..26,y=-36..17,z=-47..7
    #on x=-20..33,y=-21..23,z=-26..28
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))
from time import time
from math import sqrt
from collections import defaultdict
import copy

lstAlgo = []
lstImageColumn = []
lstEmptyImageRow = [] #used in multiple functions
canFlip = False

def DEBUGprint():
    print("----------")
    for row in lstImageColumn:
        sRow = ""
        for char in row:
            if char == 1:
                sRow = sRow + "#"
            else:
                sRow = sRow + "."
        print(sRow)
    print("----------")


def calcLit():
    total = 0
    for row in lstImageColumn:
        for char in row:
            if char == 1:
                total = total + 1
    return total

def calc9Grid(lstGrid):
    getal = 0
    for i in range(9):
        if lstGrid[i] == 1:
            getal += 2**(8-i)
    return getal

def enhance():
    global flipped
    global canFlip
    if canFlip:
        if flipped:
            infiniteValue = 1
            nextvalue = 0
        else:
            infiniteValue = 0
            nextvalue = 1
    else:
        infiniteValue = 0
        nextvalue = 0
    lineCounter = 0
    lstImageColumnCopy = copy.deepcopy(lstImageColumn)
    copyImagesizeY = len(lstImageColumnCopy) #length
    copyImagesizeX = len(lstImageColumnCopy[0]) #width
    lstCOPYEmptyImageRow = []
    for x in range(copyImagesizeX):
        lstCOPYEmptyImageRow.append(infiniteValue)
    lstImageColumn.clear()
    lstNEWEmptyImageRow = []
    newImagesizeX = 0 #width of the new MAtrix
    newRow = []
    for row in lstImageColumnCopy:
        rowCounter = 0

        newRow = [nextvalue]
        for char in row:
            gridList = [] #contains list to be calculated
            prevRow = []
            nextRow = []
            if lineCounter == 0:
                prevRow = lstCOPYEmptyImageRow.copy()
                nextRow = lstImageColumnCopy[lineCounter+1]
            elif lineCounter == (copyImagesizeY - 1):
                prevRow = lstImageColumnCopy[lineCounter-1]
                nextRow = lstCOPYEmptyImageRow.copy()
            else:
                prevRow = lstImageColumnCopy[lineCounter-1]
                nextRow = lstImageColumnCopy[lineCounter+1]
            
            if rowCounter == 0:
                #PreviousRow
                gridList.append(infiniteValue)
                gridList.append(prevRow[0])
                gridList.append(prevRow[1])
                #CurrentRow
                gridList.append(infiniteValue)
                gridList.append(row[0])
                gridList.append(row[1])
                #NextRow
                gridList.append(infiniteValue)
                gridList.append(nextRow[0])
                gridList.append(nextRow[1])
            elif rowCounter == (copyImagesizeX-1):
                #PreviousRow
                gridList.append(prevRow[rowCounter-1])
                gridList.append(prevRow[rowCounter])
                gridList.append(infiniteValue)
                #CurrentRow
                gridList.append(row[rowCounter-1])
                gridList.append(row[rowCounter])
                gridList.append(infiniteValue)
                #NextRow
                gridList.append(nextRow[rowCounter-1])
                gridList.append(nextRow[rowCounter])
                gridList.append(infiniteValue)
            else:
                #PreviousRow
                gridList.append(prevRow[rowCounter-1])
                gridList.append(prevRow[rowCounter])
                gridList.append(prevRow[rowCounter+1])
                #CurrentRow
                gridList.append(row[rowCounter-1])
                gridList.append(row[rowCounter])
                gridList.append(row[rowCounter+1])
                #NextRow
                gridList.append(nextRow[rowCounter-1])
                gridList.append(nextRow[rowCounter])
                gridList.append(nextRow[rowCounter+1])
            TMPgridvalue= calc9Grid(gridList)
            TMPfromAlgo = lstAlgo[TMPgridvalue]
            newRow.append(TMPfromAlgo)
            rowCounter += 1
        newRow.append(nextvalue)

        if lineCounter == 0:
            newImagesizeX = len(newRow)
            for x in range(newImagesizeX):
                lstNEWEmptyImageRow.append(nextvalue)
            lstImageColumn.append(lstNEWEmptyImageRow.copy())
        lstImageColumn.append(newRow.copy())
        lineCounter += 1
    lstImageColumn.append(lstNEWEmptyImageRow.copy())
    flipped = not flipped


def solvep1(path,enhancementFactor):
    with open(path) as f: lines = f.readlines()
    #ALGORITM
    #Import line
    for char in lines[0]:
        if char == '#':
            lstAlgo.append(1)
        else:
            lstAlgo.append(0)
    #check if bit zero is 1, because then the field flips every odd cycle
    global canFlip
    if lstAlgo[0] == 1:
        canFlip = True
    else:
        canFlip = False
    
    lineCounter = 0
    ImagesizeX = 0
    for line in lines: # read the image from file
        lstImageRow = []
        if lineCounter > 1:
            lstImageRow.append(0)
            for char in line:
                if char == '#':
                    lstImageRow.append(1)
                elif char == '.':
                    lstImageRow.append(0)
            lstImageRow.append(0)
            if lineCounter == 2: #one time length check
                ImagesizeX = len(lstImageRow)
            lstImageColumn.append(lstImageRow.copy())
        elif lineCounter == 1:
            lstImageColumn.append([]) #reserve empty row
        lineCounter += 1
    
    for x in range(ImagesizeX):
        lstEmptyImageRow.append(0)
    lstImageColumn[0] = lstEmptyImageRow.copy()
    lstImageColumn.append(lstEmptyImageRow.copy())

    #DEBUGprint()
    global flipped
    flipped = False
    for x in range(enhancementFactor):
        enhance()
        #DEBUGprint()
        #print(f"Amount Lit: ",calcLit()," len: ",len(lstImageColumn))
    DEBUGprint()
    return calcLit()

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    #print('p1:',solvep1("20/input.txt",2))
    print('p2:',solvep1("20/input.txt",50))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))
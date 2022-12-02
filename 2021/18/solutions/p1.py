from time import time
import math
def addTuple(t1,t2):
    newTuple = [t1,t2]
    #check depth, cannot be higher than 4 deep.

    while checkDepth(newTuple) > 4 or NeedSplit(newTuple):
        while checkDepth(newTuple) > 4:
            explodeRec(newTuple,1)
        splitTupleRec(newTuple)
        
    return newTuple

def checkDepth(t):
    t1,t2 = t
    maxDepth = 0
    if isinstance(t1, int) and isinstance(t2, int):
        return 1
    else:
        if isinstance(t1, list):
            returnValue = checkDepth(t1)
            if returnValue > maxDepth: maxDepth = returnValue
        if isinstance(t2, list):
            returnValue = checkDepth(t2)
            if returnValue > maxDepth: maxDepth = returnValue
    return maxDepth + 1

def explodeRec(parent,depth):
    #print(parent)

    if isinstance(parent[0], list):
        depthT1 = checkDepth(parent[0])
    else: depthT1 = 0
    if isinstance(parent[1], list):
        depthT2 = checkDepth(parent[1])
    else: depthT2 = 0
    addRight = 0
    addLeft = 0
    if(depthT1 == 1 and depthT2 == 0): #Found
        addLeft, addRight = parent[0]
        parent[1] += addRight
        addRight = 0
        parent[0] = 0
    elif(depthT1 == 0 and depthT2 == 1): #Found
        addLeft, addRight = parent[1]
        parent[0] += addLeft
        addLeft = 0
        parent[1] = 0
    elif (depthT1 == 1 and depthT2 == 1): #both Found, then left is first
        addLeft, addRight = parent[0]
        parent[1][0] += addRight #special case to add irectly in right pair.
        addRight = 0
        parent[0] = 0
    elif depth+depthT1 > 4: #Search Deeper
        if isinstance(parent[0], int):
            dummy = 1
        addLeft, addRight = explodeRec(parent[0],depth+1)
        if isinstance(parent[1], int):
            parent[1] += addRight
        else:
            addLeftRec(parent[1],addRight) #right value, must be added to the left
        addRight = 0
    elif depth+depthT2 > 4: # search Deeper
        addLeft, addRight = explodeRec(parent[1],depth+1)
        if isinstance(parent[0], int):
            parent[0] += addLeft
        else:
            addRightRec(parent[0],addLeft) #left value, must be added to the left
        addLeft = 0

    return (addLeft,addRight)

def addRightRec(parent, toAdd):
    if isinstance(parent[1], int):
        parent[1] += toAdd
    else:
        addRightRec(parent[1],toAdd)

def addLeftRec(parent, toAdd):
    if isinstance(parent[0], int):
        parent[0] += toAdd
    else:
        addLeftRec(parent[0],toAdd)


def calcMagintude(parent):
    value = 0
    if isinstance(parent[0], list):
        value += 3* calcMagintude(parent[0])
    else:
        value += 3* parent[0]

    if isinstance(parent[1], list):
        value += 2* calcMagintude(parent[1])
    else:
        value += 2* parent[1]
    return value

def splitTupleRec(parent):
    done = False
    #print('split',parent)
    if isinstance(parent[0], list):
        done = splitTupleRec(parent[0])
        if done:
            return done
    else:
        if parent[0] >= 10:
            parent[0] = [math.floor(parent[0]/2),math.ceil(parent[0]/2)]
            return True

    if isinstance(parent[1], list):done = splitTupleRec(parent[1])
    else:
        if parent[1] >= 10:
            parent[1] = [math.floor(parent[1]/2),math.ceil(parent[1]/2)]
            return True
    return done

def NeedSplit(parent):
    need = False
    if isinstance(parent[0], list):
        need = NeedSplit(parent[0])
        if need:
            return need
    else:
        if parent[0] >= 10:
            need = True

    if isinstance(parent[1], list):need = NeedSplit(parent[1])
    else:
        if parent[1] >= 10:
            need = True
    return need

getTupleIndex = 0
def getTuple(string):
    p1 = -1
    global getTupleIndex
    getTupleIndex +=1
    newTuple = []
    while getTupleIndex < len(string):
        if '0' <= string[getTupleIndex] <= '9':
            if p1 == -1:
                p1 = int(string[getTupleIndex])
            else:
                newTuple = [p1,int(string[getTupleIndex])]
                break
        elif string[getTupleIndex] ==  '[':
            if p1 == -1:
                p1 = getTuple(string)
            else:
                newTuple = [p1,getTuple(string)]
                break
        getTupleIndex += 1
    return newTuple

def solvep1(path):
    with open(path) as f: lines = f.readlines()
    global _sSnailData
    _sSnailData = ''
    tupleList = []
    global getTupleIndex
    getTupleIndex = 0
    for line in lines: #First run, check for all the starts,end and the rest and seperate them
        line = line.replace('\n', '')
        getTupleIndex = 0
        tupleList.append(getTuple(line))
    #calc the result
    _result = tupleList[0]
    for i in range(1,len(tupleList)):
        _result = addTuple(_result,tupleList[i])
    return calcMagintude(_result)

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print('p1:',solvep1("18/input.txt"))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))
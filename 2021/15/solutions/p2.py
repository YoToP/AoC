from time import time
from collections import defaultdict
from copy import copy
def solvep2(path,FACTOR):
    with open(path) as f:
        lines = f.readlines()
    matrix = []
    height = 0
    width = 0
    for line in lines: # load playing field into matrix
        height += 1
        line = line.replace('\n', '')
        width = len(line)
        lstLine = []
        for nr in line:
            lstLine.append(int(nr))
        matrix.append(lstLine)
    #generate super amtrix for part two:
    SuperMatrix = []
    for f in range(FACTOR):
        for i in range(height):
            supList = []
            for j in range(width):
                supList.append(matrix[i][j] + f)
                if supList[j] > 9:
                    supList[j] -= 9
            SuperMatrix.append(supList)
    for f in range(1,FACTOR):
        for i in range(height*FACTOR):
            supList = []
            for j in range(width):
                supList.append(SuperMatrix[i][j]+f)
                if supList[j] > 9:
                    supList[j] -= 9
            SuperMatrix[i] += supList
    #Create Scorelist which contains shortest path for each node(cell in matrix)
    #no need for remembering where it came from since it is a matrix, and we always start top left, so the graph will always look the same.
    lstScoreList = defaultdict(int) # the int in the dict is the shortest path
    lstScoreList[(0,0)] = 0
    while(True):
        _lstCopyScoreList = copy(lstScoreList) #copy list to iterate over
        print(len(lstScoreList))
        nothing = True
        for _node,_shortespath in _lstCopyScoreList.items():
            i,j = _node
            bToBeRemoved = True #node is not used anymore
            #check right
            if (j + 1 < (width*FACTOR)): #check out of bounds and not in copy list
                if lstScoreList[(i,j+1)] == 0:
                    lstScoreList[(i,j+1)] = _shortespath + SuperMatrix[i][j+1]
                    nothing = False
                    bToBeRemoved = False
                elif lstScoreList[(i,j+1)] > _shortespath + SuperMatrix[i][j+1]:
                    lstScoreList[(i,j+1)] = _shortespath + SuperMatrix[i][j+1]
                    nothing = False
                    bToBeRemoved = False

                
            #check down
            if i + 1 < (height*FACTOR): #check out of bounds
                if lstScoreList[(i+1,j)] == 0:
                    lstScoreList[(i+1,j)] = _shortespath + SuperMatrix[i+1][j]
                    nothing = False
                    bToBeRemoved = False
                elif lstScoreList[(i+1,j)] > _shortespath + SuperMatrix[i+1][j]:
                    lstScoreList[(i+1,j)] = _shortespath + SuperMatrix[i+1][j]
                    nothing = False
                    bToBeRemoved = False
            #check up
            if i - 1 >= 0: #check out of bounds
                if lstScoreList[(i-1,j)] == 0:
                    lstScoreList[(i-1,j)] = _shortespath + SuperMatrix[i-1][j]
                    nothing = False
                    bToBeRemoved = False
                elif lstScoreList[(i-1,j)] > _shortespath + SuperMatrix[i-1][j]:
                    lstScoreList[(i-1,j)] = _shortespath + SuperMatrix[i-1][j]
                    nothing = False
                    bToBeRemoved = False
            #check left
            if j - 1 >= 0: #check out of bounds
                if lstScoreList[(i,j-1)] == 0:
                    lstScoreList[(i,j-1)] = _shortespath + SuperMatrix[i][j-1]
                    nothing = False
                    bToBeRemoved = False
                elif lstScoreList[(i,j-1)] > _shortespath + SuperMatrix[i][j-1]:
                    lstScoreList[(i,j-1)] = _shortespath + SuperMatrix[i][j-1]
                    nothing = False
                    bToBeRemoved = False

        if nothing:
            break
        
    return lstScoreList[(height*FACTOR-1,width*FACTOR-1)]

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print("part 2:",solvep2("2021/15/inputs/input.txt",5))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))
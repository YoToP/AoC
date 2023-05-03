from time import time
from collections import defaultdict
from copy import copy
def solvep1(path):
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
    

    lstScoreList = defaultdict(int) # the int is the shortest path
    lstScoreList[(0,0)] = 0
    while(True):
        _lstCopyScoreList = copy(lstScoreList) #copy list to iterate over

        nothing = True
        for _node,_shortespath in _lstCopyScoreList.items():
            i,j = _node
            #check right
            if (j + 1 < len(matrix[i])): #check out of bounds and not in copy list
                if lstScoreList[(i,j+1)] == 0:
                    lstScoreList[(i,j+1)] = _shortespath + matrix[i][j+1]
                    nothing = False
                elif lstScoreList[(i,j+1)] > _shortespath + matrix[i][j+1]:
                    lstScoreList[(i,j+1)] = _shortespath + matrix[i][j+1]
                    nothing = False
                
            #check down
            if i + 1 < len(matrix): #check out of bounds
                if lstScoreList[(i+1,j)] == 0:
                    lstScoreList[(i+1,j)] = _shortespath + matrix[i+1][j]
                    nothing = False
                elif lstScoreList[(i+1,j)] > _shortespath + matrix[i+1][j]:
                    lstScoreList[(i+1,j)] = _shortespath + matrix[i+1][j]
                    nothing = False
            #check up
            if i - 1 >= 0: #check out of bounds
                if lstScoreList[(i-1,j)] == 0:
                    lstScoreList[(i-1,j)] = _shortespath + matrix[i-1][j]
                    nothing = False
                elif lstScoreList[(i-1,j)] > _shortespath + matrix[i-1][j]:
                    lstScoreList[(i-1,j)] = _shortespath + matrix[i-1][j]
                    nothing = False
            #check left
            if j - 1 >= 0: #check out of bounds
                if lstScoreList[(i,j-1)] == 0:
                    lstScoreList[(i,j-1)] = _shortespath + matrix[i][j-1]
                    nothing = False
                elif lstScoreList[(i,j-1)] > _shortespath + matrix[i][j-1]:
                    lstScoreList[(i,j-1)] = _shortespath + matrix[i][j-1]
                    nothing = False
        if nothing:
            break
    return lstScoreList[(height-1,width-1)]

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print("part 1:",solvep1("15/911.txt"))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))
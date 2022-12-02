from time import time
def rowBingo(board,width):
    for i in range(width):
        rowBingo = 0
        for j in range(width):
            if board[i][j][1] == True:
                rowBingo += 1
                if rowBingo == width:
                    return True
    return False

def columnBingo(board,width):
    for i in range(width):
        columnBingo = 0
        for j in range(width):
            if board[j][i][1] == True:
                columnBingo += 1
                if columnBingo == width:
                    return True
    return False

def sumUnmarked(board,width):
    sum = 0
    for i in range(width):
        for j in range(width):
            if board[j][i][1] == False:
                sum += board[j][i][0]
    return sum

def solvep2(path, width):
    with open(path) as f:
        lines = f.readlines()
    lstBoards = []
    #number on each board is a tuple (#, boolean)
    bFirstLine = True
    lstChosenNumbers = []
    for line in lines:
        if not bFirstLine:
            if len(line) < 10: #Reset administration on empty line
                _rowCount = 0
                _lstBoard = []
                for i in range(width):
                    _lstBoard.append([])
            if len(line) >= 10:#skip empty rows
                _lineElements = line.split(" ")#causes problem with single digits
                _filtertLineElements = [] # so we need an array with filtered elements. 
                for lineElement in _lineElements:
                    if lineElement != '': # filter by removing empty elements in the text
                        _filtertLineElements.append((int(lineElement),False)) #and add the tuple with a False bit, used for the score
                _lstBoard[_rowCount] = _filtertLineElements.copy()
                _rowCount += 1
                if _rowCount == width:
                    lstBoards.append(_lstBoard.copy())
        if bFirstLine:#read chosen numbers on first line
            lstChosenNumbers = line.split(",")
            bFirstLine = False
    #all boards loaded
    boardcount = len(lstBoards)
    #P2 now find the last board!!
    nummers = len(lstChosenNumbers)
    for _number in lstChosenNumbers:
        nummers -= 1
        for i in range(len(lstBoards)):
            if lstBoards[i] != '': # P2 check for out of play cards
                #mark chosen nr
                for x in range(width):
                    for y in range(width):
                        if lstBoards[i][x][y][0] == int(_number):
                            lstBoards[i][x][y] = (int(_number),True)
                if rowBingo(lstBoards[i],width) or columnBingo(lstBoards[i],width):
                    #remove card from play
                    if boardcount == 1:
                        return sumUnmarked(lstBoards[i],width)*int(_number)
                    else:
                        lstBoards[i] = '' #remove card from play
                        boardcount -= 1               
    return 0

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print(solvep2("4/input.txt",5))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))
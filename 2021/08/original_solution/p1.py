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

def solvep1(path,width):
    with open(path) as f:
        lines = f.readlines()
    #Create boards 5x5
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
            if len(line) >= 10:#skip empty rows TODO ugly hack!!
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
    for _number in lstChosenNumbers:
        for i in range(len(lstBoards)):
            #mark chosen nr
            for x in range(width):
                for y in range(width):
                    _scratch = lstBoards[i][x][y][0]
                    if lstBoards[i][x][y][0] == int(_number):
                        lstBoards[i][x][y] = (int(_number),True)
            
            if rowBingo(lstBoards[i],width) or columnBingo(lstBoards[i],width):
                return sumUnmarked(lstBoards[i],width)*int(_number)
    return 0

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    print(solvep1("4/input.txt"))
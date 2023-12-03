def p1():
    with open("2023/03/inputs/input.txt") as f:
        lines = f.readlines()
    score = 0


    for i in range(0,len(lines)):
        sequence = ''
        isValid = False
        for j in range(0,len(lines[0])-1):
            isValidUpDown = False
            if lines[i][j] == '\n':
                pass
            else:
                #line below
                if i < len(lines)-1:
                    if lines[i+1][j] == '.': #
                        pass
                    elif lines[i+1][j].isdigit():
                        pass # do nothing with numbers on other lines
                    else: #it must be another char
                        isValid = True
                        isValidUpDown = True
                #line Above
                if i > 0:
                    if lines[i-1][j] == '.': #
                        pass
                    elif lines[i-1][j].isdigit():
                        pass # do nothing with numbers on other lines
                    else: #it must be another char
                        isValid = True
                        isValidUpDown = True
                #Current line
                if lines[i][j] == '.': #
                    if len(sequence) > 0:
                        if isValid:
                            score =score + int(sequence)
                            sequence = ''
                            if not isValidUpDown: #dont invalidate when currently updown, can be used for next
                                isValid = False
                        else:
                            sequence = ''
                    else:
                        if not isValidUpDown:
                            isValid = False
                elif lines[i][j].isdigit():
                    sequence = sequence +lines[i][j]
                else: #it must be another char
                    isValid = True
                    if len(sequence) > 0:
                        score =score + int(sequence)
                        sequence = ''
        #end of line, should also count
        if len(sequence) > 0 and isValid:
                        score =score + int(sequence)
                        sequence = ''
    return score


def p2(): 
    with open("2023/03/inputs/input.txt") as f:
        _lines = f.readlines()
    matrix = []
    for line in _lines:
        matrix.append(list(line.strip()))
    score = 0
    
    def findAdjecent(x,y):
        #x,y is location of '*'
        def findSeq(_i,_j):
            #find start sequence
            _startJ = _j
            while matrix[_i][_startJ-1].isdigit():
                _startJ -= 1

            #collect whole sequence
            _seq = ''
            _endJ = _startJ
            if _endJ < len(matrix[_i]):
                while matrix[_i][_endJ].isdigit():
                    _seq += matrix[_i][_endJ]
                    matrix[_i][_endJ] = '.'
                    _endJ += 1
                    if _endJ == len(matrix[_i]):
                        break
            return _seq

        seq1 = ''
        seq2 = ''
        for a in range(x-1,x+2):
            for b in range(y-1,y+2):
                toCheck = matrix[a][b]
                if matrix[a][b].isdigit():
                    if len(seq1) > 0:
                        seq2 = findSeq(a,b)
                    else:
                        seq1 = findSeq(a,b)
        if len(seq1) > 0 and len(seq2) >0:          
            sum = int(seq1) * int(seq2)
        else:
            sum = 0
        return sum

    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])-1):
            #Current line
            if matrix[i][j] == '*': #
                score += findAdjecent(i,j)
    return score

if __name__ == '__main__':
    print(f"part 1: {p1()}")
    print(f"part 2: {p2()}")
from time import time

def p1():
    field = []
    with open("2023/11/inputs/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            if '#' in line:
                field.append(list(line))
            else:
                field.append(list(line))
                field.append(list(line.replace('.','+')))
    
    j = 0 #column
    while j < len(field[0]): # per column
        emptyColumn = True
        i = 0 #row
        while i < len(field): # check every row if 'empty'
            if field[i][j] == '#':
                emptyColumn = False
                break
            i += 1 #next row
        if emptyColumn:
            i = 0
            while i < len(field): # check every row if 'empty'
                field[i].insert(j,'+')
                i += 1
            j += 1 #we increased the field, so inc to get the next column and not the one we just created
        j += 1

    galaxyList = []
    i = 0
    while i < len(field):
        j = 0
        while j < len(field[i]):
            if field[i][j] == '#':
                galaxyList.append((i,j))
            j += 1
        i += 1

    score = 0
    i = 0
    while i < len(galaxyList):
        j = 0
        while j < len(galaxyList):
            if i == j:
                pass# do not check yourself
            else:
                a = galaxyList[i]
                b = galaxyList[j]
                diffRow = abs(galaxyList[i][0] - galaxyList[j][0])
                diffColumn = abs(galaxyList[i][1] - galaxyList[j][1])
                score += diffRow + diffColumn
                pass
            j += 1
        i += 1


    return score / 2

def p2():
    with open("2023/11/inputs/input.txt") as f:
        _lines = f.readlines()
    

    return 0

if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', p1())
    print("### p1 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    start_time = int(round(time() * 1000))
    print('part 2:', p2())
    print("### p2 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
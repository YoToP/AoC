from time import time
def solvep2(path):
    with open(path) as f:
        lines = f.readlines()
    gridlist = []
    bFoldInstructions = False
    for line in lines:
        line = line.replace('\n', '')
        if line == '':bFoldInstructions = True
        elif not bFoldInstructions:
            x, y = line.split(',') #x is to the right, y is down
            gridlist.append((int(y),int(x)))
        else:
            coord, foldLinePos = line.split(' ')[2].split('=')
            foldLinePos = int(foldLinePos)
            for i in range(len(gridlist)):
                y, x = gridlist[i]
                if coord == 'y':
                    if y > foldLinePos:
                        gridlist[i] = (foldLinePos-(y - foldLinePos),x)
                elif coord == 'x':
                    if x > foldLinePos:
                        gridlist[i] = (y,foldLinePos -(x-foldLinePos))

    maxRow = 0
    maxColumn = 0
    for y, x in gridlist:
        if y > maxRow:
            maxRow = y
        if x > maxColumn:
            maxColumn = x
    stringlines = []
    for i in range(maxRow+1):
        _string = []
        for j in range(maxColumn+1):
            _string.append(' ')
        stringlines.append(_string)
    for y, x in gridlist:
        stringlines[y][x] = chr(9608) #unicode for block
    

    for _string in stringlines:
        print("".join(_string))
    return 0

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    solvep2("2021/13/inputs/input.txt")
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))
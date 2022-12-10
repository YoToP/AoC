from time import time
from collections import defaultdict
from copy import deepcopy
def solvep1(path):
    with open(path) as f:
        lines = f.readlines()
    grid = defaultdict(lambda: defaultdict(int))
    
    bFoldInstructions = False
    for line in lines:
        line = line.replace('\n', '')
        if line == '':bFoldInstructions = True
        elif not bFoldInstructions:
            x, y = line.split(',') #x is to the right, y is down
            grid[int(y)][int(x)] += 1
        else:
            coord, foldLinePos = line.split(' ')[2].split('=')
            foldLinePos = int(foldLinePos)
            if coord == 'y':
                _copyGrid = deepcopy(grid)
                for _row, _grid in _copyGrid.items():
                    if _row > foldLinePos:
                        for _column, _x in _grid.items(): 
                            grid[foldLinePos-(_row - foldLinePos)][_column] += 1
                            print('y',_row,foldLinePos)
                        del grid[_row]
                    
            elif coord == 'x':
                _copyGrid = deepcopy(grid)
                for _row, _grid in _copyGrid.items():
                    for _column, _x in _grid.items(): 
                        if _column > foldLinePos:
                            grid[_row][foldLinePos -(_column-foldLinePos)] += 1
                            print('x',_row,foldLinePos)
                        if _column > foldLinePos: 
                            del grid[_row][_column]
            break #part 1 break needed

    total = 0  
    for _row, _grid in grid.items():
        total +=  len(_grid.items())
    return total

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print(solvep1("2021/13/inputs/input.txt"))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))
from time import time
from collections import defaultdict

def solvep2(path):
    with open(path) as f:
        lines = f.readlines()
    grid = defaultdict(int)
    for line in lines:
        iFromH = int(line.split(" -> ")[0].split(",")[0])
        iFromV = int(line.split(" -> ")[0].split(",")[1])
        iToH = int(line.split(" -> ")[1].split(",")[0])
        iToV = int(line.split(" -> ")[1].split(",")[1])

        #determine horizontal
        if iFromH == iToH:
            if iFromV < iToV:
                for i in range(iToV-iFromV+1):
                    grid[(iFromH,iFromV+i)] += 1
            else:
                for i in range(iFromV-iToV+1):
                    grid[(iFromH,iToV+i)] += 1
        #determine vertical
        elif iFromV == iToV:
            if iFromH < iToH:
                for i in range(iToH-iFromH+1):
                    grid[(iFromH+i,iFromV)] += 1
            else:
                for i in range(iFromH-iToH+1):
                    grid[(iToH+i,iFromV)] += 1
        #determine (suprising) diagonal
        else:
            if iFromH > iToH: #swap if fromH is higer than To, so only two solution have to be made
                _scratch = iFromH
                iFromH = iToH
                iToH = _scratch
                _scratch = iFromV
                iFromV = iToV
                iToV = _scratch
            if iFromV < iToV:
                for i in range(iToH-iFromH+1): #we must check with H, since we know for sure From is lower than To.
                    grid[(iFromH+i,iFromV+i)] += 1
            else:
                for i in range(iToH-iFromH+1): #we must check with H, since we know for sure From is lower than To.
                    grid[(iFromH+i,iFromV-i)] += 1
    return sum(1 for v in grid.values() if v >= 2)

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print(solvep2("5/input.txt"))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))
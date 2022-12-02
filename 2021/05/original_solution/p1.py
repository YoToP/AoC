from time import time
def AddUniqueAndTimesInList(list,tuple):
    timesInList = list.count(tuple)
    if timesInList == 0 or 1:
        list.append(tuple)
    return timesInList

def solvep1(path):
    with open(path) as f:
        lines = f.readlines()
    lstDangerzone = [] #main list
    intDangerzones = 0
    for line in lines: #0,9 -> 5,9
        iFromH = int(line.split(" -> ")[0].split(",")[0]) #0,9
        iFromV = int(line.split(" -> ")[0].split(",")[1]) #0,9
        iToH = int(line.split(" -> ")[1].split(",")[0]) #0,9
        iToV = int(line.split(" -> ")[1].split(",")[1]) #0,9


        #determine horizontal
        if iFromH == iToH:
            if iFromV < iToV:
                for i in range(iToV-iFromV+1):
                    value = AddUniqueAndTimesInList(lstDangerzone,(iFromH,iFromV+i))
                    if value == 1:
                        intDangerzones += 1
            else:
                for i in range(iFromV-iToV+1):
                    value = AddUniqueAndTimesInList(lstDangerzone,(iFromH,iToV+i))
                    if value == 1:
                        intDangerzones += 1
        #determine vertical
        if iFromV == iToV:
            if iFromH < iToH:
                for i in range(iToH-iFromH+1):
                    value = AddUniqueAndTimesInList(lstDangerzone,(iFromH+i,iFromV))
                    if value == 1:
                        intDangerzones += 1
            else:
                for i in range(iFromH-iToH+1):
                    value = AddUniqueAndTimesInList(lstDangerzone,(iToH+i,iFromV))
                    if value == 1:
                        intDangerzones += 1


    return intDangerzones

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print(solvep1("5/input.txt"))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))
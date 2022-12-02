def createFilter(lines,column):
    localFilter = []
    for i in range(column):
        localFilter.append(0)
    #read lines
    for line in lines:
        if line != '':
            for i in range(column):
                if line[i] == '0':
                    localFilter[i] = localFilter[i] - 1
                if line[i] == '1':
                    localFilter[i] = localFilter[i] + 1
    return localFilter

def checkHowManyRowsLeft(lines):
    count = 0
    for line in lines:
        if line != '':
            count = count + 1
    return count

def solvep2(path,column):
    with open(path) as f:
        lines = f.readlines()
    #init
    s = createFilter(lines,column)
#O2------------------------------------------------------------------------------------
    oxygenList = lines.copy() #copy list, and start deleting until one is left
    oxygenFilter = s
    for i in range(len(oxygenFilter)): # links naar rechts
        oxygenFilter = createFilter(oxygenList,column)
        for j in range(len(oxygenList)):
            if checkHowManyRowsLeft(oxygenList) == 1: # is only 1 left?
                break # keep breaking until out of i loop
            if oxygenList[j] != '':
                if oxygenFilter[i] > 0:
                    if oxygenList[j][i] == '0':
                        oxygenList[j] = ''
                if oxygenFilter[i] < 0:
                    if oxygenList[j][i] == '1':
                        oxygenList[j] = ''
                if oxygenFilter[i] == 0: # if 0, then act like > 0
                    if oxygenList[j][i] == '0':
                        oxygenList[j] = ''    
                                            
    #find the remaining char
    for line in oxygenList:
        if line != '':
            oxygenGetal = int(line,2)
            break    
#CO2------------------------------------------------------------------------------------
    CO2List = lines.copy() #copy list, and start deleting until one is left
    CO2Filter = createFilter(CO2List,column)
    for i in range(len(CO2Filter)): # links naar rechts
        CO2Filter = createFilter(CO2List,column)
        for j in range(len(CO2List)):
            if checkHowManyRowsLeft(CO2List) == 1:# is only 1 left?
                break# keep breaking until out of i loop
            if CO2List[j] != '':
                if CO2Filter[i] > 0:
                    if CO2List[j][i] == '1':
                        CO2List[j] = ''
                if CO2Filter[i] < 0:
                    if CO2List[j][i] == '0':
                        CO2List[j] = ''
                if CO2Filter[i] == 0: # if 0, then act like < 0
                    if CO2List[j][i] == '1':
                        CO2List[j] = ''                                    
    #find the remaining char
    for line in CO2List:
        if line != '':
            CO2Getal = int(line,2)
            break
    return oxygenGetal * CO2Getal

if __name__ == '__main__':
    print(solvep2("3/input.txt",12))
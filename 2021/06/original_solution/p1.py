from time import time
def solvep1(path,maxdays):
    with open(path) as f:
        lines = f.readlines()
    lstFishDatabase = []
    for i in range(maxdays+1):
        lstFishDatabase.append(0)
    for nr in lines[0].split(','):
        lstFishDatabase[int(nr)] += 1

    #80 rounds:
    for i in range(80):
        _worklist = lstFishDatabase.copy()
        for j in range(maxdays+1):
            if j < maxdays:
                lstFishDatabase[j] = _worklist[j+1]
            if j == maxdays:
                lstFishDatabase[maxdays] = _worklist[0]
                lstFishDatabase[6] += _worklist[0]
    iPopulation = 0
    for amount in lstFishDatabase:
        iPopulation += amount
    return iPopulation

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print(solvep1("6/input.txt",8))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))
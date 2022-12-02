from time import time
def solvep2(path,maxdays):
    with open(path) as f:
        lines = f.readlines()
    lstFishDatabase = []
    for i in range(maxdays+1):
        lstFishDatabase.append(0)
    for nr in lines[0].split(','):
        lstFishDatabase[int(nr)] += 1

    #256 rounds:
    for i in range(256):
        _worklist = lstFishDatabase.copy()
        lstFishDatabase[0:8] = _worklist[1:9]
        lstFishDatabase[maxdays] = _worklist[0]
        lstFishDatabase[6] += _worklist[0]
    return sum(lstFishDatabase[0:9])

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print(solvep2("6/input.txt",8))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))
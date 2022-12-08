from time import time
from collections import deque

class dir:
    def __init__(self,name):
        self.name = name
        self.dirs = []
        self.files = []
        self.currentsize = 0

    def __repr__(self):
        return self.name

    def addFiles(self, name,size):
        self.files.append((name,size))

    def addDir(self, dir):
        self.dirs.append(dir)

    def getSize(self):
        for dir in self.dirs:
            self.currentsize += dir.getSize()
        for name,size in self.files:
            self.currentsize += int(size)
        return self.currentsize
    def isDirNameInDir(self,name):
        isInDir = False
        for dir in self.dirs:
            if dir.name == name:
                isInDir = True
        return isInDir
    def getTotalSizeDirsUnder(self,sizeLimit):
        totalsize = 0
        #self.getSize()
        if self.currentsize <= sizeLimit:
            totalsize+= self.currentsize
        for dir in self.dirs:
            totalsize += dir.getTotalSizeDirsUnder(sizeLimit)
        return totalsize
    def getDirSizesList(self):
        _dirList = []
        _dirList.append(self.currentsize)
        for dir in self.dirs:
            _dirList.extend(dir.getDirSizesList())
        return _dirList

def part1(path):
    with open(path) as f:
        data = f.readlines()
    historyList = deque()
    rootDir = dir('/')
    currentDir = rootDir
    for line in data:
        text = line.strip().split(" ")
        if text[0] == '$':
            if text[1] == 'cd':
                if text[2] == '/':
                    historyList.clear()
                    currentDir = rootDir
                elif text[2] == '..':#back
                    if len(historyList) > 0:
                        currentDir = historyList.pop()
                    else:
                        print("WARNING; cannot cd .., already at root")
                else:
                    if currentDir.isDirNameInDir(text[2]):
                        print("CD into exisitng dir; NOT IMPLEMENTED")
                    else:
                        _newDir = dir(text[2])
                        currentDir.addDir(_newDir)
                        historyList.append(currentDir)
                        currentDir = _newDir
            elif text[1] == 'ls':
                pass #No actions
            else:
                print(f"wrong command: {text[1]}")
        elif text[0] == 'dir':
            pass #No actions, only add when moving into dir with cd
        else:
            currentDir.addFiles(text[1],text[0])
    
    #calc sizes
    rootDir.getSize()
    return rootDir.getTotalSizeDirsUnder(100000)

#total disk space =
TOTAL_DISK_SPACE = 70000000
#need unused space =
NEEDED_UNUSED_SPACE = 30000000
def part2(path):
    with open(path) as f:
        data = f.readlines()
    historyList = deque()
    rootDir = dir('/')
    currentDir = rootDir
    for line in data:
        text = line.strip().split(" ")
        if text[0] == '$':
            if text[1] == 'cd':
                if text[2] == '/':
                    historyList.clear()
                    currentDir = rootDir
                elif text[2] == '..':#back
                    if len(historyList) > 0:
                        currentDir = historyList.pop()
                    else:
                        print("WARNING; cannot cd .., already at root")
                else:
                    if currentDir.isDirNameInDir(text[2]):
                        print("CD into exisitng dir; NOT IMPLEMENTED")
                    else:
                        _newDir = dir(text[2])
                        currentDir.addDir(_newDir)
                        historyList.append(currentDir)
                        currentDir = _newDir
            elif text[1] == 'ls':
                pass #No actions
            else:
                print(f"wrong command: {text[1]}")
        elif text[0] == 'dir':
            pass #No actions, only add when moving into dir with cd
        else:
            currentDir.addFiles(text[1],text[0])
    
    #calc sizes
    rootdirsize = rootDir.getSize()
    neededSpace = NEEDED_UNUSED_SPACE-(TOTAL_DISK_SPACE-rootdirsize)
    sizesList = rootDir.getDirSizesList()
    sizesList.sort()
    for size in sizesList:
        if size > neededSpace:
            return size
    return 0

if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', part1("2022/07/inputs/input.txt"))
    #print('example part 1:', part1("2022/07/inputs/example.txt"))
    print('part 2:', part2("2022/07/inputs/input.txt"))
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
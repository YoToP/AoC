from time import time
''' 
day13
'''
def ListCompare(leftList,rightList):
    if len(rightList) < len(leftList):
        return False
    elif len(rightList) > len(leftList):
        return True
    else:
        len(leftList)
    return False

def IntCompare(left, right):
    return left<right

def getList(string):
    _list = []
    i = 0
    while i < len(string):
        if string[i] =='[':
            #new list starts, find closing bracket.
            closingBracketsNeeded = 0
            for j in range(i+1,len(string)):
                if string[j] == ']':
                    if closingBracketsNeeded == 0:
                        _list.append(getList(string[i+1:j]))
                        i = j
                        break
                    else:
                        closingBracketsNeeded -=1
                elif string[j] == '[':
                    closingBracketsNeeded +=1
        elif string[i] >= '1' and string[i] <= '9':
            _list.append(int(string[i]))
        i +=1
    return _list

def part1(path):
    with open(path) as f:
        lines = f.read()
    pairs= lines.split('\n\n')
    
    pairCounter = 0
    CorrectPairSum = 0
    for pair in pairs:
        pairCounter += 1
        pleft,pright = pair.split('\n')
        leftlist = getList(pleft[1:len(pleft)-1])
        rightlist = getList(pright[1:len(pright)-1])
        
        if ListCompare(leftlist,rightlist):
            CorrectPairSum += pairCounter
        pass
    return CorrectPairSum


def part2(path):
    

    return 0


if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', part1("2022/13/inputs/example.txt"))
    print('part 2:', part2("2022/13/inputs/input.txt"))
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))

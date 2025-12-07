def isValidP1(s:str) -> bool:
    stringSize = len(s)

    if stringSize % 2 > 0: #odd values do not need to be checked
        return True
    else:
        x = int(stringSize/2)
        if s[:x] == s[x:stringSize]:
            return False
        else:
            return True
    return False

def isValidP2(s:str) -> bool:
    stringSize = len(s)

    if stringSize % 2 > 0: #odd values only needs singles to be checked
        allSame = True
        firstChar = s[0]
        for c in s:
            if c != firstChar:
                allSame = False
        if allSame:
            return False
        else:
            return True
    else:
        maxX = int(stringSize/2)
        x = 1
        while x <= maxX:
            if stringSize % x == 0:
                firstSlice = s[0:x]
                isSame = True
                for i in range(x,int(stringSize/x+x),x):
                    nextSlice = s[i:i+x]
                    if firstSlice != nextSlice:
                        isSame = False
                        break #break this for loop
                if isSame:
                    return False
            x += 1
        return True
    return False

def puzzle():
    ranges = []
    with open("2025/02/example.txt") as f:
        ranges = f.readline().strip().split(",")
    intranges = []
    for r in ranges:
        start,end = r.split("-")
        intranges.append((int(start),int(end)))
    scoreP1 = 0
    scoreP2 = 0
    for _s,_e in intranges:
        for _nr in range(_s,_e+1):
            if not isValidP1(str(_nr)):
                scoreP1 += _nr
            if _nr == 824824824:
                pass
            if not isValidP2(str(_nr)):
                scoreP2 += _nr
    return (scoreP1,scoreP2)

if __name__ == '__main__':
    p1,p2 = puzzle()
    print(f"part 1: {p1}")
    print(f"part 2: {p2}")
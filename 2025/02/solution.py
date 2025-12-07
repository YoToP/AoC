from collections import defaultdict


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

    if stringSize % 2 > 0: #odd values do not need to be checked
        return True
    else:
        x = int(stringSize/2)
        if s[:x] == s[x:stringSize]:
            return False
        else:
            return True
    return False

def puzzle():
    ranges = []
    with open("2025/02/input.txt") as f:
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
            if not isValidP2(str(_nr)):
                scoreP2 += _nr
    return (scoreP1,scoreP2)




if __name__ == '__main__':
    p1,p2 = puzzle()
    print(f"part 1: {p1}")
    print(f"part 2: {p2}")
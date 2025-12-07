from collections import defaultdict

def p1():
    def isValid(s:str) -> bool:
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
    ranges = []
    with open("2025/02/input.txt") as f:
        ranges = f.readline().strip().split(",")
    intranges = []
    for r in ranges:
        start,end = r.split("-")
        intranges.append((int(start),int(end)))
    score = 0
    for _s,_e in intranges:
        for _nr in range(_s,_e+1):
            if not isValid(str(_nr)):
                score += _nr
    return score


def p2():
    return 0

if __name__ == '__main__':
    print(f"part 1: {p1()}")
    print(f"part 2: {p2()}")
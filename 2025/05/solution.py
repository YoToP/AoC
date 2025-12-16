from time import time
import copy

def p1(ranges = [],idList = []):
    RangeList = []
    score = 0
    for _r in ranges:
        _s,_e = _r.split("-")
        RangeList.append(range(int(_s),int(_e)+1))
    for _id in idList:
        for _r in RangeList:
            if int(_id) in _r:
                score +=1
                break

    return score

def p2(ranges = []):
    ids = set()
    for _r in ranges:
        _s,_e = _r.split("-")
        for i in range(int(_s),int(_e)+1):
            ids.add(i)
    return len(ids)

if __name__ == '__main__':
    with open("2025/05/input.txt") as f:
        ranges,idList = f.read().split(f"{f.newlines}{f.newlines}")
        ranges = ranges.split(f"{f.newlines}")
        idList = idList.split(f"{f.newlines}")
    start_time = int(round(time() * 1000))
    print('part 1:', p1(ranges,idList))
    print("### p1 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    start_time = int(round(time() * 1000))
    print('part 2:', p2(ranges))
    print("### p2 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
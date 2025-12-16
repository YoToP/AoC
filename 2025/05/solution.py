from time import time

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
    RangeList = []
    score = 0
    for _r in ranges:
        _s,_e = _r.split("-")
        RangeList.append((int(_s),int(_e)))
    while True:
        if len(RangeList) == 0:
            break
        lowestStart = int(1e100)
        lowestRange = None
        lowestEnd = 0
        for _r in RangeList:
            _s,_e = _r
            if _s < lowestStart:
                lowestStart = _s
                lowestRange = _r
        lowestEnd = lowestRange[1]
        RangeList.remove(lowestRange)

        while True:
            removed = False
            for _r in RangeList:
                _s,_e = _r
                if lowestEnd >= _s:
                    if lowestEnd < _e:
                        lowestEnd = _e
                    RangeList.remove(_r)
                    removed = True
                    break
            if not removed:
                break
        score += (lowestEnd-lowestStart+1)
    return score

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
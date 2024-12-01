from time import time

def p1():
    lftList = []
    rhtList = []
    with open("2024/01/inputs/input.txt") as f:
        for line in f.readlines():
            lft, rht = line.strip().split("   ")
            lftList.append(int(lft))
            rhtList.append(int(rht))
    sortedLft = sorted(lftList)
    sortedRht = sorted(rhtList)
    score = 0
    for i in range(0,len(sortedLft)):
        score += abs(sortedLft[i]-sortedRht[i])
    return score

    

def p2():
    lftList = []
    rhtList = []
    with open("2024/01/inputs/input.txt") as f:
        for line in f.readlines():
            lft, rht = line.strip().split("   ")
            lftList.append(int(lft))
            rhtList.append(int(rht))

    score = 0
    for i in range(0,len(lftList)):
        count = rhtList.count(lftList[i])
        score += lftList[i] * count
    return score


if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', p1())
    print("### p1 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    start_time = int(round(time() * 1000))
    print('part 2:', p2())
    print("### p2 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
from time import time
def p1():
    with open("2023/05/inputs/input.txt") as f:
        blocks = f.read().split('\n\n')
    seeds = blocks[0].split(": ")[1].split(' ')
    lowest = 1e10
    #voor alle seeds:
    for seed in seeds:
        checkValue = int(seed)
        #check of deze in de lijst staat. anders is het nummer hetzelfde
        blockNr = 1
        while blockNr < 8:
            lines = blocks[blockNr].split('\n')
            for line in lines: 
                numbers = line.split(' ')
                if len(numbers) == 3:
                    #dest, Source, length
                    dest = int(numbers[0])
                    src = int(numbers[1])
                    length = int(numbers[2])
                    if checkValue in range(src,src+length+1):
                        checkValue = checkValue + (dest-src)
                        break
            blockNr += 1
        if checkValue < lowest:
            lowest = checkValue
    return lowest


def p2(): 
    with open("2023/05/inputs/input.txt") as f:
        blocks = f.read().split('\n\n')
    seedRangeLineElements = blocks[0].split(": ")[1].split(' ')
    i = 0
    seedRanges = []
    while i < len(seedRangeLineElements):
        start = int(seedRangeLineElements[i])
        end = start + int(seedRangeLineElements[i+1])
        seedRanges.append((start,end))
        i+=2
    lowest = 1e10

    #Per block, dan alle ranges checken
    blockNr = 1
    while blockNr < 8:
        i = 0
        while i < len(seedRanges):
            if seedRanges[i][1] == -1:
                pass
            if blockNr == 1:
                if i == 9:
                    pass
            lines = blocks[blockNr].split('\n')
            for line in lines: 
                numbers = line.split(' ')
                if len(numbers) == 3:
                    #dest, Source, length
                    dest = int(numbers[0])
                    src = int(numbers[1])
                    length = int(numbers[2])
                    if seedRanges[i][0] >= src+length: #If lower number is over eind of range
                        #Its outside, do nothing
                        pass
                    else:
                        if seedRanges[i][0] >= src: #if lowest is inside range
                            if seedRanges[i][1] < src+length: #if highest is inside range
                                #complete inside, modify range to 
                                pass
                                seedRanges[i] =(seedRanges[i][0]+dest-src,seedRanges[i][1]+dest-src)
                                if seedRanges[i][1] == -1:
                                    pass
                                break
                            else:
                                #Not completely inside. cut range, and add to seeddRanges
                                seedRanges.append((src+length,seedRanges[i][1]))
                                seedRanges[i] =(seedRanges[i][0]+dest-src,src+length-1+dest-src)
                                if seedRanges[i][1] == -1:
                                    pass
                                break
                        else: #lowest is not inside range
                            if seedRanges[i][1] <= src: #if under src, then its outside range
                                #do nothing, the numbers will not change.
                                pass
                            else:
                                if seedRanges[i][1] <= src+length: #but highes is inside
                                    #cut the range
                                    seedRanges.append((seedRanges[i][0],src-1))
                                    seedRanges[i] =(dest,seedRanges[i][1]+dest-src)
                                    if seedRanges[i][1] == -1:
                                        pass
                                    break
            i += 1
        blockNr += 1

    lowest = 1e10
    for _min,_max in seedRanges:
        if _min < lowest:
            lowest = _min
    return lowest

if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', p1())
    print("### p1 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    start_time = int(round(time() * 1000))
    print('part 2:', p2())
    print("### p2 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
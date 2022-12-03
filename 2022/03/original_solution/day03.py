from time import time


def part1(path):
    with open(path) as f:
        lines = f.readlines()
    sum = 0
    for line in lines:
        cleanLine = line.strip()
        deel1 = line[slice(int(len(cleanLine)/2))]
        deel2 = cleanLine.split(deel1)[1]

        sameList = []
        for char1 in deel1:
            alreadyUsed = False
            for char in sameList:
                if char1 == char:
                    alreadyUsed = True
            if not alreadyUsed:
                for char2 in deel2:
                    if char1 == char2:
                        prio = ord(char1)-38
                        if prio > 52:
                            prio = prio - 58
                        sameList.append(char1)
                        sum += prio
                        break
    return sum


def part2(path):
    with open(path) as f:
        lines = f.readlines()
    sum = 0
    for i in range(0, len(lines), 3):
        line1, line2, line3 = lines[i:i+3]
        line1 = line1.strip()
        line2 = line2.strip()
        line3 = line3.strip()
        sameList = []
        for char1 in line1:
            alreadyUsed = False
            for char in sameList:
                if char1 == char:
                    alreadyUsed = True
            if not alreadyUsed:
                for char2 in line2:
                    alreadyUsed = False
                    for char in sameList:
                        if char2 == char:
                            alreadyUsed = True
                    if not alreadyUsed:
                        if char1 == char2:
                            for char3 in line3:
                                if char2 == char3:
                                    prio = ord(char1)-38
                                    if prio > 52:
                                        prio = prio - 58
                                    sameList.append(char1)
                                    sum += prio
                                    break
    return sum


# Run when this script is not imported by another script(e.g. Unittest)
if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', part1("2022/03/inputs/input.txt"))
    print('part 2:', part2("2022/03/inputs/input.txt"))
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))

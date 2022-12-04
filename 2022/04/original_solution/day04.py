from time import time


def part1(path):
    with open(path) as f:
        lines = f.readlines()
    sum = 0
    for line in lines:
        cline = line.strip()
        deel1,deel2 = cline.split((","))
        range1Start,range1End = deel1.split("-")
        range1 = range(int(range1Start),int(range1End)+1)
        range2Start,range2End = deel2.split("-")
        range2 = range(int(range2Start),int(range2End)+1)
        setRange1 = set(range1)
        setRange2 = set(range2)
        if setRange1.issubset(setRange2):
            sum +=1
        elif setRange2.issubset(setRange1):
            sum +=1
    return sum


def part2(path):
    with open(path) as f:
        lines = f.readlines()
    sum = 0
    for line in lines:
        cline = line.strip()
        deel1,deel2 = cline.split((","))
        range1Start,range1End = deel1.split("-")
        range1 = range(int(range1Start),int(range1End)+1)
        range2Start,range2End = deel2.split("-")
        range2 = range(int(range2Start),int(range2End)+1)
        setRange1 = set(range1)
        setRange2 = set(range2)
        if len(setRange1.intersection(setRange2)) > 0:
            sum +=1


    return sum


# Run when this script is not imported by another script(e.g. Unittest)
if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', part1("2022/04/inputs/input.txt"))
    print('part 2:', part2("2022/04/inputs/input.txt"))
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))

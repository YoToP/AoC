from time import time
# Using sets to remove the loops.


def part1(path):
    with open(path) as f:
        lines = f.readlines()
    i = 25
    
    while i < len(lines):
        bFound = False
        for x in range(i-25,i):
            for y in range(i-25,i):
                if x != y:
                    sum = int(lines[x]) + int(lines[y])
                    if sum == int(lines[i]):
                        bFound = True
                        break
            if bFound:
                break
        if not bFound:
            return int(lines[i])
        i += 1
    return 0


def part2(path,toBeFound):
    with open(path) as f:
        lines = f.readlines()
    r = 0# rear
    f = 1# front
    runningSum = runningSum = int(lines[r])+int(lines[f])

    while f != r:
        if runningSum == toBeFound:
            smallest = int(lines[r])
            biggest = int(lines[r])
            for line in lines[r:f]:
                lineValue = int(line)
                if lineValue > biggest:
                    biggest = lineValue
                elif lineValue < smallest:
                    smallest = lineValue
            return biggest + smallest
        elif runningSum > toBeFound:
            runningSum -= int(lines[r]) #remove rear value from sum
            r += 1
        elif runningSum < toBeFound:
            f += 1
            runningSum += int(lines[f]) #add front value from sum
    return 0


# Run when this script is not imported by another script(e.g. Unittest)
if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', part1("2020/09/inputs/input.txt"))
    print('part 2:', part2("2020/09/inputs/input.txt",part1("2020/09/inputs/input.txt")))
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))

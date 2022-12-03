from time import time
# Using sets to remove the loops.


def part1(path):
    with open(path) as f:
        lines = f.readlines()
    sum = 0
    for line in lines:
        cleanLine = line.strip()
        start = int(len(cleanLine)/2)
        deel1 = set(cleanLine[slice(start)])
        deel2 = set(cleanLine[slice(start, start+start)])
        #always one in intersections so nood need for loop.
        prio = ord(deel1.intersection(deel2).pop())-38 #min 38 to get A from 65 to 27
        if prio > 52: #if higher than 52, then its lowercase
            prio = prio - 58#so correct the lowercase to a = 1
        sum += prio
    return sum


def part2(path):
    with open(path) as f:
        lines = f.readlines()
    sum = 0
    for i in range(0, len(lines), 3):#step of 3
        line1, line2, line3 = lines[i:i+3]
        line1 = set(line1.strip())
        line2 = set(line2.strip())
        line3 = set(line3.strip())
        #always one in intersections so nood need for loop.
        prio = ord(line1.intersection(line2).intersection(line3).pop())-38#min 38 to get A from 65 to 27
        if prio > 52:#if higher than 52, then its lowercase
            prio = prio - 58#so correct the lowercase to a = 1
        sum += prio
    return sum


# Run when this script is not imported by another script(e.g. Unittest)
if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', part1("2022/03/inputs/input.txt"))
    print('part 2:', part2("2022/03/inputs/input.txt"))
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))

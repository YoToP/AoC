from time import time
#no sets
def part1(path):
    with open(path) as f:
        lines = f.readlines()
    sum = 0
    for line in lines:
        deel1, deel2 = line.strip().split((","))
        a, b = deel1.split("-")
        x, y = deel2.split("-")
        if (int(a) <= int(x) <= int(b)) and (int(a) <= int(y) <= int(b)):
            sum += 1
        elif (int(x) <= int(a) <= int(y)) and (int(x) <= int(b) <= int(y)):
            sum += 1
    return sum

def part2(path):
    with open(path) as f:
        lines = f.readlines()
    sum = 0
    for line in lines:
        deel1, deel2 = line.strip().split((","))
        a, b = deel1.split("-")
        x, y = deel2.split("-")
        if int(b) >= int(x) and int(a) <= int(y):
            sum += 1
        elif int(y) >= int(a) and int(x) <= int(b):
            sum += 1
    return sum

# Run when this script is not imported by another script(e.g. Unittest)
if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', part1("2022/04/inputs/input.txt"))
    print('part 2:', part2("2022/04/inputs/input.txt"))
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
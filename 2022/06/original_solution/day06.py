from time import time
from collections import deque

def part1and2(path,distinctChars):
    with open(path) as f:
        data = f.read()
    charRow = deque()
    i = 0
    for char in data:
        if char in charRow:
            removedchar = charRow.popleft()
            while removedchar != char:
                removedchar = charRow.popleft()
            charRow.append(char)
            i +=1
        else:
            charRow.append(char)
            i +=1
            if len(charRow) == distinctChars:
                return i
    return 0

if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', part1and2("2022/06/inputs/input.txt",4))
    print('part 2:', part1and2("2022/06/inputs/input.txt",14))
    print("### total run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
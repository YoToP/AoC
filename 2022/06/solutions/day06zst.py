from time import time
from collections import deque
import zstandard as zstd

def readZST(path):
    with open(path, "rb") as f:
        data = f.read()
    dctx = zstd.ZstdDecompressor(max_window_size=2**31)
    return dctx.decompress(data,max_output_size=2**31)

def part1and2(path,distinctChars):
    #with open(path) as f:
    #    data = f.read()
    data = readZST(path)
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
    PerInputTime = start_time
    path = "2022/06/inputs/aoc22d6l.txt.zst"
    print('part 1:', part1and2(path,4))
    print('part 2:', part1and2(path,14))
    print(f"### input: {path} run time is {(int(round(time() * 1000)) - PerInputTime)} miliseconds")
    
    PerInputTime = int(round(time() * 1000))
    path = "2022/06/inputs/aoc22d6xl.txt.zst"
    print('part 1:', part1and2(path,4))
    print('part 2:', part1and2(path,14))
    print(f"### input: {path} run time is {(int(round(time() * 1000)) - PerInputTime)} miliseconds")

    PerInputTime = int(round(time() * 1000))
    path = "2022/06/inputs/aoc22d6xxl.txt.zst"
    print('part 1:', part1and2(path,4))
    print('part 2:', part1and2(path,14))
    print(f"### input: {path} run time is {(int(round(time() * 1000)) - PerInputTime)} miliseconds")
    
    print(f"### total run time is {(int(round(time() * 1000)) - start_time)} miliseconds")
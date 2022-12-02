with open("2022/01/inputs/input.txt") as f:
    lines = f.readlines()
high = 0
nr2 = 0
nr3 = 0
temp = 0
debug = 0
for line in lines:
    cleanline = line.strip()
    if cleanline == "":
        if temp > high:
            _t =high
            high = temp
            temp = _t
        if temp > nr2:
            _t =nr2
            nr2 = temp
            temp = _t
        if temp > nr3:
            nr3 = temp
            temp = 0
        temp = 0
    else:
        temp = temp + int(cleanline)

sum = high + nr2 + nr3
print(sum)
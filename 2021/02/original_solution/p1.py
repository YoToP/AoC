with open("2/input.txt") as f:
    lines = f.readlines()
depth = 0
hor = 0
for line in lines:
    lineElements = line.split(" ")
    if lineElements[0] == "forward":
        hor = hor + int(lineElements[1])
    elif lineElements[0] == "up":
        depth = depth - int(lineElements[1])
    elif lineElements[0] == "down":
        depth = depth + int(lineElements[1])
print(str(depth)+" * "+str(hor))
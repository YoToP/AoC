with open("1/input.txt") as f:
    lines = f.readlines()
count = 0
for i in range(len(lines)):
    if i > 0: # check when there is something to check
        if int(lines[i]) > int(lines[i-1]):
            count = count + 1
print(count)
with open("1/input.txt") as f:
    lines = f.readlines()
count = 0
for i in range(len(lines)):
    if i > 2: # check when there is something to check
        if int(lines[i]) > int(lines[i-3]): # a + b + c > b + c + d is hetzelfde als a > d
            count = count + 1
print(count)
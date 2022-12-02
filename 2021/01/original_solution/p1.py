with open("1/input.txt") as f:
    lines = f.readlines()
last = 1000000
count = 0
for line in lines:
    if int(line) > last:
        count = count + 1
        print("Last:",last,", New: ",int(line))
    last = int(line)
print(count)
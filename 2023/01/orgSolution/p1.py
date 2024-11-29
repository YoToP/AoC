with open("2023/01/inputs/input.txt") as f:
    lines = f.readlines()
total = 0
for line in lines:
    line = line.strip()
    s = ''
    x = 0
    while x < len(line):
        test = line[x]
        if line[x].isdigit():
            s = s + line[x]
        else:
            if line[x] == 'o':
                if line[x:x+3] == 'one':
                    s = s + '1'
            elif line[x] == 't':
                if line[x:x+3] == 'two':
                    s = s + '2'
                elif line[x:x+5] == 'three':
                    s = s + '3'
            elif line[x] == 'f':
                if line[x:x+4] == 'four':
                    s = s + '4'
                elif line[x:x+4] == 'five':
                    s = s + '5'
            elif line[x] == 's':
                if line[x:x+3] == 'six':
                    s = s + '6'
                elif line[x:x+5] == 'seven':
                    s = s + '7'
            elif line[x] == 'e':
                sstring = line[x:x+5]
                if line[x:x+5] == 'eight':
                    s = s + '8'
            elif line[x] == 'n':
                if line[x:x+4] == 'nine':
                    s = s + '9'
        x = x +1

    #s = ''.join(x for x in line if x.isdigit())
    if len(s) == 1:
        total = total + int(s+s)
    elif len(s) == 2:
        total = total + int(s)
    else:
       total = total + int(s[0]+s[len(s)-1])


print(total)
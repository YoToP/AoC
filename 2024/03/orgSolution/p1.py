from time import time

def p1():
    with open("2024/03/inputs/input.txt") as f:
        score = 0
        for line in f.readlines():
            i = line.find('mul(')
            while i >= 0:
                debugString = "mul("
                i += 4 #cursor to next char
                valid = True
                #search first number
                startIndex = i
                while line[i].isdigit():
                    i += 1
                if startIndex == i: #no digits found
                    i = line.find('mul(',i+1)
                    continue
                debugString += line[startIndex:i] # DEBUG
                x1 = int(line[startIndex:i])
                #search comma
                debugString += line[i] # DEBUG
                if line[i] != ',':
                    i = line.find('mul(',i+1)
                    continue
                i += 1
                # search second nr
                startIndex = i
                while line[i].isdigit():
                    i += 1
                if startIndex == i: #no digits found
                    i = line.find('mul(',i+1)
                    continue
                debugString += line[startIndex:i] # DEBUG
                x2 = int(line[startIndex:i])
                #search closing bracket
                debugString += line[i] # DEBUG
                if line[i] != ')':
                    i = line.find('mul(',i+1)
                    continue
                #multiply and add to score
                score += x1 * x2

                i = line.find('mul(',i+1)
    return score

def p2():
    with open("2024/03/inputs/input.txt") as f:
        do = True
        score = 0
        for line in f.readlines():
            i = 0
            while i < len(line):
                if line[i:i+2] == 'do':
                    i += 2 #next part
                    if line[i:i+2] == '()': #do path
                        i += 2 #forward i
                        do = True
                        continue
                    elif line[i:i+5] == "n't()":
                        i += 5 #forward i
                        do = False
                        continue
                    else:
                        continue
                elif line[i:i+4] == 'mul(':
                    i += 4
                    if do:
                        #search first number
                        startIndex = i
                        while line[i].isdigit():
                            i += 1
                        if startIndex == i: #no digits found
                            continue
                        x1 = int(line[startIndex:i])
                        
                        #search comma
                        if line[i] != ',':
                            continue
                        i += 1

                        # search second nr
                        startIndex = i
                        while line[i].isdigit():
                            i += 1
                        if startIndex == i: #no digits found
                            continue
                        x2 = int(line[startIndex:i])
                        
                        #search closing bracket
                        if line[i] != ')':
                            continue
                        #multiply and add to score
                        score += x1 * x2

                        i += 1
                else:
                    i += 1
    return score


def p2_():
    with open("2024/03/inputs/input.txt") as f:
        do = True
        score = 0
        for line in f.readlines():

            
            i = iMul
            while i >= 0:
                i += 4 #cursor to next char
                valid = True
                #search first number
                startIndex = i
                while line[i].isdigit():
                    i += 1
                if startIndex == i: #no digits found
                    i = line.find('mul(',i+1)
                    continue
                x1 = int(line[startIndex:i])
                #search comma
                if line[i] != ',':
                    i = line.find('mul(',i+1)
                    continue
                i += 1
                # search second nr
                startIndex = i
                while line[i].isdigit():
                    i += 1
                if startIndex == i: #no digits found
                    i = line.find('mul(',i+1)
                    continue
                x2 = int(line[startIndex:i])
                #search closing bracket
                if line[i] != ')':
                    i = line.find('mul(',i+1)
                    continue
                #multiply and add to score
                score += x1 * x2

                i = line.find('mul(',i+1)
    return score

if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', p1())
    print("### p1 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    start_time = int(round(time() * 1000))
    print('part 2:', p2())
    print("### p2 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
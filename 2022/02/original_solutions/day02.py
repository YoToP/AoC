def p1():
    with open("2022/02/inputs/input.txt") as f:
        lines = f.readlines()
    score = 0
    for line in lines:
        cleanLine = line.strip()
        i, j = cleanLine.split(" ")

        if i == 'A':
            if j == 'X':
                score += 4
            elif j == 'Y':
                score += 8
            else:
                score += 3
        elif i == 'B':
            if j == 'X':
                score += 1
            elif j == 'Y':
                score += 5
            else:
                score += 9
        elif i == 'C':
            if j == 'X':
                score += 7
            elif j == 'Y':
                score += 2
            else:
                score += 6
    return score


def p2():
    with open("2022/02/inputs/input.txt") as f:
        lines = f.readlines()
    score = 0
    for line in lines:
        cleanLine = line.strip()
        i, j = cleanLine.split(" ")
        if i == 'A':
            if j == 'X':
                score += 3
            elif j == 'Y':
                score += 4
            else:
                score += 8
        elif i == 'B':
            if j == 'X':
                score += 1
            elif j == 'Y':
                score += 5
            else:
                score += 9
        elif i == 'C':
            if j == 'X':
                score += 2
            elif j == 'Y':
                score += 6
            else:
                score += 7
    return score


# Run when this script is not imported by another script(e.g. Unittest)
if __name__ == '__main__':
    print(f"part 1: {p1()}")
    print(f"part 2: {p2()}")

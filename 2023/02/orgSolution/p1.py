def p1():
    with open("2023/02/inputs/input.txt") as f:
        lines = f.readlines()
    score = 0
    for line in lines:
        cleanLine = line.strip()
        gameNr, j = cleanLine.split(": ")
        gameNr = int(gameNr.split(" ")[1])
        setCorrect = 1
        sets = j.split("; ")
        for _set in sets:
            redCount = 0
            blueCount = 0
            greenCount = 0
            
            pairs = _set.split(", ")
            for pair in pairs:
                nr, color = pair.split(" ")
                if color == "red":
                    redCount = redCount + int(nr)
                elif color == "blue":
                    blueCount = blueCount + int(nr)
                elif color == "green":
                    greenCount = greenCount + int(nr)
                else:
                    print(f"error codes: {cube}")
            if redCount > 12 or greenCount > 13 or blueCount > 14:
                setCorrect = 0
        if setCorrect == 1:
            score = score + gameNr
            
    return score


def p2():
    with open("2023/02/inputs/input.txt") as f:
        lines = f.readlines()
    score = 0
    for line in lines:
        cleanLine = line.strip()
        gameNr, j = cleanLine.split(": ")
        gameNr = int(gameNr.split(" ")[1])
        setCorrect = 1
        sets = j.split("; ")
        redLow = 0
        blueLow = 0
        greenLow = 0
        for _set in sets:
            redCount = 0
            blueCount = 0
            greenCount = 0
            
            pairs = _set.split(", ")
            for pair in pairs:
                nr, color = pair.split(" ")
                if color == "red":
                    redCount = redCount + int(nr)
                elif color == "blue":
                    blueCount = blueCount + int(nr)
                elif color == "green":
                    greenCount = greenCount + int(nr)
                else:
                    print(f"error codes: {cube}")
            if redCount > 0 and redCount > redLow:
                redLow = redCount
            if blueCount > 0 and blueCount > blueLow:
                blueLow = blueCount
            if greenCount > 0 and greenCount > greenLow:
                greenLow = greenCount
        score = score + redLow * blueLow * greenLow
    return score


# Run when this script is not imported by another script(e.g. Unittest)
if __name__ == '__main__':
    print(f"part 1: {p1()}")
    print(f"part 2: {p2()}")
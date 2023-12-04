from collections import defaultdict
def p1():
    with open("2023/04/inputs/input.txt") as f:
        lines = f.readlines()
    score = 0
    AMOUNT_WIN_NUMBERS = 10
    for line in lines:
        line = line.strip()
        _, numbers = line.split(":")
        winning, mynumbers = numbers.split(" | ")
        winset = set()
        for winNr in winning.split(" "):
            if winNr.isdigit():
                winset.add(int(winNr))
        AMOUNT_WIN_NUMBERS = len(winset)
        amount_play_numbers = 0
        for winNr in mynumbers.split(" "):
            if winNr.isdigit():
                winset.add(int(winNr))
                amount_play_numbers += 1

        if len(winset) < AMOUNT_WIN_NUMBERS+amount_play_numbers:
            amountWinning = AMOUNT_WIN_NUMBERS+amount_play_numbers-len(winset)
            score += 2**(amountWinning-1)
        else:
            pass
    return score


def p2(): 
    with open("2023/04/inputs/input.txt") as f:
        lines = f.readlines()
    score = 0
    AMOUNT_WIN_NUMBERS = 10
    def InitDict():
        return 1
    cardCounterDict = defaultdict(InitDict)
    cardnr = 0
    for line in lines:
        line = line.strip()
        _, numbers = line.split(":")
        cardnr += 1
        winning, mynumbers = numbers.split(" | ")
        winset = set()
        for winNr in winning.split(" "):
            if winNr.isdigit():
                winset.add(int(winNr))
        AMOUNT_WIN_NUMBERS = len(winset)
        amount_play_numbers = 0
        for winNr in mynumbers.split(" "):
            if winNr.isdigit():
                winset.add(int(winNr))
                amount_play_numbers += 1

        if len(winset) < AMOUNT_WIN_NUMBERS+amount_play_numbers:
            amountWinning = AMOUNT_WIN_NUMBERS+amount_play_numbers-len(winset)
            for i in range(1,amountWinning+1):
                cardCounterDict[i+cardnr] += 1 * cardCounterDict[cardnr]
        else:
            pass
        cardCounterDict[cardnr] = cardCounterDict[cardnr]
    for k,v in cardCounterDict.items():
        score+= v
    return score

if __name__ == '__main__':
    print(f"part 1: {p1()}")
    print(f"part 2: {p2()}")
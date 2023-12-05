from collections import defaultdict
def p1():
    with open("2023/05/inputs/example.txt") as f:
        blocks = f.read().split('\n\n')
    
    seeds = blocks[0].split(": ")[1].split(' ')
    seedToSoilDict = defaultdict(int)
    for seed in seeds:
        seedToSoilDict[int(seed)]
    lines = blocks[1].split('\n')
    for line in lines: #seed-to-soil map:
        numbers = line.split(' ')
        if len(numbers) == 3:
            #dest, Source, length
            src = int(numbers[1])
            dest = int(numbers[0])
            length = int(numbers[2])
            for i in range(src,src+length+1):
                seedToSoilDict[i] = dest+i

    #soil-to-fertilizer map:
    soilToFertDict = defaultdict(int)
    lines = blocks[2].split('\n')
    for line in lines: 
        numbers = line.split(' ')
        if len(numbers) == 3:
            #dest, Source, length
            src = int(numbers[1])
            dest = int(numbers[0])
            length = int(numbers[2])
            for i in range(src,src+length+1):
                soilToFertDict[i] = dest+i
    #fertilizer-to-water map:
    fertToWaterDict = defaultdict(int)
    lines = blocks[3].split('\n')
    for line in lines: 
        numbers = line.split(' ')
        if len(numbers) == 3:
            #dest, Source, length
            src = int(numbers[1])
            dest = int(numbers[0])
            length = int(numbers[2])
            for i in range(src,src+length+1):
                fertToWaterDict[i] = dest+i

#water-to-light map:
    waterToLightDict = defaultdict(int)
    lines = blocks[4].split('\n')
    for line in lines: 
        numbers = line.split(' ')
        if len(numbers) == 3:
            #dest, Source, length
            src = int(numbers[1])
            dest = int(numbers[0])
            length = int(numbers[2])
            for i in range(src,src+length+1):
                waterToLightDict[i] = dest+i

#light-to-temperature map:
    lightToTempDict = defaultdict(int)
    lines = blocks[5].split('\n')
    for line in lines: 
        numbers = line.split(' ')
        if len(numbers) == 3:
            #dest, Source, length
            src = int(numbers[1])
            dest = int(numbers[0])
            length = int(numbers[2])
            for i in range(src,src+length+1):
                lightToTempDict[i] = dest+i
#temperature-to-humidity map:
    tempToHumidDict = defaultdict(int)
    lines = blocks[6].split('\n')
    for line in lines: 
        numbers = line.split(' ')
        if len(numbers) == 3:
            #dest, Source, length
            src = int(numbers[1])
            dest = int(numbers[0])
            length = int(numbers[2])
            for i in range(src,src+length+1):
                tempToHumidDict[i] = dest+i
#humidity-to-location map:
    humidToLocDict = defaultdict(int)
    lines = blocks[7].split('\n')
    for line in lines: 
        numbers = line.split(' ')
        if len(numbers) == 3:
            #dest, Source, length
            src = int(numbers[1])
            dest = int(numbers[0])
            length = int(numbers[2])
            for i in range(src,src+length+1):
                humidToLocDict[i] = dest+i
    score = 0
    return score


def p2(): 
    with open("2023/04/inputs/input.txt") as f:
        lines = f.readlines()
    cardCounterDict = defaultdict(lambda: 1)
    cardnr = 0
    for line in lines:
        _, numbers = line.strip().split(":")
        cardnr += 1
        winning, mynumbers = numbers.split(" | ")
        winset = set()
        for winNr in winning.split(" "):
            if winNr.isdigit():
                winset.add(int(winNr))
        amountWinningNumbers = len(winset)
        amountPlayNumbers = 0
        for winNr in mynumbers.split(" "):
            if winNr.isdigit():
                winset.add(int(winNr))
                amountPlayNumbers += 1

        if len(winset) < amountWinningNumbers+amountPlayNumbers: #only calc when at least 1 number is a winning number
            amountWinning = amountWinningNumbers+amountPlayNumbers-len(winset)
            for i in range(1,amountWinning+1):
                cardCounterDict[i+cardnr] += 1 * cardCounterDict[cardnr]
        else:
            cardCounterDict[cardnr] #make sure to add the last one to the Dict
        
    score = 0
    for k,v in cardCounterDict.items():
        score+= v
    return score

if __name__ == '__main__':
    print(f"part 1: {p1()}")
    #print(f"part 2: {p2()}")
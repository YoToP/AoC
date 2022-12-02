#DIKKE FAAL
with open("1\\input.txt") as f:
    lines = f.readlines()
last = 1000000
count = 0
ACount = 0
ATotal = 0
BCount = -1
BTotal = 0
CCount = -2
CTotal = 0
DCount = -3
DTotal = 0
breakcount = 0
for line in lines:    
    #D
    if 0 <= DCount < 3:
        DTotal = DTotal + int(line)
    if DCount == 2:
        if CTotal > 0:
            print("D check "+ str(DTotal)+" > "+ str(CTotal))
            if DTotal > CTotal:
                count = count + 1
    if DCount == 3:
        DTotal = 0
    if DCount == 4:
        DCount = 0
    DCount = DCount + 1

    #C
    if 0 <= CCount < 3:
        CTotal = CTotal + int(line)
    if CCount == 2:
        if BTotal > 0:
            print("C check "+ str(CTotal)+" > "+ str(BTotal))
            if CTotal > BTotal:
                count = count + 1
    if CCount == 3:
        CTotal = 0
    if CCount == 4:
        CCount = 0
    CCount = CCount + 1

    #B
    if 0 <= BCount < 3:
        BTotal = BTotal + int(line)
    if BCount == 2:
        if ATotal > 0:
            print("B check "+ str(BTotal)+" > "+ str(ATotal))
            if BTotal > ATotal:
                count = count + 1
    if BCount == 3:
        BTotal = 0
    if BCount == 4:
        BCount = 0
    BCount = BCount + 1

    #A
    if 0 <= ACount < 3:
        ATotal = ATotal + int(line)
    if ACount == 2:
        if DTotal > 0:
            print("A check "+ str(ATotal)+" > "+ str(DTotal))
            if ATotal > DTotal:
                count = count + 1
    if ACount == 3:
        ATotal = 0
    if ACount == 4:
        ACount = 0
    ACount = ACount + 1
    breakcount = breakcount + 1
    if breakcount > 20:
        break
    #print(". A: "+str(ACount)+". B: "+str(BCount)+". C: "+str(CCount)+". D: "+str(DCount))

print(count)
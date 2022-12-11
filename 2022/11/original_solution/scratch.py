
for x in range(53,1007,19):
    checkValue = (x-5+11)
    if checkValue %17 == 10:
        checkValue = checkValue - 8
        if checkValue % 11 == 4:
            print(x)
            break
exit()
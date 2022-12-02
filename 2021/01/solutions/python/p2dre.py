#Diederik van der Rhee
import os
inputFile = os.path.normpath(r"1\\input.txt")
file = open(inputFile, 'r')
Lines = file.readlines()
counter = 0
windowSize = 3
for i in range (0, len(Lines)):
    if (i + 3 < len(Lines)):
        current = 0
        next = 0
        for j in range (0, windowSize):
            current = current + int(Lines[i+j])
            next = next + int(Lines[i+j+1])
            if (next > current):
                counter = counter + 1

print (counter)
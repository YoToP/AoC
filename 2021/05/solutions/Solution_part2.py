import os

import pandas as pd

inputFile = os.path.normpath(r"5/example1.txt")

df = pd.read_csv(inputFile, sep='[, ]', header=None)

x1 = []
y1 = []
x2 = []
y2 = []

for i in range (0, len(df)):
    row = df.iloc[i]
    x1.append(int(row[0]))
    y1.append(int(row[1]))
    x2.append(int(row[3]))
    y2.append(int(row[4]))
        
maxX = max(max(x1), max(x2))
maxY = max(max(y1), max(y2))


lines = [[0 for i in range(maxX + 1)] for j in range(maxY + 1)]

for i in range (0, len(x1)):
    xDif = abs(x1[i] - x2[i])
    yDif = abs(y1[i] - y2[i])
    
    if (x1[i] == x2[i] == y1[i] == y2[i]):
        print ("All the same!")
    elif (x1[i] == x2[i] and y1[i] == y2[i]):
        print ("Two the same points")
        
    if (x1[i] == x2[i]):
        #common x values
        x = x1[i]
        yStart = y1[i]
        yEnd = y2[i]
        if (yStart > yEnd):
            yTemp = yStart
            yStart = yEnd
            yEnd = yTemp
        for y in range (yStart, yEnd + 1):
            lines[x][y] = lines[x][y] + 1
        #raise Exception('1')
    elif (y1[i] == y2[i]):
        #common y values
        y = y1[i]
        xStart = x1[i]
        xEnd = x2[i]
        if (xStart > xEnd):
            xTemp = xStart
            xStart = xEnd
            xEnd = xTemp
        for x in range (xStart, xEnd + 1):
            lines[x][y] = lines[x][y] + 1
    elif (xDif == yDif and xDif > 0):
      xDif = abs(x1[i] - x2[i])
      yDif = abs(y1[i] - y2[i])
      
      xStart = x1[i]
      yStart = y1[i]
      
      xDirection = 1
      if (x1[i] > x2[i]):
          xDirection = -1

      yDirection = 1
      if (y1[i] > y2[i]):
          yDirection = -1
          
      for q in range (0, xDif + 1):
          x = xStart + (q* xDirection)
          y = yStart + (q * yDirection)
          lines[x][y] = lines[x][y] + 1
      
        
        
counter = 0
for x in range (0, maxX + 1):
    for y in range (0, maxY + 1):
        if (lines[x][y] >= 2):
            counter = counter + 1
print (counter)


#for y in range (0, maxY + 1):
#    rowString = ""
#    for x in range (0, maxX + 1):
#        value = lines[x][y]
#        if (value == 0):
#            rowString += "."
#        else:
#            rowString += str(value)
#    print (rowString)
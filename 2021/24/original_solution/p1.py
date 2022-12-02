from time import time

def eql(arg1,arg2):
    global w,x,y,z
    if arg1 == 'w':
        if arg2 == 'w':
            if w == w:
                w = 1
            else:
                w = 0
        elif arg2 == 'x':
            if w == x:
                w = 1
            else:
                w = 0
        elif arg2 == 'y':
            if w == y:
                w = 1
            else:
                w = 0
        elif arg2 == 'z':
            if w == z:
                w = 1
            else:
                w = 0
        else:
            if w == int(arg2):
                w = 1
            else:
                w = 0
    elif arg1 == 'x':
        if arg2 == 'w':
            if x == w:
                x = 1
            else:
                x = 0
        elif arg2 == 'x':
            if x == x:
                x = 1
            else:
                x = 0
        elif arg2 == 'y':
            if x == y:
                x = 1
            else:
                x = 0
        elif arg2 == 'z':
            if x == z:
                x = 1
            else:
                x = 0
        else:
            if x == int(arg2):
                x = 1
            else:
                x = 0
    elif arg1 == 'y':
        if arg2 == 'w':
            if y == w:
                y = 1
            else:
                y = 0
        elif arg2 == 'x':
            if y == x:
                y = 1
            else:
                y = 0
        elif arg2 == 'y':
            if y == y:
                y = 1
            else:
                y = 0
        elif arg2 == 'z':
            if y == z:
                y = 1
            else:
                y = 0
        else:
            if y == int(arg2):
                y = 1
            else:
                y = 0
    elif arg1 == 'z':
        if arg2 == 'w':
            if z == w:
                z = 1
            else:
                z = 0
        elif arg2 == 'x':
            if z == x:
                z = 1
            else:
                z = 0
        elif arg2 == 'y':
            if z == y:
                z = 1
            else:
                z = 0
        elif arg2 == 'z':
            if z == z:
                z = 1
            else:
                z = 0
        else:
            if z == int(arg2):
                z = 1
            else:
                z = 0

def mod(arg1,arg2):
    global w,x,y,z
    if arg1 == 'w':
        if arg2 == 'w':
            w = w % w
        elif arg2 == 'x':
            w = w % x
        elif arg2 == 'y':
            w = w % y
        elif arg2 == 'z':
            w = w % z
        else:
            w = w % int(arg2)
    elif arg1 == 'x':
        if arg2 == 'w':
            x = x % w
        elif arg2 == 'x':
            x = x % x
        elif arg2 == 'y':
            x = x % y
        elif arg2 == 'z':
            x = x % z
        else:
            x = x % int(arg2)
    elif arg1 == 'y':
        if arg2 == 'w':
            y = y % w
        elif arg2 == 'x':
            y = y % x
        elif arg2 == 'y':
            y = y % y
        elif arg2 == 'z':
            y = y % z
        else:
            y = y % int(arg2)
    elif arg1 == 'z':
        if arg2 == 'w':
            z = z % w
        elif arg2 == 'x':
            z = z % x
        elif arg2 == 'y':
            z = z % y
        elif arg2 == 'z':
            z = z % z
        else:
            z = z % int(arg2)

def div(arg1,arg2):
    global w,x,y,z
    if arg1 == 'w':
        if arg2 == 'w':
            w = round(w / w)
        elif arg2 == 'x':
            w = round(w / x)
        elif arg2 == 'y':
            w = round(w / y)
        elif arg2 == 'z':
            w = round(w / z)
        else:
            w = round(w / int(arg2))
    elif arg1 == 'x':
        if arg2 == 'w':
            x = round(x / w)
        elif arg2 == 'x':
            x = round(x / x)
        elif arg2 == 'y':
            x = round(x / y)
        elif arg2 == 'z':
            x = round(x / z)
        else:
            x = round(x / int(arg2))
    elif arg1 == 'y':
        if arg2 == 'w':
            y = round(y / w)
        elif arg2 == 'x':
            y = round(y / x)
        elif arg2 == 'y':
            y = round(y / y)
        elif arg2 == 'z':
            y = round(y / z)
        else:
            y = round(y / int(arg2))
    elif arg1 == 'z':
        if arg2 == 'w':
            z = round(z / w)
        elif arg2 == 'x':
            z = round(z / x)
        elif arg2 == 'y':
            z = round(z / y)
        elif arg2 == 'z':
            z = round(z / z)
        else:
            try:
                z = round(z / int(arg2))
            except:
                global errorFlag
                errorFlag = True
                global reason
                reason = "Division error"


def mul(arg1,arg2):
    global w,x,y,z
    if arg1 == 'w':
        if arg2 == 'w':
            w = w * w
        elif arg2 == 'x':
            w = w * x
        elif arg2 == 'y':
            w = w * y
        elif arg2 == 'z':
            w = w * z
        else:
            w = w * int(arg2)
    elif arg1 == 'x':
        if arg2 == 'w':
            x = x * w
        elif arg2 == 'x':
            x = x * x
        elif arg2 == 'y':
            x = x * y
        elif arg2 == 'z':
            x = x * z
        else:
            x = x * int(arg2)
    elif arg1 == 'y':
        if arg2 == 'w':
            y = y * w
        elif arg2 == 'x':
            y = y * x
        elif arg2 == 'y':
            y = y * y
        elif arg2 == 'z':
            y = y * z
        else:
            y = y * int(arg2)
    elif arg1 == 'z':
        if arg2 == 'w':
            z = z * w
        elif arg2 == 'x':
            z = z * x
        elif arg2 == 'y':
            z = z * y
        elif arg2 == 'z':
            z = z * z
        else:
            z = z * int(arg2)

def add(arg1,arg2):
    global w,x,y,z
    if arg1 == 'w':
        if arg2 == 'w':
            w = w + w
        elif arg2 == 'x':
            w = w + x
        elif arg2 == 'y':
            w = w + y
        elif arg2 == 'z':
            w = w + z
        else:
            w = w + int(arg2)
    elif arg1 == 'x':
        if arg2 == 'w':
            x = x + w
        elif arg2 == 'x':
            x = x + x
        elif arg2 == 'y':
            x = x + y
        elif arg2 == 'z':
            x = x + z
        else:
            x = x + int(arg2)
    elif arg1 == 'y':
        if arg2 == 'w':
            y = y + w
        elif arg2 == 'x':
            y = y + x
        elif arg2 == 'y':
            y = y + y
        elif arg2 == 'z':
            y = y + z
        else:
            y = y + int(arg2)
    elif arg1 == 'z':
        if arg2 == 'w':
            z = z + w
        elif arg2 == 'x':
            z = z + x
        elif arg2 == 'y':
            z = z + y
        elif arg2 == 'z':
            z = z + z
        else:
            z = z + int(arg2)

def getModelNrElement():
    global modelnr
    global modelnrPointer
    global linenr
    if modelnrPointer > len(modelnr):
        print(f"ALU WARNING: Too many INP operands. On line: {linenr}")
        return modelnr[len(modelnr)-1]
    else:
        nr = modelnr[modelnrPointer]
        modelnrPointer +=1
        return nr

def solvep1(path):
    global modelnr
    #op regel 91: 794 bij [1, 1, 5, 8, 1, 9, 9, 9, 9, 9, 9, 1, 1, 8] laagste
    modelnr = [1,1,5,6,9,9,9,1,7,9,7,9,9,9]
    #modelnr = [1,1,5,9,9,3,9,1,5,1,4,1,1,8] #uitkomst deel 1
    #modelnr = [9,9,9,9,9,9,9,9,9,1,4,1,1,8] #uitkomst laatste deel = 0
    #modelnr = [1,3,5,7,9,2,4,6,8,9,9,9,9,9]
    #modelnr = [1,1,1,1,1,1,1,1,1,1,1,1,1,9]
    global modelnrPointer
    modelnrPointer = 0
    global w,x,y,z
    w = 0
    x = 0
    y = 0
    z = 0
    tempmin =  99999999
    global errorFlag, reason
    errorFlag = False
    reason = "noerror"
    global linenr
    linenr = 0
    bFound = False
    with open(path) as f: lines = f.readlines()
    while not bFound:
        #print(f"Trying modelNr: {modelnr}")
        for line in lines:
            if errorFlag:
                print(reason)
                break
            linenr += 1
            strippedLine = line.split("#")[0].strip()
            if len(strippedLine) >0:
                if strippedLine[0] == 'i': #INP operation
                    ins, arg1 = strippedLine.split(" ")
                    if arg1 == 'w':
                        w = getModelNrElement()
                    elif arg1 == 'x':
                        x = getModelNrElement()
                    elif arg1 == 'y':
                        y = getModelNrElement()
                    elif arg1 == 'z':
                        z = getModelNrElement()
                else:
                    ins, arg1, arg2 = strippedLine.split(" ")
                    if ins == 'add':
                        add(arg1,arg2)
                    elif ins == 'mul':
                        mul(arg1, arg2)
                    elif ins == 'div':
                        div(arg1, arg2)
                    elif ins == 'mod':
                        mod(arg1, arg2)
                    elif ins == 'eql':
                        eql(arg1, arg2)
                    else:
                        print(f"ALU ERROR: Invalid Instruction found:{ins}")
            if linenr == 241:
                if x == 1:
                    print(f"op regel {linenr}: {z} bij {modelnr}")
                    exit()

            if linenr == 238:
                #print(z)
                if x <= 10:
                    #print(f"x:{x}")
                    #print(f"bij modelNr: {modelnr}")
                    pass
                pass
            if linenr == 247:
                pass
        errorFlag = True
        if z != 0 or errorFlag:
            errorFlag = False
            mindex = 13
            mindex = 13
            if modelnr[mindex] == 1:
                modelnr[mindex] = 9
                if modelnr[mindex-1] == 1:
                    modelnr[mindex-1] = 9
                    if modelnr[mindex-2] == 1:    
                        modelnr[mindex-2] = 9
                        if modelnr[mindex-3] == 1: 
                            modelnr[mindex-3] = 9
                            if modelnr[mindex-4] == 1: 
                                print(f"tempmin: {tempmin}")
                                return z
                            else:
                                modelnr[mindex-4]-=1
                        else:
                            modelnr[mindex-3]-=1
                    else:
                        modelnr[mindex-2] -=1
                else:
                    modelnr[mindex-1] -=1
            else:
                modelnr[mindex] -= 1
            modelnrPointer = 0
            w = 0
            x = 0
            y = 0
            z = 0
            linenr=0
        else:
            return z
    
    return z

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print('p1:',solvep1("24/input.txt"))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))
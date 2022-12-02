def solvep1(path,column):
    with open(path) as f:
        lines = f.readlines()
    #init
    s = []
    for i in range(column):
        s.append(0)
    #read lines
    for line in lines:
        for i in range(column):
            if line[i] == '0':
                s[i] = s[i] - 1
            if line[i] == '1':
                s[i] = s[i] + 1
            
            line.strip()

    #calculate gamma
    gamma = ""
    for getal in s:
        if getal > 0:
            gamma = gamma + '1'
        if getal < 0:
            gamma = gamma + '0'
        if getal == 0:
            print("WTF")
    GammaGetal = int(gamma,2)
    print("Gamma,",GammaGetal)
    
    epsilon = ""
    for getal in s:
        if getal > 0:
            epsilon = epsilon + '0'
        if getal < 0:
            epsilon = epsilon + '1'
        if getal == 0:
            print("WTF2")
    EpsilonGetal = int(epsilon,2)
    print("Epsilon,",EpsilonGetal)

    return GammaGetal * EpsilonGetal

if __name__ == '__main__':
    print(solvep1("3/input.txt",12))
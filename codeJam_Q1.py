numCases = int(input())
RC = ""
printing = ""
for i in range(numCases):
    RC = list(map(int, input().strip().split(" ")))
    R = int(RC[0])
    C = int(RC[1])
    firstR = ('.'*2 + ('+-'*(C-1)) + '+\n')
    secondR = ('.'*2 + ('|.'*(C-1)) + '|\n')    
    middleR = (('+-'*C + '+\n') + ('|.'*C + '|\n'))*(R-1)
    lastR = ('+-'*C + '+')
    matrix = "\n" + firstR + secondR + middleR + lastR
    print("Case #{}: {}".format(i+1,matrix))
numCases = int(input())
for i in range(numCases):
    p1 = list(map(int, input().strip().split(" ")))
    p2 = list(map(int, input().strip().split(" ")))
    p3 = list(map(int, input().strip().split(" ")))
    c = [p1[0], p2[0], p3[0]]
    m = [p1[1], p2[1], p3[1]]
    y = [p1[2], p2[2], p3[2]]
    k = [p1[3], p2[3], p3[3]]
    maxC = min(c) // 10**4
    maxM = min(m) // 10**4
    maxY = min(y) // 10**4
    maxK = min(k) // 10**4
    print(maxC + maxM + maxY + maxK)
    if (maxC + maxM + maxY + maxK) < 100:
        group = "IMPOSSIBLE"
    else:
        if maxC + maxM + maxY + maxK == 100:
            group = str(maxC * 10**4) + " " + str(maxM * 10**4) + " " + str(maxY * 10**4) + " " + str(maxK * 10**4)
        elif maxC + maxM + maxY + maxK > 100:
            maxC = maxC//2
            maxM = maxM//2
            maxY = maxY//2
            maxK = maxK//2            
            difference = maxC + maxM + maxY + maxK - 100
            setIs = False
            add = 0
            print(maxC, maxM, maxY, maxK)
            while setIs is False and difference > 0:
                if maxC - difference > 0:
                    maxC -= difference
                    setIs = True
                else:
                    if maxM - difference > 0:
                        maxM -= difference
                        setIs = True
                    else:
                        if maxY - difference > 0:
                            maxY -= difference
                            setIs = True
                        else:
                            if maxK - difference > 0:
                                maxK -= difference
                                setIs = True
                            else:
                                difference -= 1
                                add += 1
                                setIs = False
                if maxC + add < maxC*2:
                    maxC += add 
                    
            print(difference)
            print(add)
            group = str(round(maxC * 10**4)) + " " + str(round(maxM * 10**4)) + " " + str(round(maxY * 10**4)) + " " + str(round(maxK * 10**4))
    print("Case #{}: {}".format(i+1,group))
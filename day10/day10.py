def solve(data):
    data.sort()
    count1 =0
    count3 =1
    count2 =0
    maxVolt = max(data) + 3
    effectRate = 0
    for val in data:
        diff = val-effectRate
        effectRate= diff+effectRate
        if diff==1:
            count1+=1
            continue
        elif diff==2:
            count2+=1
            continue
        else:
            count3+=1
            continue

    return count1*count3


calc = {}

def part2(i,sortedData):
    global calc #global dict for memoization
    if i in calc: #checks for precomputed counts 
        return calc[i]
    elif sortedData[i] == sortedData[-1]: #max value reached (only 1 possible combination from here, will recurse backwards from here)
        calc[i] = 1
        return 1
    else:
        nextVals = [sortedData[i]+j for j in range(1,4)] 
        count = 0
        for j,val in enumerate(nextVals):
            if val in sortedData:
                count+=part2(sortedData.index(val),sortedData) #recursive call
        calc[i] = count
        return count





with open("day10.txt") as f:
    data = f.readlines()
    data = [int(dataval) for dataval in data]
    ans = solve(data)
    print("part 1" ,ans)
    data.insert(0,0)#start point
    data.sort()
    print("part 2", part2(0,data))
    print(calc)

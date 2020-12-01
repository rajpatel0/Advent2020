with open("day1.txt") as f:
    data = f.readlines()
    listofNums = [int(num) for num in data]
    listofNums.sort()
    i = 0
    j = len(listofNums) - 1
    while i<j:
        if listofNums[i]+listofNums[j]>2020:
            j-=1
        elif listofNums[i]+listofNums[j]<2020:
            i+=1
        else:
            print(listofNums[i],listofNums[j])
            print(listofNums[i]*listofNums[j])
            break



with open("day1.txt") as f:
    data = f.readlines()
    listofNums = [int(num) for num in data]
    listofNums.sort()
    listofNumsLength = len(listofNums)
    for i in range(listofNumsLength-2):
        j=i+1
        k=len(listofNums)-1
        while(j<k):
            if listofNums[i]+listofNums[j]+listofNums[k]>2020:
                k-=1
            elif listofNums[i]+listofNums[j]+listofNums[k]<2020:
                j+=1
            else:
                print(listofNums[i],listofNums[j],listofNums[k])
                print(listofNums[i]*listofNums[j]*listofNums[k])
                break




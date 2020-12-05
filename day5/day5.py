def solve(data):
    highestID = 0
    seatID = []
    
    for line in data:
        top = 128
        bot = 0
        initialString = line[0:7]
        restString = line[7:]
        for char in initialString:
            if char == "F":
                top=(top+bot)//2
            else: 
                bot=(bot+top)//2
        left = 0
        right = 8
        for char in restString:
            if (char == 'L'):
                right= (right+left)//2
            else:
                left = (left+right)//2

        Id =  bot*8 +left
        highestID = max(highestID,Id)
        seatID.append(Id)
    seatID.sort()

    for i in range(len(seatID)-1):
        if ((seatID[i+1]-seatID[i])==2): #if diff between seats is 2 theres a gap
            missingSeat = seatID[i]+1 #prints the missing seat aka my seat
            break

    return highestID,missingSeat
    
        




with open("day5.txt") as f:
    data = f.readlines()
    data = [dataval for dataval in data]
    part1,part2=solve(data)
    print(part1,part2)

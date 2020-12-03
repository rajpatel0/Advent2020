def solve(data,xchange,ychange):
    countTrees = 0
    currentposX = 0
    currentposY = 0
    while currentposY < len(data)-1:
        currentposX += xchange
        currentposY += ychange
        if currentposX >= len(data[0])-1:
            currentposX -= len(data[0])-1
        if data[currentposY][currentposX] == '#':
            countTrees +=1

    return countTrees
        




with open("day3.txt") as f:
    data = f.readlines()
    listofdata = [dataval for dataval in data]
    numvalid = solve(listofdata,1,1)
    numvalid2 = solve(listofdata,3,1)
    numvalid3 = solve(listofdata,5,1)
    numvalid4 = solve(listofdata,7,1)
    numvalid5 = solve(listofdata,1,2)

    print(numvalid*numvalid2*numvalid3*numvalid4*numvalid5)

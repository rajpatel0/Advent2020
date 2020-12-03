def solve(data):
    countTrees = 0
    currentposX = 0
    currentposY = 0
    while currentposY < len(data)-1:
        currentposX += 3
        currentposY += 1
        if currentposX >= len(data[0])-1:
            currentposX -= len(data[0])-1
        if data[currentposY][currentposX] == '#':
            countTrees +=1

    return countTrees
        




with open("day3.txt") as f:
    data = f.readlines()
    listofdata = [dataval for dataval in data]
    numvalid = solve(listofdata)
    print(numvalid)


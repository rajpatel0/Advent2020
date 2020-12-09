def solve(data):
    i = 0
    j = 24
    count = 0
    while j<len(data)+1:
        possibleVals=getPossibleValues(data[i:j+1])
        i+=1
        j+=1
        if data[j] not in possibleVals:
            return findEncryptionWeakness(data,data[j])
    return count

def getPossibleValues(data):
    listofPossibleVals = []
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            listofPossibleVals.append(data[i]+data[j])
    return listofPossibleVals

def findEncryptionWeakness(possibleVals,fakeVal):
    i=0
    j=1
    fakeValGuess = possibleVals[i] + possibleVals[j]
    while j<len(possibleVals):
        if fakeValGuess == fakeVal:
            break
        if fakeValGuess>fakeVal:
            print(fakeValGuess,fakeVal)
            i+=1
            j= i +1
            fakeValGuess = possibleVals[i]+possibleVals[j]
            continue
        j+=1
        fakeValGuess += possibleVals[j]
    return min(possibleVals[i:j+1])+max(possibleVals[i:j+1])


with open("day9.txt") as f:
    data = f.readlines()
    data = [int(dataval) for dataval in data]
    count = solve(data)
    print(count)


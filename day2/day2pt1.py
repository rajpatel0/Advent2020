def solve(data):
    count = 0
    for val in data:
        policy = val.split()
        policyMin,policyMax = policy[0].split('-')
        policyMin = int(policyMin)
        policyMax = int(policyMax)
        policyChar,useless = policy[1].split(":")
        countofChar = policy[2].count(policyChar)
        if countofChar>=policyMin and countofChar<=policyMax:
            count += 1
    return count
        




with open("day2.txt") as f:
    data = f.readlines()
    listofdata = [dataval for dataval in data]
    numvalid = solve(listofdata)
    print(numvalid)


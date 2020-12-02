def solve(data):
    count = 0
    for val in data:
        policy = val.split()
        policyMin,policyMax = policy[0].split('-')
        policyMin = int(policyMin)
        policyMax = int(policyMax)
        policyChar,useless = policy[1].split(":")
        stringToCheck = policy[2]

        if (stringToCheck[policyMin-1]==policyChar) ^ (stringToCheck[policyMax-1]==policyChar):
            count += 1
    return count
        




with open("day2.txt") as f:
    data = f.readlines()
    listofdata = [dataval for dataval in data]
    numvalid = solve(listofdata)
    print(numvalid)


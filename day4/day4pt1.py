def checkValidPassport(possiblePassport):
    possiblePassport = [value.replace('\n','') for value in possiblePassport]
    passportString = ' '.join(possiblePassport)
    thingsToCheck = ['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:']
    answer = 1
    print(passportString)
    for elem in thingsToCheck:
        if elem in passportString:
            continue
        answer = 0
        break

    return answer
    
        




with open("day4.txt") as f:
    data = f.readlines()
    passportValues = []
    count = 0
    for dataVal in data:
        passportValues.append(dataVal)
        if dataVal == '\n':
            count += checkValidPassport(passportValues)
            passportValues = []
    print(count)

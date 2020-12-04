def issueYear(year):
    year= int(year)
    if year>=2010 and year<=2020:
        return True
    return False

def exprYear(year):
    year = int(year)
    if year>=2020 and year <= 2030:
        return True
    return False

def height(ht):
    if ht[-1].isalpha():
        lengthHt = len(ht)
        heightNum = int(ht[0:lengthHt-2])
        heightUnit = ht[lengthHt-2:lengthHt]
        if heightUnit == 'in':
            if heightNum>=59 and heightNum <= 76:
                return True
        if heightUnit == 'cm':
            if heightNum>=150 and heightNum<=193:
                return True
        return False
    return False

def hairColor(hc):
    if hc[0] == '#' and hc[1:].isalnum():
        return True
    return False

def validBirthYear(year):
    year = int(year)
    if year>=1920 and year <=2002:
        return True
    return False
def validEyeColor(color):
    validColor = ['amb','blu','brn','gry','grn','hzl','oth']
    if color in validColor:
        return True
    return False

def validPassID(pid):
    if len(pid) == 9: 
        return True
    return False

def checkValidPassport(possiblePassport):
    possiblePassport = [value.replace('\n','') for value in possiblePassport]
    passportString = ' '.join(possiblePassport)
    passportList = passportString.split(' ')
    thingsToCheckList = [elem.split(':') for elem in passportList]
    thingsToCheckList.pop(-1)
    answer = 0
    if len(thingsToCheckList)>=7:
        for elem in thingsToCheckList:
            if elem[0] == 'cid' and len(thingsToCheckList) == 7:
                return 0
            if elem[0] == 'byr':
                if validBirthYear(elem[1]):
                    continue
                else:
                    return 0
            if elem[0] == 'iyr':
                if issueYear(elem[1]):
                    continue
                else:
                    return 0 
            if elem[0] == 'eyr':
                if exprYear(elem[1]):
                    continue
                else:
                    return 0
            if elem[0] == 'hgt':
                if height(elem[1]):
                    continue
                else:
                    return 0
            if elem[0] == 'hcl':
                if hairColor(elem[1]):
                    continue
                else:
                    return 0
            if elem[0] == 'ecl':
                if validEyeColor(elem[1]):
                    continue
                else:
                    return 0 
            if elem[0] == 'pid':
                if validPassID(elem[1]):
                    continue
                else:
                    return 0 
        answer = 1

        

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

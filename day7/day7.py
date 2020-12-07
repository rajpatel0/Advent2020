def solve(data):
    count = 0
    bagDict = {} 
    goldHoldingBags = set()
    emptyBags = set()
    for line in data: 
        lineData=line.split('contain') 
        bag = lineData[0] 
        bag = bag.strip()
        bag = bag[0:len(bag)-1]
        bagDict[bag] = []
        restBags = ' '.join(lineData[1:])
        for val in restBags.split(','):
            val = val.strip()
            val = val.strip('s.\n')
            val = ''.join([i for i in val if not i.isdigit()])
            val = val.strip()
            if 'no other bags' in val:
                emptyBags.add(bag)
            if 'shiny gold' in val:
                goldHoldingBags.add(bag)
            bagDict[bag].append(val)
    for key in bagDict.keys():
        count += hasgold(key,bagDict)


            

    return count

def hasgold(key,bagDict):
    shinyGold = False
    try:
        for item in bagDict[key]:
            if 'shiny gold' in item:
                shinyGold = True
    except:
        pass
    if 'no other bag' in key:
        return 0
    elif shinyGold:
        return 1
    else:
        return max([hasgold(val,bagDict) for val in bagDict[key]])


            




with open("day7.txt") as f:
    data = f.readlines()
    data = [dataval for dataval in data]
    count = solve(data)
    print(count)



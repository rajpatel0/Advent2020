def solve(data):
    count = 0
    bagDict = {}
    bagDictCount = {}
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
            val = val.strip()
            bagDict[bag].append(val)
    count = getCount('shiny gold bag', bagDict)
    count -=1

            

    return count
            
def getCount(key,bagDict):
    if 'no other bag' in key:
        return 0
    else:
        values = getVals(bagDict[key])
        keys = getKeys(bagDict[key])
        return 1+sum([value*getCount(newkey,bagDict) for value,newkey in zip(values,keys)])


def getVals(data):
    listofInts = []
    for item in data:
        if item[0].isnumeric():
            listofInts.append(int(item[0]))
        else:
            listofInts.append(0)
    return listofInts

def getKeys(data):
    listofkeys = []
    for item in data:
        item=''.join([i for i in item if not i.isdigit()]) 
        item = item.strip()
        listofkeys.append(item)
    return listofkeys




with open("day7.txt") as f:
    data = f.readlines()
    data = [dataval for dataval in data]
    count = solve(data)
    print(count)



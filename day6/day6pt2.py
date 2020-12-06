import re
def solve(data):
    count = 0
    for line in data:
        listofAns = line.split(' ')
        print(listofAns)
        initialSet = set(listofAns[0])
        if len(listofAns)>1:
            for ans in listofAns[1:]:
                if ans == '':
                    continue
                newset = set(ans)
                initialSet = initialSet.intersection(newset)
        count += len(initialSet)
    return count
    

with open("day6.txt") as f:
    data = f.read()
    data = data.split('\n\n')
    data = [re.sub('\n',' ',dataval) for dataval in data]
    ans = solve(data)
    print(ans)
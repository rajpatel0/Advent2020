import re
def solve(data):
    count = 0
    for line in data:
        uniqChars=set(line)
        count += len(uniqChars)
    return count
    

with open("day6.txt") as f:
    data = f.read()
    data = data.split('\n\n')
    data = [re.sub('\n','',dataval) for dataval in data]
    ans = solve(data)
    print(ans)
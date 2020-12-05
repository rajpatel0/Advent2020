import re 
#Credits to Jon Hollenbach, damn what a cool solution note this is just part 1 can easily be extended to part 2 by using my sort.


def solve(data): 
    SeatIDs = [] 
    for item in data: item = re.sub('F|L','0',item)
        item = re.sub('B|R','1',item)
        SeatIDs.append(int(item,2))
    


with open("day5.txt") as f:
    data = f.readlines()
    data = [dataval for dataval in data]
    count=solve(data)
    print(count)

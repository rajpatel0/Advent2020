def solve(data):
    codes = ['acc','jmp','nop']
    acc =0
    i = 0
    listofi = []
    listofjmpi = []
    listofnopi = []
    lenData = len(data)
    lineToChange = 0
    while (i < lenData):
        if i in listofi:
            print("Line to change", listofi[-1])
            lineToChange = listofi[-1]
            break
        listofi.append(i)
        
        opcode = data[i].split(' ')
        if codes[2] in opcode[0]:
            listofnopi.append(i)
            i+=1
            continue
        elif codes[1] in opcode[0]:
            listofjmpi.append(i)
            jumpCount = opcode[1].strip('\n')
            if jumpCount[0] == '+':
                jump = int(jumpCount[1:])
                i+=jump
                continue
            else:
                jump = int(jumpCount[1:])
                i-=jump
                continue
        else:
            accCount = opcode[1].strip('\n')
            if accCount[0] == '+':
                accVal = int(accCount[1:])
                acc += accVal
                i+=1
                continue
            else:
                accVal = int(accCount[1:])
                acc -= accVal
                i+=1
                continue
    print("part 1", acc)
    for i in listofjmpi:
        newData = adjustedData(data,i,codes)
        val = testRun(newData,0,0,codes)
        if val > 0:
            print("part 2",val)
    for i in listofnopi:
        newData = adjustedData(data,i,codes)
        val = testRun(newData,0,0,codes)
        if val > 0:
            print("part 2",val)
 
def adjustedData(data,i,codes):
    newData = list(data)
    lineToChangeData=newData[i]
    datalist=lineToChangeData.split(' ')
    opcode = datalist[0]
    if opcode == codes[1]:
        opcode = codes[2]
    else:
        opcode = codes[1]
    newline = opcode+ ' ' + datalist[1]
    newData[i] = newline
    return newData
   


def testRun(data,i,acc,codes):
    listofi = []
    while (True):
        if i in listofi:
            break
        listofi.append(i)

        try:
            opcode = data[i].split(' ')
        except:
            return acc
        if codes[2] in opcode[0]:
            i+=1
            continue
        elif codes[1] in opcode[0]:
            jumpCount = opcode[1].strip('\n')
            if jumpCount[0] == '+':
                jump = int(jumpCount[1:])
                i+=jump
                continue
            else:
                jump = int(jumpCount[1:])
                i-=jump
                continue
        elif codes[0] in opcode[0]:
            accCount = opcode[1].strip('\n')
            if accCount[0] == '+':
                accVal = int(accCount[1:])
                acc += accVal
                i+=1
                continue
            else:
                accVal = int(accCount[1:])
                acc -= accVal
                i+=1
                continue
        else:
            return 0
    return 0
 

        
            



            




with open("day8.txt") as f:
    data = f.readlines()
    data = [dataval for dataval in data]
    count = solve(data)
    print(count)



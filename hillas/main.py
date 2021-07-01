f = open('input/231119.out_005', 'r')
lineList = f.read()
f.close()
strList = lineList.split()

#test
for i in range(10):
    print(strList[i])

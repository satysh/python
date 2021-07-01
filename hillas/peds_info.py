from pedestals import Pedestals as Peds

#read txt
f = open('input/xy.txt', 'r')
lineList = f.read()
f.close()
strList = lineList.split()
nums = []
for i in range(8, len(strList)):
    #print(strList[i])
    nums.append(float(strList[i]))

nclr = []
nfeu = []
x = []
y = []
it = 0
for i in nums:
    if it == 8:
        it = 0
    if it == 0:
        nclr.append(int(i))
    if it == 1:
        nfeu.append(int(i))
    if  it == 3:
        x.append(i)
    elif it == 4:
        y.append(i)
    it += 1

peds = None
for i in range(len(x)):
    peds = Peds(nclr[i], nfeu[i], x[i])

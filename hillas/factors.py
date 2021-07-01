class Factors(object):
    """docstring for Factors"""
    chanels_list = []
    def __init__(self, clr_id, chanel, phtamp):
        self.clr_id = int(clr_id)
        self.chanel = int(chanel)
        if phtamp != 'NaN':
                self.phtamp = float(phtamp)
        else:
            self.phtamp = 1.
        Factors.chanels_list.append(self)
    def Print(self):
        for i in Factors.chanels_list:
            print('clrid='+str(i.clr_id)+' chanelid='+str(i.chanel)+' phtamp='+str(i.phtamp))
    def get_factor(self, clr_id, chanel):
        for i in Factors.chanels_list:
            if clr_id == i.clr_id and chanel == i.chanel:
                return i.phtamp
        else:
            return None


#read txt
f = open('input/factors.txt', 'r')
lineList = f.read()
f.close()
strList = lineList.split()

#check

it = 0
factors = None
clrid = None
chanelid = None
photoamp = None
for i in range(6, len(strList)):
    if it == 0:
        clrid= strList[i]
    elif it == 1:
        chanelid = strList[i]
    elif it == 4:
        photoamp = strList[i]
    elif it == 5:
        it = -1
        factors = Factors(clrid, chanelid, photoamp)
    it += 1

#factors.Print()

'''
for i in range(1, 23):
    for j in range(1, 65):
        photoamp = factors.get_factor(i, j)
        if photoamp != None:
                print('clrid='+str(i)+' chanelid='+str(j)+' phtamp='+str(photoamp))
'''

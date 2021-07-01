class Event(object):
    """docstring for Event"""
    def __init__(self):
        self.clrsDict = dict()
        for i in range(22):
            self.clrsDict[i+1] = dict()
            pixsDict = self.clrsDict[i+1]
            for j in range(28):
                pixsDict[j+1] = 0.
    def Print(self):
        for key, val in self.clrsDict.items():
            print('clrid='+str(key))
            pixsDict = val
            for key, val in pixsDict.items():
                print('pixid='+str(key)+" amp="+str(val))
            print('\n')
    def PrintCluster(self, clrid):
        pixsDict = self.clrsDict[clrid]
        print('clrid='+str(clrid))
        for key, val in pixsDict.items():
            print('pixid='+str(key)+" amp="+str(val))
    def set_pixel_amp(self, clrid, pixid, amp):
        self.clrsDict[clrid][pixid] = amp
    def del_pixel_amp(self, clrid, pixid):
        self.clrsDict[clrid][pixid] = 0.
    def get_pixel_amp(self, clrid, pixid):
        return self.clrsDict[clrid][pixid]
    def get_amp_sum(self):
        s = 0.
        for val in self.clrsDict.values():
            pixsDict = val
            for val in pixsDict.values():
                s += val
        return s

#check
'''
ev = Event()
ev.Print()
it = 1.
for i in range(28):
    ev.set_pixel_amp(3, i+1, it)
    it += 1.
ev.PrintCluster(3)
ev.del_pixel_amp(3, 4)
ev.PrintCluster(3)
clr = 3
for pix in range(1, 29):
    print("clr="+str(clr)+' pix='+str(pix)+' amp='+str(ev.get_pixel_amp(clr, pix)))
print('s='+str(ev.get_amp_sum()))
'''

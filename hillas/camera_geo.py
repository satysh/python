import math
max_dist = 4 # cm
class CameraGeo(object):
    """
    This is a camera geometry class
    """
    pix_count = 0
    pix_list = []
    def __init__(self, clr_id, pix_id, pix_x, pix_y):
        self.clr_id = clr_id
        self.pix_id = pix_id
        self.pix_x = pix_x
        self.pix_y = pix_y
        CameraGeo.pix_count += 1
        CameraGeo.pix_list.append(self)
    def print(self):
        print(self.clr_id, self.pix_id, self.pix_x, self.pix_y)
    def get_count(self):
        return CameraGeo.pix_count
    def get_pixel(self, clr_id, pix_id):
        for pix in CameraGeo.pix_list:
            if pix.clr_id == clr_id and pix.pix_id == pix_id:
                return pix
        else:
            return None
    def get_pixels_neighbors_list(self, clr_id, pix_id):
        nei_list = []
        pixel = self.get_pixel(clr_id, pix_id)
        x1 = pixel.pix_x
        y1 = pixel.pix_y
        for pix in CameraGeo.pix_list:
            x2 = pix.pix_x
            y2 = pix.pix_y
            dist = math.sqrt( (x2-x1)**2 + (y2-y1)**2 )
            if 0. < dist <= max_dist:
                pair = (pix.clr_id, pix.pix_id)
                nei_list.append(pair)
        return nei_list
    def get_pixel_xy(self, clr_id, pix_id):
        pix = self.get_pixel(clr_id, pix_id)
        if pix != None:
                return (pix.pix_x, pix.pix_y)
        else:
            return (None, None)
    def get_pixel_x(self, clr_id, pix_id):
        pix = self.get_pixel(clr_id, pix_id)
        if pix != None:
                return pix.pix_x
        else:
            return None
    def get_pixel_y(self, clr_id, pix_id):
        pix = self.get_pixel(clr_id, pix_id)
        if pix != None:
                return pix.pix_y
        else:
            return None

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

geometry = None
for i in range(len(x)):
    geometry = CameraGeo(nclr[i], nfeu[i], x[i], y[i])

#check
'''
for clr in range(1, 23):
    for pix in range(1, 29):
        pixel = geometry.get_pixel(clr, pix)
        if pixel != None:
            nei_list = geometry.get_pixels_neighbors_list(clr, pix)
            print('clr='+str(clr)+' pix='+str(pix)+' nnei='+str(len(nei_list)))
            print('nei are:')
            for i in range(len(nei_list)):
                neiclrid, neipixid = nei_list[i]
                print(' '+str(neiclrid)+', '+str(neipixid))
'''

'''
print(geometry.get_pixel_xy(1, 1))
print(geometry.get_pixel_x(1, 1))
print(geometry.get_pixel_y(1, 1))
'''


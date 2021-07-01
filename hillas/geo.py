import numpy as np
import matplotlib.pyplot as plt
from camera_geo import geometry as geo

x = []
y = []
for clr_id in range(1, 23):
    for pix_id in range(1, 29):
        pix = geo.get_pixel(clr_id, pix_id)
        if pix != None:
            pix.print()
            x.append(pix.pix_x)
            y.append(pix.pix_y)

plt.scatter(x, y)
plt.colorbar()
plt.grid(True)
plt.show()

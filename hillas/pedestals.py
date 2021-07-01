class Pedestals(object):
    """docstring for Pedestals"""
    pix_count = 0
    pix_list = []
    def __init__(self, clr_id, pix_id, pix_amp):
        self.clr_id = clr_id
        self.pix_id = pix_id
        self.pix_amp = pix_amp
        Pedestals.pix_count += 1
        Pedestals.pix_list.append(self)
    def get_pixel(self, clr_id, pix_id):
        for pix in Pedestals.pix_list:
            if pix.clr_id == clr_id and pix.pix_id == pix_id:
                return pix
        else:
            return None
    def print(self):
        print(self.clr_id, self.pix_id, self.pix_amp)

    def get_pixel_amp(self, clr_id, pix_id):
        pix = self.get_pixel(clr_id, pix_id)
        return pix.pix_amp


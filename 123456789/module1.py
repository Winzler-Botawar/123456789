
import matplotlib.pyplot as plt
import numpy as np

#fig = plt.figure(figsize=(6,6))\


class surface(object):
    def __init__(self, col, row):
        self.col = col
        self.row = row

    #def Generate_Surface(self):
    #    step_x = (self.p2[0] - self.p1[0])/50
    #    step_y = (self.p2[1] - self.p1[1])/50
    def create(self):
        col_, row_ = np.meshgrid(np.arange(self.col),np.arange(self.row))
        print(col_.shape)




class furniture():

    pass

class door(furniture):
    pass

def init_energy_function(p1,p2,*door):
    p1.x


if __name__ == "__main__":
    a = surface(10,30)
    a.create()

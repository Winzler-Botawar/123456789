
import matplotlib.pyplot as plt
import numpy as np

#fig = plt.figure(figsize=(6,6))\


class surface(object):                          # 所有法向量都應由用戶自行標注
    def __init__(self, p1, p2, n):
        self.p1 = p1
        self.p2 = p2
        self.x_list = []
        self.y_list = []
        vec_n = n
        a = np.mat((p2[0] - p1[0]), (p2[1] - p1[0]))
        print(a.shape())

    def Generate_Surface(self):
        step_x = (self.p2[0] - self.p1[0])/50
        step_y = (self.p2[1] - self.p1[1])/50
        i = self.p1[0]
        while i < self.p2[0]:
            i += step_x
            self.x_list.append(i)
        print(self.x_list)
    #def create(self):
    #    x,y = map(int,input().split())
    #    a = np.ones((x+1,y+1))

    #    col_, row_ = np.meshgrid(np.arange(self.col),np.arange(self.row))
    #    print(col_.shape)


class furniture_group(object):
    def __init__(self, *args, **kwargs):
                                #对角点坐标
        point1_x = x1
        point1_y = y1

        point2_x = x2
        point2_y = y2

        theta_ = theta          #组方向

        grouptype = type_       #组属性

    def barycenter():
         pass



class furniture(furniture_group):
    def __init__(self, *args, **kwargs):
        super().__init__()

    pass

class door(furniture):
    pass

def init_energy_function(p1,p2,*door):
    p1.x


if __name__ == "__main__":

    #plt.figure(figsize=(5, 5)) #设置坐标轴的大小
    #plt.title("Room Coordinate")  #设置标题
    #plt.show()  #展示
    p_1 = [5,3]
    p_2 = [7,6]
    x = [2,3]
    a = surface(p_1,p_2,x)
    a.Generate_Surface()

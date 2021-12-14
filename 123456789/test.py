# coding=gbk
#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(threshold=np.inf)


def distance(i, j, k, r):
    return pow((pow(k-i, 2) + pow(r-j, 2)), 1/2)

'''
下面生成一个长宽分别为50格的房间
'''
m, n = (50, 50)
x = np.linspace(1, 50, m)    #线性序列生成器
y = np.linspace(1, 50, n)
X, Y = np.meshgrid(x, y)

#plt.style.use('ggplot')
#plt.plot(X, Y, marker='.', color='blue', linestyle='none')
#plt.grid(True)
#plt.show()

EM = np.zeros(shape = (50, 50))
center = EM[25, 25]             #实际上是[25.5， 25.5]
door = EM[10, 1]
window = EM[5, 49]
#w = [0.1, 0.3, 0.6]



for i in range(0, 50, 1):
    for j in range(0, 50, 1):
        Dmean = 0.1 * distance(i, j, 10, 1) + 0.3 * distance(i, j, 25.5, 25.5) + 0.6 * distance(i, j, 5, 49)
        Dvar = pow((pow((Dmean - 0.1 * distance(i, j, 10, 1)), 2) + pow((Dmean - 0.3 * distance(i, j, 25.5, 25.5)), 2) + pow((Dmean - 0.6 * distance(i, j, 5, 49)), 2)), 1/2)
        

        EM[j, i] = round((Dmean / Dvar), 3)


plt.figure()
plt.imshow(EM, vmin=0.7, vmax=0.9)      #色差设置
plt.colorbar()
plt.show()





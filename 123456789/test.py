import numpy as np
import matplotlib.pyplot as plt

points=np.arange(-5,5,0.01) #生成1000个间隔相等的点
xs,ys=np.meshgrid(points,points)
ys

z=np.sqrt(xs**2+ys**2)
z
plt.imshow(z,cmap=plt.cm.gray);plt.colorbar();plt.title('image plot of $\sqrt{x^2+y^2}$ for a grid of values')
plt.show()


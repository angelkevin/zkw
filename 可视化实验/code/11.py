import matplotlib
import matplotlib.pyplot as plt #导入绘图模块
from mpl_toolkits.mplot3d import Axes3D #3d绘图模块
import numpy as np #导入数值计算拓展模块
import time

start = time.time()

x_lim, y_lim, z_lim = np.linspace(-10,10,520), np.linspace(-10,10,520), np.linspace(-10,10,520)
# 用来存放绘图点X,Y,Z坐标
X_points, Y_points, Z_points = [], [], []

for x in x_lim:
    for y in y_lim:
        for z in z_lim:
            if (x**2+(9/4)*y**2+z**2-1)**3-(9/80)*y**2*z**3-x**2*z**3<=0:
                X_points.append(x)
                Y_points.append(y)
                Z_points.append(z)

end = time.time()

fig=plt.figure()                                # 画布初始化
ax=fig.add_subplot(111,projection='3d')         # 采用3d绘图
ax.scatter(X_points,Y_points,Z_points,s=20,alpha=0.5,color="red") # 3d散点图填充
plt.show()

print(end-start)
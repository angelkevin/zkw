import matplotlib
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"]=["SimHei"] 
plt.rcParams["axes.unicode_minus"]=False
x=np.linspace(0.1, 10, 100)
y=np.sin(x)
z = np.cos(x)
plt.title("sin cos 函数图像")
plt.xlabel("x坐标")
plt.ylabel("y")
plt.plot(x,y, linestyle='-',label="sin" )
plt.plot(x,z, linestyle='-', label ="cos")
plt.legend(
          title = "sin cos",
          loc = "lower left",
          shadow = True,
          facecolor = "yellow",
          edgecolor = 'pink',
          ncol = 2,
          markerfirst = False)
plt.show()

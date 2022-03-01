import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['axes.unicode_minus'] = False


def rotate(p, d):
    a = np.radians(d)
    m = np.array([[np.cos(a), np.sin(a)], [-np.sin(a), np.cos(a)]])
    return np.dot(p, m)


def koch_curve(p, q):
    p, q = np.array(p), np.array(q)
    u = p + (q - p) / 3  
    v = q - (q - p) / 3  
    w = rotate(v - u, 60) + u  

    return u.tolist(), v.tolist(), w.tolist()


def snow(triangle):
    for i in range(5):
        result = list()
        t_len = len(triangle)
        for j in range(t_len):
            p = triangle[j]
            q = triangle[(j + 1) % t_len]
            u, v, w = koch_curve(p, q)
            result.extend([p, u, w, v])
        triangle = result.copy()
        triangle.append(triangle[0])
    return triangle


import numpy as np
import matplotlib.pyplot as plt


def plot_snow(snow_list):
    for triangle in snow_list:
        data = np.array(snow(triangle))
        x, y = np.split(data, 2, axis=1)
        plt.plot(x, y)

    plt.axis('equal')
    plt.show()


snow_list = [
    ([(0, 0), (0.5, 0.8660254), (1, 0)])]
plot_snow(snow_list)
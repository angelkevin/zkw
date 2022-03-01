from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
from imageio import imread
import numpy as np
import matplotlib.pyplot as plt
import jieba
n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
plt.bar(X, +Y1, facecolor='blue')
plt.bar(X, -Y2, facecolor='pink')
plt.xlim(-.5, n)
plt.ylim(-1.25, 1.25)
for x, y in zip(X, Y1):
    plt.text(x, y + 0.05, '%.2f' % y, ha='center', va='bottom')
for x, y in zip(X, Y2):
    plt.text(x, -y-0.05, '%.2f' % y, ha='center', va='top')
plt.show()

# 示例代码
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
from imageio import imread
import numpy as np
import matplotlib.pyplot as plt
import jieba

# 打开文本
with open("郑州市第29场新冠肺炎疫情防控新闻发布会.txt", encoding="utf-8") as f:
    s = f.read()

# 中文分词
text = ' '.join(jieba.cut(s))

# 生成对象
img = Image.open("R-C.jpg")  # 打开遮罩图片
mask = np.array(img)  # 将图片转换为数组

stopwords = ["我", "你", "她", "的", "是", "了", "在", "也", "和", "就", "都", "这", "无"]
wc = WordCloud(
    stopwords= stopwords,
    mask=mask,
    max_words=500,
    font_path=r'C:\Windows\Fonts\STXINGKA.TTF',
    background_color="white",
    max_font_size=100,
    mode="RGB",
    scale=2
).generate(text)

im_colors = ImageColorGenerator(mask)
wc.recolor(color_func=im_colors)

plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

# 保存到文件
wc.to_file("6.png")

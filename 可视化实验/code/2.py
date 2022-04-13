import matplotlib.pyplot as plt
 
labels = ['1','2','3','4','5','6','7','8','9','10','11','12']
x = [5.2,2.7,5.8,5.7,7.3,9.2,8.7,15.6,10.5,11.0,7.8,3.9]
wox = [3.6,4.6,2.1,3.8,8.9,5.8,6.5,27.8,13.9,6.2,10.3,3.7]
width = 0.35     
fig, ax = plt.subplots(figsize=(5,3),dpi=200)
ax.bar(labels, x, width,label='2020')
ax.bar(labels, wox, width, bottom=x,label='2021')
ax.set_ylabel('money')
ax.set_title('Clothing store business data')
ax.legend()
plt.show()
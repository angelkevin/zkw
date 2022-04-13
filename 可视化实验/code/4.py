import matplotlib
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"] 
plt.rcParams["axes.unicode_minus"]=False
labels = ["二七区","中原区","管城区","高新区","航空港区","金水区","郑东新区"]
nums = [47,27,14,6,4,4,1]
explode = (0.1,0.1,0.1,0.1,0.1,0.1,0.1)
plt.pie(nums,explode=explode,labels=labels,autopct="%3.1f%%",startangle=45,shadow=True)
plt.title("郑州市新冠肺炎疫情")
plt.show()
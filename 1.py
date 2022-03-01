import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False
results = [{"英语": 78, "java": 90,"线性代数": 78, "马克思主义": 90,"计算机导论": 48,"体育":79,"python":82,"网页设计":93},
          {"英语": 83, "java": 85, "线性代数": 65, "马克思主义": 82, "计算机导论": 75,"体育":85,"python":78,"网页设计":85},
          {"英语": 88, "java": 85, "线性代数": 71, "马克思主义": 83, "计算机导论": 86,"体育":87,"python":89,"网页设计":56},
          {"英语": 90, "java": 80, "线性代数": 67, "马克思主义": 76, "计算机导论": 86,"体育":90,"python":76,"网页设计":92},
          {"英语": 72, "java": 73, "线性代数": 71, "马克思主义": 71, "计算机导论": 74,"体育":71,"python":82,"网页设计":84},
          {"英语": 70, "java": 86, "线性代数": 72, "马克思主义": 72, "计算机导论": 67,"体育":81,"python":66,"网页设计":77},]
data_length = len(results[0])
angles = np.linspace(0, 2*np.pi, data_length, endpoint=False)
labels = [key for key in results[0].keys()]
score = [[v for v in result.values()] for result in results]
score_a = np.concatenate((score[0], [score[0][0]]))
score_b = np.concatenate((score[1], [score[1][0]]))
score_c = np.concatenate((score[2], [score[2][0]]))
score_d = np.concatenate((score[3], [score[3][0]]))
score_e = np.concatenate((score[4], [score[4][0]]))
score_f = np.concatenate((score[5], [score[5][0]]))
angles = np.concatenate((angles, [angles[0]]))
labels = np.concatenate((labels, [labels[0]]))
fig = plt.figure(figsize=(5, 5), dpi=100)
ax = plt.subplot(111, polar=True)
ax.plot(angles, score_a, color='g')
ax.plot(angles, score_b, color='b')
ax.plot(angles, score_c, color='r')
ax.plot(angles, score_d, color='pink')
ax.plot(angles, score_e, color='y')
ax.plot(angles, score_f, color='black')
ax.set_thetagrids(angles*180/np.pi, labels)

ax.set_theta_zero_location('N')
ax.set_rlim(0, 100)
ax.set_rlabel_position(270)
ax.set_title("成绩")
plt.legend(['王芳','李普','颜美','李壮','韩晓','杨乐'], loc='upper right')
plt.show()
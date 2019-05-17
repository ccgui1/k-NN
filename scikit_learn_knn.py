# coding=gb18030
from sklearn.neighbors import KNeighborsClassifier
import operator
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams['font.sans-serif'] = ['FangSong']
from matplotlib.font_manager import FontProperties
font = FontProperties(fname='/usr/share/fonts/cjkuni-uming/uming.ttc',size=16)



plt.style.use('seaborn-whitegrid')
group = np.array([[80, 12], [90, 8], [6, 70], [4, 75]])
lables = ['爱情电影', '爱情电影', '动作电影', '动作电影']

neigh = KNeighborsClassifier(n_neighbors=2)
neigh.fit(group, lables)

print("请输入亲吻镜头：")
x = int(input())
print("请输入打斗镜头：")
y = int(input())
print(neigh.predict([[x,y]]))
plt.plot(group[:,0],group[:,1],'o')     #图形化界面
plt.xlim(0,100)                         #设置x轴上下限
plt.ylim(0,100)
plt.xlabel("爱情镜头",fontproperties=font)   #x轴标签
plt.ylabel("打斗镜头",fontproperties=font)   
plt.plot(x,y,'*')
plt.plot()
# print(neigh.predict_proba([[0.9]]))
plt.show()

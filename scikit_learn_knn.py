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
lables = ['�����Ӱ', '�����Ӱ', '������Ӱ', '������Ӱ']

neigh = KNeighborsClassifier(n_neighbors=2)
neigh.fit(group, lables)

print("���������Ǿ�ͷ��")
x = int(input())
print("������򶷾�ͷ��")
y = int(input())
print(neigh.predict([[x,y]]))
plt.plot(group[:,0],group[:,1],'o')     #ͼ�λ�����
plt.xlim(0,100)                         #����x��������
plt.ylim(0,100)
plt.xlabel("���龵ͷ",fontproperties=font)   #x���ǩ
plt.ylabel("�򶷾�ͷ",fontproperties=font)   
plt.plot(x,y,'*')
plt.plot()
# print(neigh.predict_proba([[0.9]]))
plt.show()

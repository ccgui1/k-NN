# coding=gbk
from sklearn.neighbors import KNeighborsClassifier
import operator
import numpy as np
#def createDataSet():
group = np.array([[80, 12], [90, 8], [6, 70], [4, 75]])
lables = ['�����Ӱ', '�����Ӱ', '������Ӱ', '������Ӱ']
neigh = KNeighborsClassifier(n_neighbors=2)
neigh.fit(group, lables)
print(neigh.predict([[7,26]]))
# print(neigh.predict_proba([[0.9]]))

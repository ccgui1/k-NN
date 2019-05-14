import numpy as np
print(np.array([3.14,4,2,3]))

#可通过dtype来设置数组的数据类型
print(np.array([3.14,4,2,3],dtype='int'))
print(np.array([3.14,4,2,3],dtype='float'))
print()
#嵌套列表构成的多维数组
print(np.array([range(i,i + 4) for i in [2,4,6]]))
# 创建一个长度为10的数组，数组的值都是0
print(np.zeros(10,dtype=int))
#创建一个长度为10的数组，且值为1
print(np.ones(10,dtype=int))
#创建一个3*5的浮点型数组，且值为1
print(np.ones((3,5),dtype=float))
#创建一个3*5的浮点型数组，且值为3.14
print(np.full((3,5),3.14)
#从0开始到20结束，步长为2
print(np.arange(0,20,2))
#创建一个5个元素的数组，这5个数均匀的分配到0~1
print(np.lispace(0,1,5))

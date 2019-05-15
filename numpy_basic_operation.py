import numpy as np
print(np.array([3.14,4,2,3]))
print("****************************")
#可通过dtype来设置数组的数据类型
print(np.array([3.14,4,2,3],dtype='int'))
print(np.array([3.14,4,2,3],dtype='float'))
print()
#嵌套列表构成的多维数组
print(np.array([range(i,i + 4) for i in [2,4,6]]))
# 创建一个长度为10的数组，数组的值都是0
print(np.zeros(10,dtype=int))
print("****************************")
#创建一个长度为10的数组，且值为1
print(np.ones(10,dtype=int))
#创建一个3*5的浮点型数组，且值为1
print(np.ones((3,5),dtype=float))
print("****************************")
#创建一个3*5的浮点型数组，且值为3.14
print(np.full((3,5),3.14))
print("****************************")
#从0开始到20结束，步长为2
np.arange(0,20,2)
print("****************************")
#创建一个5个元素的数组，这5个数均匀的分配到0~1
print(np.linspace(0,1,5))
print("****************************")
#创建一个3x3的、在0~1均匀分布的随机数组成的数组
print(np.random.random((3,3)))
print("*******************************************")
#创建一个3*3的、均值为0、方差为1的
#正态分布的随机数数组
print(np.random.normal(0,1,(3,3)))
print("*******************************************")
#创建一个3*3的、[0,10)区间的随机整数型数组
print(np.random.randint(0,10,(3,3)))
print("*******************************************")
#创建一个3*3的单位矩阵
print(np.eye(3,3))
print("*******************************************")
#创建一个由3个整数数组组成的未初始化的数组
#数组的值是内存空间中的任意值
print(np.empty(3))
print()
print()
print()
#指定数据类型
print(np.zeros(10,dtype='int16'))
#或者用相关的NumPy对象来指定：
print(np.zeros(10,dtype=np.int16))
print()
print()
print()
np.random.seed(0)  #设置随机数种子

x1 = np.random.randint(10, size=6)       #一维数组
x2 = np.random.randint(10, size=(3,4))    #二维数组
x3 = np.random.randint(10, size=(3,4,5)) #三维数组
print(x3) 
print("x3 ndim: ",x3.ndim)            #数组的维度
print("x3 shape ",x3.shape)           #数组的大小，3个数组，每个数组4行5列
print("x3 size  ",x3.size)            #数组的总大小,即多少个数
print("dtype: ",x3.dtype)
print("itemsize: ",x3.itemsize,"bytes")  #每个数组元素的字节大小
print("nbtybes: ",x3.nbytes,"bytes")     #数组总字节大小是属性


print("*******************************************")
print(x1)
print(x1[0])
print("*******************************************")
print(x2)
print(x2[0,0])
print(x2[2,0])
x2[0,0] = 12
print(x2)
#数组的切片x[start:stop:step]
print("*******************************************")
x = np.arange(10)
print(x)
print(x[:5])            #前5个元素
print(x[5:])            #缩引5之后的元素
print(x[4:7])           #第4个值开始，第7个值结束，包含第7个值
print(x[::2])           #每隔一个元素
print(x[1::2])          #每隔一个元素，从缩印1开始
print("逆序输出：",x[::-1])          #所有逆序输出
print("从索引5开始每隔一个元素逆序：",x[5::-2])




















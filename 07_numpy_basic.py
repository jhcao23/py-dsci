# -*- coding: utf-8 -*-

__author__ = 'John'
__date__ = '2019-09-08'
__product__ = 'PyCharm'
__filename__ = '07_numpy_basic'

# Numpy的核心数据结构ndarray多维数组_笔记
# http://www.ai111.vip/thread-213-1-1.html

# NumPy模块是Python的一种开源的数值计算扩展, 是一个用python实现的科学计算包, 主要包括:
# 1 一个具有矢量算术运算和复杂广播能力的快速且节省空间的多维数组, 称为ndarray
# ndarray  N-dimensional array object
# 2 用于对整组数据进行快速运算的标准数学函数 ufunc
# 3 实用的线性代数 傅里叶变换和随机数生成函数
# 4 Numpy和稀疏矩阵的运算包Scipy配合使用更加方便


# NumPy的核心数据结构: ndarray   N维数组
# 元素的数据类型由dtype(data-type)对象来指定, 每个ndarray只有一种dtype类型
# ndarray的大小固定 创建好后数组大小是不会发生改变的

# 创建ndarray数组对象的方法:
# 1 array函数: 接收一个普通的python序列(字符串 元祖 列表), 并将其转换为ndarray
# 2 zeros函数: 创建指定长度或形状的全0数组
# 3 ones函数: 创建指定长度或形状的全1数组
# 4 empty函数: 创建一个没有任何具体值的数组 (准确的说是创建一些未初始化的ndarray多维数组)
# 5 arange()函数: python的range()
# 6 linspace函数 等差数列  endpoint是否包含终值 默认包含终值
# 7 logspace函数 等比数列
# 8 使用随机数填充数组 numpy.random中的random()函数

# ndarray属性
# dtype : 数组元素数据类型的对象
# shape:一个数组的各个维度大小的元祖 即数组的形状
# size: 数组总个数, 即shape中各个数的相乘
# ndim: 一个数组的维度数量

import numpy as np

print(np.__version__)

# array zeros ones empty arange linspace logspace random
a = np.array([[2, 3, 4], [5, 6, 7]], dtype=np.float)
print(a)
print(a.dtype)

b = np.zeros((3, 4, 2), dtype=np.int)
print(b)

c = np.ones((2, 3))
print(c)

d = np.empty((3, 3))
print(d)

print(np.arange(1, 10, 2))
print(np.array(range(1, 10, 2)))

e = np.linspace(1, 10, 7, endpoint=False)
print(e)
print(np.linspace(1, 10, 8))

f = np.logspace(1, 8, 4, endpoint=False)
print(f)
print(np.logspace(1, 8, 5))

# [0, 1)
g = np.random.random((2, 3, 4))
print(g)

print('属性', g.dtype, g.shape, g.size, g.ndim)

print(np.random.randint(10, 20, (2, 3, 4)))

# -*- coding: utf-8 -*-

__author__ = 'John'
__date__ = '2019-09-08'
__product__ = 'PyCharm'
__filename__ = '03_numpy_transpose'

"""
.. _09_对ndarray的操作:索引_切片_转置_笔记:
    http://www.ai111.vip/thread-217-1-1.html
"""

import numpy as np


"""
数组转置与轴对换
数组转置是指将shape进行重置操作，并将其值重置为原始shape元祖的倒置
比如原始shape为（2,3,4） 则转置后为（4,3,2）
对于二维数组矩阵而言，数组的转置就是矩阵的转置
可以通过调用数组的transpose函数或T属性进行数组转置操作
"""
# shape ()
a = np.arange(24).reshape((2, 3, 4))
print(a)

b = a.T
print(b, b.shape)
b = np.transpose(a)
print(b, b.shape)
b = a.transpose()
print(b, b.shape)
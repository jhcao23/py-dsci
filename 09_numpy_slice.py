# -*- coding: utf-8 -*-

__author__ = 'John'
__date__ = '2019-09-08'
__product__ = 'PyCharm'
__filename__ = '09_numpy_slice'

"""
.. _09_对ndarray的操作:索引_切片_转置_笔记:
    http://www.ai111.vip/thread-217-1-1.html
"""

import numpy as np

"""
# 多维数组的索引 取元素的值
# axis0 axis1

# 索引--->数组的切片
# 在各个维度上单独切片, 如果某维度都保留, 则直接使用:冒号
"""
a = np.random.random((2, 3, 4))
print('a', a)
# print(a[0][1][1])
# print(a[0, 1, 1])
# print(a[0][0][1:3])
# print(a[0][1][1:3])
print('a[0][2][1:3]', a[0][2][1:3])
print('a[0, :, 1:3]', a[0, :, 1:3])
print('a[0][:].T[1:3].T', a[0][:].T[1:3].T)
print('-----')


"""
注意: numpy中通过切片得到的新数组, 只是原来数组的一个视图, 因此对新数组
进行操作也会影响原数组  内存地址的引用还是一样
"""

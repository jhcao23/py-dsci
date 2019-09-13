# -*- coding: utf-8 -*-

__author__ = 'John'
__date__ = '2019-09-08'
__product__ = 'PyCharm'
__filename__ = '08_numpy_shape'

"""
 .. _ndarray元素类型转换_shape变换_元素级运算_矩阵积:
     http://www.ai111.vip/thread-215-1-1.html
"""

import numpy as np

"""
数据类型可以变  shape也是可以变的
1 直接修改数组ndarray的shape值, 要求修改后乘积不变
2 直接使用reshape函数创建一个改变尺寸的新数组, 原数组的shape保持不变, 但是新数组和原数组共享一个内存空间
也就是修改任何一个数组中的值都会对另外一个产生影响, 要求新旧数组的元素个数一致 也就是size一致

当指定某一个轴为-1的时候, 表示将根据数组元素的size自动计算该轴的长度值
"""
d = np.random.random((2, 3, 5))
print(d, d.shape)
# d.shape = (3, 10)
# size = 3*5 *2 ndim
# print(d, d.shape)
e = d.reshape((3, 2, 5))
print(e, e.shape, d, d.shape)
f = d.reshape((3, -1, 5))
print(e, e.shape, d, d.shape)

"""
数组与标量 数组之间的运算 add multiple
数组不用循环即可对每个元素执行批量的算术运算操作, 这个过程叫做矢量化, 即用数组表达式替代循环
矢量化数组运算性能比纯python方式快上一两个数量级
每个维度大小相等的两个数组之间的任何算术运算都会将其运算应用到元素级上的操作
元素级操作: 在numpy中每个维度大小相等的数组之间的运算, 为元素级运算, 即只用于位置相同的元素之间
所得的运算结果组成一个新的数组, 运算结果的位置与操作数位置相同
字符串与数字不能加
"""
a1 = [2, 3, 5]
b1 = ['222', 'dfy', 88]
print('a1', a1, 'b1', b1)
print('a1+b1', a1+b1)

a = np.array([2, 3, 5])
b = np.array(['4', '5', '2'], dtype=int)
print('a*b', a*b)
print('a^2', a**2)


"""
数组的运算  数组之间  数组与标量之间

数组的矩阵积   矩阵: 多维数组即矩阵
矩阵的乘法: 不是元素级操作, 两个二维矩阵满足一个矩阵的列数与第二个矩阵的行数相同, 
矩阵积: 也称为 点积 数量积
三维数组也可以做矩阵积  多维数组也可以只是复杂一些

.. _dot:
    https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.dot.html#numpy.dot
"""
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[2, 3, 4], [4, 6, 8]])
print('d', d, 'd.shape', d.shape)
d.shape = (3, 2)
print('c', c)
print('d', d)
print(c.shape, d.shape)
# print(c*2)
print('------')
print('np.dot(c, d)', np.dot(c, d))
print('c.dot(d)', c.dot(d))



# -*- coding: utf-8 -*-

__author__ = 'John'
__date__ = '2019-09-08'
__product__ = 'PyCharm'
__filename__ = '09_numpy_index_shard_transform'


"""
.. _09_对ndarray的操作:索引_切片_转置_笔记:
    http://www.ai111.vip/thread-217-1-1.html
"""

import numpy as np


"""
布尔值的索引: 利用布尔类型的数组进行数据索引, 最终返回的结果是对应
索引数组中数据为True位置的值
True位置的元素取出来形成一个新数组(一维的)
条件是: b与c数组的shape必须一致

数据提取 数据清洗用到的方法

注意: numpy中不能使用python中的and or not操作符 使用 & | ~ 来替换
"""
print('-----')
print('bool值的索引')
b = np.random.random((4, 4, 2))
print('b', b)
c = b > 0.5
print('c', c)
d = b[c]
print('d', d, 'type', type(d))

"""花式索引: 利用整数数组进行索引的方式 ix_函数会产生一个索引器"""

a = np.arange(32).reshape((8, -1))
print(a)
print('------')
print(a[1:3])  #连续
print(a[[0, 3, 5]])  #非连续行  连续的列
# axis0行 axis1列
# 非连续行 非连续列  交叉的值
print(a[[0, 3, 5], [0, 3, 2]])
# 非连续行 非连续列 所有的
print(a[np.ix_([0, 3, 5], [0, 2, 3])])
print('-----')
print(a[[0, 3, 5]].T[[0, 2, 3]].T)


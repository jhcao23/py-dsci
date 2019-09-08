# -*- coding: utf-8 -*-

__author__ = 'John'
__date__ = '2019-09-08'
__product__ = 'PyCharm'
__filename__ = '08_numpy_type'

"""
 .. _ndarray元素类型转换_shape变换_元素级运算_矩阵积:
     http://www.ai111.vip/thread-215-1-1.html
"""

import numpy as np

"""
# 数据类型的简写  int8  i8
uint8 u1   bool_   float32  f($)
complex128 c16（由两个64位的浮点数来表示）  复数  实数+虚数
object 往数组里存一个自定义的  或 ndarray里放ndarray
string_  unicode_
"""

a = np.array([2900, 3, 4])
print(a, a.dtype)
b = a.astype(np.complex128)
print(b.dtype, a.dtype)
c = np.array(['python', 'java', 'rn'], dtype='U14')
print(c, c.dtype)

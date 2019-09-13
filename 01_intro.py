# -*- coding: utf-8 -*-

"""
01 python数据分析基础模块 numpy scipy pandas matplotlib

conda install XXX OR  pip/pip3 install XXX

numpy提供常用的数值数组 矩阵等函数
numpy的优点: 1 基于向量化的运算   2 进行数值运算时numpy数组比list效率高
"""
import numpy as np

print(np.arange(10))

for i in range(10):
    print(i)

a = np.arange(10)
print(a**2)

"""
scipy 是一种基于numpy的扩展 用来做高等数学 信号处理 优化 统计的扩展包比如: 线性代数 统计的 空间的数据结构
"""
from scipy import linalg

a = np.array([[1, 2], [30, 4]])
print(a)
# 二阶方阵行列式
print(linalg.det(a))

# 推荐用scipy.linalg代替numpy.linalg

"""
Pandas 是一种构建于Numpy的高级数据结构和精巧工具, 快速简单的处理数据    数据结构: Series和DataFrame
"""
import pandas as pd

s = pd.Series([2, 4, 5, np.nan, 8, 9])
print(s)

dates = pd.date_range('20171201', periods=7)
print(dates)

df = pd.DataFrame(np.random.randn(7, 4), index=dates, columns=list('ABCD'))
print(df)
# 转置
# print(df.T)

print(df.sort_values(by='B'))

print(df.head(2))
print(df.tail(1))
print(df.describe())

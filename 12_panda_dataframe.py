# -*- coding: utf-8 -*-

__author__ = 'John'
__date__ = '2019-09-12'
__product__ = 'PyCharm'
__filename__ = '12_panda_dataframe'

"""
12 pandas的数据结构DataFrame详解_笔记
http://www.ai111.vip/thread-224-1-1.html
"""

"""
DataFrame的创建:  2 字典
字典中的value只能是一维数组或者单个的简单数据类型, 如果是数组长度必须一致

索引对象, 不管是Series还是DataFrame对象, 都有索引对象
他们的自动对齐功能也是通过索引实现的
DataFrame可以直接通过列索引获取指定列的数据

如果需要获取指定行的数据的话, 需要通过ix方法来获取对应行索引的行数据

DataFrame可以切片操作

修改值  新增列 新增行  numpy是不能加新行新列的 但是DataFrame可以
修改某个具体对象的值, 即可以先列后行 也可以先行后列 最好是先列后行可以自动改变对象的数据类型
"""

import pandas as pd
import numpy as np

arr = [['dfy', 100], ['zs', 90], ['ls', 88]]
df1 = pd.DataFrame(arr)
print('df1', df1)
print('df1.index', df1.index)
print('df1.columns', df1.columns)
print('df1.dtypes', df1.dtypes)

# rename indexes(rows) and columns
# method 0
df1 = pd.DataFrame(arr, index=['第一行', '第二行', '第三行'], columns=['name', '分数'])
# method 1
df1 = pd.DataFrame(df1, index=['第一行', '第二行', '第三行'], columns=['name', '分数'])
# method 2
df1.index, df1.columns = ['第一行', '第二行', '第三行'], ['name', '分数']
print('df1 with given indexs and columns ', df1)

# using dict to construct DataFrame
dict1 = {
    'Chinese': [90, 88, 67],
    'Math': [99, 78, 89],
    'English': [98, 102, 125],
    'Physics': 88
}
df2 = pd.DataFrame(dict1)
df2.index = ['dfy', 'zs', 'ls']
print('df2', df2)

# reading should go column first then row (index)
#print(df2['dfy']['Chinese']) # throw error
print(df2['Chinese']['dfy']) # okay!
print(df2.ix['dfy']['Chinese'])
print(df2.ix[:2, :2])
# question: how to do slicing for column first then row?
#print(df2[:2, :2]) # throw error
print(df2.dtypes)

# assignment to DataFrame
df2['English'] = np.nan
df2.ix['dfy']['English'] = np.nan
df2['English'] = [0, 0, 0]
df2.ix['dfy']  = [100, 100, 100, 100]
df2['XXX'] = np.nan
df2.ix['YYY'] = np.nan
print(df2)
print(df2.dtypes)

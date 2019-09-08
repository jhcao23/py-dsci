# -*- coding: utf-8 -*-
__author__ = 'John'
__date__ = '2019-09-08'
__product__ = 'PyCharm'
__filename__ = '04_lamda'

"""
04 python中的匿名函数与Lambda表达式_源码
"""

from functools import reduce

result = []
for i in range(8):
    result.append(i**2)
print(result)

print([i ** 2 for i in range(8)])

print([i for i in range(9) if i % 2 == 0])

a = [[1, 2, 3], [44, 55, 66], [77, 88, 99]]
print([j for i in a for j in i])


lambda1 = lambda x: x ** 2
lambda2 = lambda x, y: x + y
lambda3 = lambda x: x % 2 == 0

# python map reduce filter

print(list(map(lambda1, range(8))))

print(reduce(lambda2, range(8)))

print(list(filter(lambda3, range(8))))

# 练习：计算5!+4!+3!+2!+1!的和
# 要求：使用我们刚刚讲的lambda和map reduce filter

# 5!= 5*4*3*2*1
la1 = lambda x, y: x * y

print(reduce(la1, range(1, 6)))

la2 = lambda n: reduce(la1, range(1, n + 1))
print(list(map(la2, range(1, 6))))

la3 = lambda a, b: a + b

print(reduce(la3, list(map(la2, range(1, 6)))))

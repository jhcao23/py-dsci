# -*- coding: utf-8 -*-

__author__ = 'John'
__date__ = '2019-09-08'
__product__ = 'PyCharm'
__filename__ = '03_iterator'

"""
03 python中的装饰器与迭代器
http://www.ai111.vip/thread-204-1-1.html

迭代器（iterator）
可迭代的对象：如果一个对象可以用for in 的方式遍历其内容 就是一个可迭代的对象 list tuple 字典
迭代器：遍历可迭代对象内容的方式
常见的迭代器：组合 排列 笛卡尔积  串联迭代器可以被next()函数调用的并不断返回下一个值得对象叫做迭代器：iterator
凡是可以用作与next()函数的对象都是iterator
"""

# 排列 组合 笛卡尔积 串联迭代器
import itertools
x = range(1, 5)
y = list('abc')
# 排列
com1 = itertools.combinations(x, 3)
#  组合
com2 = itertools.permutations(x, 3)

# 笛卡尔积
com3 = itertools.product(x, y)

# 串联迭代器
com4 = itertools.chain(com1, com2, com3)


for i in com4:
    print(i)

'''可迭代对象与迭代器的区别：通过iter()将一个可迭代对象变成迭代器'''
list01 = [1,2,3,4,5] #是一个可迭代对象
# for i in list01:
#     print(i)
# print(next(list01))   #list01不是迭代器所以无法调用  next

#通过iter()将一个可迭代对象变成迭代器
a = iter(list01)
print(a)
print(next(a))
print(next(a))
print(next(a))

"""
Yield
yield 生成器
    生成一个迭代器
        -> yield的作用是吧一个函数变成一个generator
        -> 使用生成器可以达到延迟操作的效果，所谓延迟操作就是指在需要的时候
        产生结果而不是立即产生就结果，节省资源消耗，和声明一个序列不同的是
        生成器，在不使用的时候几乎是不占内存的。
如果生成器用了next() 则for循环会接着next()的位置进行哦
        
"""
def getNum(n):
    i = 0
    while i <= n:
        # print(i)    #打印i
        #return i
        # #返回一个i ,结束函数的运行
        yield i
        #将函数变成一个generator
        i+=1
# 调用函数
print(getNum(5))

#把生成器赋值给一个变量a
a = getNum(5)
# 使用生成器 通过 next()方法
print(next(a))
#输出yield返回的值
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
# print(next(a))

#for循环遍历一个生成器
for i in a:
    print(i)
'''如果生成器用了next() 则for循环会接着next()的位置进行哦'''
def gen():
    i = 0
    while i < 5:
        temp = yield i  #是赋值操作吗？不是
        #使用了yield之后是一个生成器
        print(temp)   #因为 yield 之后返回结果到调用者的地方，暂停运行 ，赋值操作没有运行
        i+=1
a = gen()
print(next(a))
print(next(a))
print(a.send('我是a'))  #可以将值发送到 上一次yield的地方

print('*'*8)
print(next(a))



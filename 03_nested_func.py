# -*- coding: utf-8 -*-

__author__ = 'John'
__date__ = '2019-09-08'
__product__ = 'PyCharm'
__filename__ = '03_nested_func'

"""
02 python中函数的嵌套定义与使用_笔记
http://www.ai111.vip/thread-199-1-1.html
"""

def fun1():
    def fun2():
        print('hello world')
    return fun2

fun1()()

"""函数嵌套的三层用法"""
def fun1():
    print('我是fun1的函数体语句')

    def fun2():
        print('我是fun2的函数体语句')

        def fun3():
            print('Hello World!')
        return fun3
    return fun2

a = fun1()
b = a()
b()
# fun1中返回 fun2的方法名
# fun1()就是调用函数 返回fun2的函数入口给变量a
# a()就是调用函数fun2 返回fun3的函数入口给变量b
# 最后调用b()
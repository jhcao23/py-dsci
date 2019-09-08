# -*- coding: utf-8 -*-

__author__ = 'John'
__date__ = '2019-09-08'
__product__ = 'PyCharm'
__filename__ = '03_recursive_func'


"""
02 python中函数的嵌套定义与使用_笔记
http://www.ai111.vip/thread-199-1-1.html
"""

"""
    递归函数
"""
def main(n):
    print('进入第%d层梦境'%n)
    if n == 3:
        print('到达潜意识区,原来我最爱的人是你！开始醒来')
    else:
        main(n+1)
    print('从第%d层梦境醒来'%n)


main(1)  #回到调用的地方
"""
    第一次调用:进入第1层梦境
        第二次调用：进入第2层梦境
            第三次调用：进入第3层梦境 进入 if 到达潜意识区,原来我最爱的人是你！开始醒来
            从第3层梦境醒来 结束第三次调用
        从第2层梦境醒来 结束第二次调用
    从第1层梦境醒来 结束第一次调用
"""

"""用递归函数 计算阶乘问题"""
"""
    阶乘
"""
def jiecen(n):
    if n == 1:
        return 1
    else:
        return n*jiecen(n-1)

print(jiecen(5))
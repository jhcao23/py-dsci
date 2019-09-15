# -*- coding: utf-8 -*-

__author__ = 'John'
__date__ = '2019-09-13'
__product__ = 'PyCharm'
__filename__ = '19_thread'

"""
19 Python中的多线程模块threading_笔记
http://www.ai111.vip/thread-248-1-1.html
"""

"""
时间片
由于cpu的执行效率非常高, 时间片非常短, 在各个任务之间快速的切换, 给人的感觉就是多个任务在同时进行, 并发运行

进程与线程的区别: 
1 线程是程序执行的最小单位, 而进程是操作系统分配资源的最小单位
2 一个进程是由一个或多个线程组成, 线程是一个进程中代码的不同执行路线
3 进程之间相互独立, 但同一个进程下的各个线程之间共享程序的内存空间 (包括代码段 数据集 堆等) 及一些进程级的资源 (如打开文件和信号) 
某进程内的线程在其他进程是不可见的
4 调度和切换: 线程上下文切换比进程上下文切换要快得多
总之, 进程与线程都是一种抽象的概念, 线程是一种比进程更小的抽象, 线程和进程都可用于实现并发
"""

import time
import threading

# 多任务 并发运行 :  进程 线程
# 时间片  cup时间  0.01秒 1秒
# 人  cpu视角去看

def music(name, loop):
    for i in range(loop):
        print('在听音乐: %s 时间: %s name:%s id:%s'%(name, time.ctime(), t1.getName(), t1.ident))
        time.sleep(1)


def movie(name, loop):
    for i in range(loop):
        print('在看电影: %s 时间: %s name:%s id:%s' % (name, time.ctime(), threading.Thread.getName(t2), t2.ident))
        time.sleep(1)

# music('模特', 3)
# movie('速度8', 4)
# print('任务结束啦 时间: %s'%time.ctime())


t1 = threading.Thread(target=music, args=('模特', 3))
t1.setName('music thread')

t2 = threading.Thread(target=movie, args=('速度与激情8', 4), name='movie thread')

# 设置一下线程守护
t1.setDaemon(True)
t2.setDaemon(True)

t1.start()
t2.start()

# 阻塞主线程
t1.join(1)
t2.join(1)

# 主线程
print('任务结束啦 时间: %s'%time.ctime())

"""
python中仅仅只支持一个线程的运行
python中多线程模块: thread模块 threading模块 推荐用threading模块
主要原因是thread不支持守护线程, 当主线程退出时, 所有的子线程不管他们是否还在工作, 都会被强行退出, 
有时我们并不希望发生这种行为, 这时就引入了守护线程的概念 threading模块支持守护线程

threading.Thread是threading模块中最重要的类之一
创建线程有两种方式: 
1 继承Thread类, 重写它的run方法
2 创建一个threading.Thread的实例对象 (__init__构造方法) , 将调用对象作为参数传入

给线程设置名字: 1 线程对象.setName()  2 name参数传入
线程的id   ident
Thread.join([timeout]) 会使主线程阻塞, 直到被调用线程运行结束或超时 如果没有提供超时参数, 则主线程将一直阻塞直到被调线程结束
主线程: 不包含在Thread里面的程序 UI界面 Main函数

setDaemon:主线程A启动了子线程B 调用B.setDaemon(True),则主线程结束时, 会把子线程B也杀死, 必须在start线程之前设置
"""






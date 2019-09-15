# -*- coding: utf-8 -*-

__author__ = 'John'
__date__ = '2019-09-15'
__product__ = 'PyCharm'
__filename__ = '20_multiprocessing_pool'

"""
20 python中的多进程模块multiprocessing与进程池pool_笔记
http://www.ai111.vip/thread-250-1-1.html
"""
import time
import multiprocessing
import os

"""
pool 进程池

Pool可以提供指定数量的进程, 供用户调用, 当有新的请求提交到pool中时, 
如果池还没有满, 那么就会创建一个新的进程用来执行该请求；
但如果池中的进程数已经达到规定最大值, 那么该请求就会等待, 直到池中有进程结束, 才会创建新的进程来执行它. 


进程池方法: 
apply(func[, args[, kwds]]):  阻塞的执行, 比如创建一个有3个线程的线程池, 当执行时是创建完一个,执行完函数再创建另一个, 变成一个线性的执行.  apply_async(func[, args[, kwds[, callback]]]) :  它是非阻塞执行, 同时创建3个线程的线城池, 同时执行, 只要有一个执行完立刻放回池子待下一个执行, 并行的执行 .
close():  关闭pool, 使其不在接受新的任务. 
terminate():  结束工作进程, 不在处理未完成的任务. 
join(): 主进程阻塞, 等待子进程的退出,  join方法要在close或terminate之后使用. 
"""

# 进程池 pool

def work(n):
    print('run work(%s) start, work id :%s'%(n, os.getpid()))
    time.sleep(3)
    print('work(%s) end, work id :%s'%(n, os.getpid()))

print('父进程 id: %s'%os.getpid())

# 创建一个进程池 里面同时2个子进程
p = multiprocessing.Pool(2)
for i in range(5):
    # 5个任务去提交进程池
    # p.apply(work, args=(i, )) # 同步 synchronous
    p.apply_async(work, args=(i, )) # 异步 asynchronous

p.close()
# p.terminate()
p.join()

print('父进程结束')

"""
运行代码的时候 windows上会报错:
    This probably means that you are not using fork to start your
            child processes and you have forgotten to use the proper idiom
            in the main module:
                if __name__ == '__main__':
                    freeze_support()
解决方法: 只需要加上这个判断即可 if __name__ == '__main__':
__name__  如果在当前py文件运行则返回__main__ 如果是被引入作为模块在另外py文件运行则返回模块名
mac环境下 不加判断也是没有问题的
"""
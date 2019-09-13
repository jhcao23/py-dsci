# -*- coding: utf-8 -*-

__author__ = 'John'
__date__ = '2019-09-13'
__product__ = 'PyCharm'
__filename__ = '20_multiprocessing'

"""
20 python中的多进程模块multiprocessing与进程池pool_笔记
http://www.ai111.vip/thread-250-1-1.html
"""

"""
multiprocessing库的出现很大程度上是为了弥补threading库因为GIL低效的缺陷. 
它完整的复制了一套threading所提供的接口方便迁移. 
唯一的不同就是它使用了多进程而不是多线程. 
每个进程有自己的独立的GIL, 完全并行, 无GIL的限制(进程中包括线程), 
可充分利用多cpu多核的环境,因此也不会出现进程之间的GIL争抢. 

进程间虽然不能共享某一个内存空间 但是进程间可以通行

python多进程并发, 模块名称: multiprocessing
python中的多线程其实并不是真正的多线程, 如果想要充分地使用多核CPU的资源, 在python中大部分情况需要使用多进程
借助这个包, 可以轻松完成从单进程到多进程并发执行的转换. 

multiprocessing包是Python中的多进程管理包. 与threading.Thread类似, 
它可以利用multiprocessing.Process对象来创建一个进程. 
该Process对象与Thread对象的用法相同, 也有start(), run(), join()等方法. 
此外multiprocessing包中也有Lock/Event/Semaphore/Condition类 (这些对象可以像多线程那样, 通过参数传递给各个进程), 
用以同步进程, 其用法与threading包中的Thread类一致. 
所以, multiprocessing的很大一部份与threading使用同一套API, 只不过换到了多进程的情境. 
multiprocessing提供了threading包中没有的IPC(比如Pipe和Queue), 效率上更高. 
应优先考虑Pipe和Queue, 避免使用Lock/Event/Semaphore/Condition等同步方式 (因为它们占据的不是用户进程的资源,而是线程). 

同步执行: 一个进程在执行任务时, 另一个进程必须等待执行完毕, 才能继续执行,
加锁可以保证多个进程修改同一块数据时, 同一时间只能有一个任务可以进行修改.
没错, 速度是慢了, 但牺牲了速度却保证了数据安全. 
异步执行: 一个进程在执行任务时, 另一个进程无需等待其执行完毕就可以执行, 
当有消息返回时, 系统会提醒后者进行处理, 这样会很好的提高运行效率
"""

# 多进程
import time
import multiprocessing

# 单进程
def work_1(filename, n):
    print('work_1 start')
    for i in range(n):
        with open(filename, 'a') as f_obj:
            f_obj.write('i love python \n')
            time.sleep(1)
    print('work_1 end')


def work_2(filename, n):
    print('work_2 start')
    for i in range(n):
        with open(filename, 'a') as f_obj:
            f_obj.write('www.ai111.vip come on!  \n')
            time.sleep(1)
    print('work_2 end')

work_1('dfy.txt', 3)
work_2('dfy.txt', 4)

# 多进程
def work_1(filename, n):
    print('work_1 start')
    for i in range(n):
        with open(filename, 'a') as f_obj:
            f_obj.write('i love python \n')
            time.sleep(1)
    print('work_1 end')


def work_2(filename, n):
    print('work_2 start')
    for i in range(n):
        with open(filename, 'a') as f_obj:
            f_obj.write('www.ai111.vip come on!  \n')
            time.sleep(1)
    print('work_2 end')

p1 = multiprocessing.Process(target=work_1, args=('dfy.txt', 3))
p2 = multiprocessing.Process(target=work_2, args=('dfy.txt', 4))

p1.start()
p2.start()

# 同步执行  异步执行

# 加锁 同步
def work_1(filename, n, lock):
    print('work_1 start')
    lock.acquire()
    for i in range(n):
        with open(filename, 'a') as f_obj:
            f_obj.write('i love python \n')
            time.sleep(1)
    print('work_1 end')
    lock.release()


def work_2(filename, n, lock):
    print('work_2 start')
    lock.acquire()
    for i in range(n):
        with open(filename, 'a') as f_obj:
            f_obj.write('www.ai111.vip come on!  \n')
            time.sleep(1)
    print('work_2 end')
    lock.release()

lock = multiprocessing.Lock()
p1 = multiprocessing.Process(target=work_1, args=('dfy.txt', 3, lock))
p2 = multiprocessing.Process(target=work_2, args=('dfy.txt', 4, lock))

p1.start()
p2.start()


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
import os

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
    # p.apply(work, args=(i, ))
    p.apply_async(work, args=(i, ))

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
# -*- coding: utf-8 -*-

__author__ = 'John'
__date__ = '2019-09-15'
__product__ = 'PyCharm'
__filename__ = '20_multiprocessing_lock'

"""
20 python中的多进程模块multiprocessing与进程池pool_笔记
http://www.ai111.vip/thread-250-1-1.html
"""
import time
import multiprocessing

# 同步执行 & 异步执行 | sync & async

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

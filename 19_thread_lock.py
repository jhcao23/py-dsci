# -*- coding: utf-8 -*-

__author__ = 'John'
__date__ = '2019-09-15'
__product__ = 'PyCharm'
__filename__ = '19_thread_lock'

"""
19 Python中的多线程模块threading_笔记
http://www.ai111.vip/thread-248-1-1.html
"""

"""
GIL全局解释锁简介
GIL并不是Python的特性, Python完全可以不依赖于GIL
为了更有效的利用多核处理器的性能, 就出现了多线程的编程方式, 而随之带来的就是线程间数据一致性和状态同步的困难. 为了有效解决多份缓存之间的数据同步时各厂商花费了不少心思,就有了GIL,也不可避免的带来了一定的性能损失
Python当然也逃不开, 为了利用多核, Python开始支持多线程. 而解决多线程之间数据完整性和状态同步的最简单方法自然就是加锁.  于是有了GIL这把超级大锁
GIL无疑就是一把全局排他锁. 毫无疑问全局锁的存在会对多线程的效率有不小影响. 甚至就几乎等于Python是个单线程的程序.  那么读者就会说了, 全局锁只要释放的勤快效率也不会差啊. 只要在进行耗时的IO操作的时候, 能释放GIL, 这样也还是可以提升运行效率的嘛. 或者说再差也不会比单线程的效率差吧. 理论上是这样, 而实际上呢? Python比你想的更糟. 
但当CPU有多个核心的时候, 问题就来了. 从release GIL到acquire GIL之间几乎是没有间隙的. 所以当其他在其他核心上的线程被唤醒时, 大部分情况下主线程已经又再一次获取到GIL了. 这个时候被唤醒执行的线程只能白白的浪费CPU时间, 看着另一个线程拿着GIL欢快的执行着. 然后达到切换时间后进入待调度状态, 再被唤醒, 再等待, 以此往复恶性循环. GIL的存在导致多线程无法很好的利用多核CPU的并发处理能力. 
http://www.ai111.vip/forum.php?mod=attachment&aid=NDV8ZDBjZmIyNGJ8MTU2ODQxNTgzMHw0OHwyNDg%3D&nothumb=yes
http://www.ai111.vip/forum.php?mod=attachment&aid=NDZ8YmFkYmE0MTh8MTU2ODQxNTgzMHw0OHwyNDg%3D&nothumb=yes
"""

import threading

# 锁
balance = 0

lock = threading.Lock()

def change(n):
    global balance
    balance += n
    balance -= n

def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change(n)
        finally:
            lock.release()

# run_thread(8)
t1 = threading.Thread(target=run_thread, args=(4,))
t2 = threading.Thread(target=run_thread, args=([8]))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

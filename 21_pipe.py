# -*- coding: utf-8 -*-

__author__ = 'John'
__date__ = '2019-09-15'
__product__ = 'PyCharm'
__filename__ = '21_pipe'

"""
21 python中的进程间通信 线程间通信与生产者消费者模型_笔记
http://www.ai111.vip/thread-252-1-1.html
"""

"""
multiprocessing.Queue
进程彼此之间互相隔离, 要实现进程间通信 (IPC) ,
multiprocessing模块支持两种形式: 队列Queue和管道Pipe, 这两种方式都是使用消息传递的


创建队列的类 (底层就是以管道和锁定的方式实现) : 
Queue([maxsize]):创建共享的进程队列, Queue是多进程安全的队列, 可以使用Queue实现多进程之间的数据传递. 
参数介绍: maxsize是队列中允许最大项数, 省略则无大小限制. 

Queue介绍方法
q.get_nowait():同q.get(False)
q.put_nowait():同q.put(False)
q.empty():调用此方法时q为空则返回True, 该结果不可靠, 比如在返回True的过程中, 如果队列中又加入了项目. 
q.full(): 调用此方法时q已满则返回True, 该结果不可靠, 比如在返回True的过程中, 如果队列中的项目被取走. 
q.qsize():返回队列中目前项目的正确数量, 结果也不可靠, 理由同上.

pipe管道通信

Pipe方法返回(conn1, conn2)代表一个管道的两个端. 
Pipe方法有duplex参数: duplex 为 True(默认值), 那么这个管道是全双工模式, 也就是说conn1和conn2均可收发. 
duplex 为 False, conn1只负责接受消息, conn2只负责发送消息. 前收后发

send和recv方法分别是发送和接收消息的方法. 
在全双工模式下, 可以调用conn1.send发送消息, conn1.recv接收消息. 
如果没有消息可接收, recv方法会一直阻塞. 如果管道已经被关闭, 那么recv方法会抛出EOFError
"""

import multiprocessing
import time

# 进程间通信  发消息 数据
# 队列 & 管道 | Queue & Pipe

# Pipe管道的方式 跨进程通信

def put(p):
    for value in ['a', 'b', 'c']:
        print('发送 %s 到pipe中...'%value)
        p[1].send(value)
        # q.put(value)
        time.sleep(2)


def get(p):
    while True:
        # value = q.get(True)
        value = p[0].recv()
        print('从pipe取到数据: %s !'%value)

# Pipe()方法返回 (conn1,conn2)  代表是一个管道的两端
# 前收 后发
p = multiprocessing.Pipe(duplex=False)

pwrite = multiprocessing.Process(target=put, args=(p, ))
pread = multiprocessing.Process(target=get, args=(p, ))

pwrite.start()
pread.start()

pwrite.join()
pread.terminate()

print('父进程结束')

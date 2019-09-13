# -*- coding: utf-8 -*-

__author__ = 'John'
__date__ = '2019-09-08'
__product__ = 'PyCharm'
__filename__ = '06_time'

"""
06 python中的时间Time模块_源码
"""

from datetime import datetime
import time

print(datetime.now())
print(time.time())
# 时间戳  1970 1 1 0 0 到现在为止的秒数
# time_tuple 时间元祖  struct_time
print(time.localtime())


# 2017/12/21 17:12:34
# %Y %y  %m %d  %H  %I  %M  %S
print(time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()))

time_tuple = time.strptime('2017-12-12 14:23:56', '%Y-%m-%d %H:%M:%S')
print(time.mktime(time_tuple))
# 时间字符串 时间元祖  时间戳

'''
    sleep 推迟调用线程的运行, secs指秒数
'''
for i in range(1,3):
    print('让子弹飞一会')
    time.sleep(2)
    print('子弹在飞')
    time.sleep(2)
    print('子弹到了')

# 计算三天前的时间 按格式输出
# 获取现在的时间戳
now = time.time()
# 减去三天的秒数
three_ago = now - 60*60*24*3
# 将时间戳转换为时间元组
time_tuple = time.localtime(three_ago)
# 将时间戳转换为时间字符串
print(time.strftime('%Y-%m-%d %H:%M:%S', time_tuple))
# -*- coding: utf-8 -*-

__author__ = 'John'
__date__ = '2019-09-08'
__product__ = 'PyCharm'
__filename__ = '05_mysql'

"""
05 python中操作mysql数据库CRUD(增 删 改 查)_源码
pymysql: https://github.com/PyMySQL/PyMySQL
https://pymysql.readthedocs.io/en/latest/
"""

import pymysql

# python操作mysql数据库的三种方式：1、pymysql  2、mysqldb 3、sqlalchemy

password = 'PASSWORD'
database_name = 'DATABASE_NAME'

# 1、数据库的连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password=password, db=database_name, charset='utf8')
# print(conn)

# 2、创建操作的游标
cursor = conn.cursor()

# 3、设置字符编码以及自动提交
cursor.execute('set names utf8')
cursor.execute('set autocommit=1')
# conn.commit()

# 4、编写sql语句 crud
# sql = "insert into tb_user(name, pwd) values('dfy888', '222')"
# sql = 'delete from tb_user where id={0}'.format(2)
# sql = "update tb_user set pwd='333' where name='dfy999'"
sql = 'select * from tb_user'
print(sql)

# 5、执行sql并且得到结果集

cursor.execute(sql)

# 得到结果集三种方式：fetchone()  fetchemany(n)  fetchall()

# result = cursor.fetchall()
# result = cursor.fetchone()
result = cursor.fetchmany(2)
print(result)

# 6、关闭游标和连接
cursor.close()
conn.close()

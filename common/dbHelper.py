# import pymysql
#
# def connect_mysql():
#     db = pymysql.Connect(host="192.168.100.55",
#                          port=3306,
#                          user="root",
#                          password="root",
#                          db="db_test_jk",
#                          charset="utf8")
#     return db
#
# def createCur():
#     db = connect_mysql()  # 数据库对象
#     cur = db.cursor()  # 创建游标，作用，启动/激活数据库
#     return cur
#
#
# def selectMethod(sql):
#     '''
#     查询方法
#     :param sql: sql语句
#     :return: 查询结果，元祖
#     '''
#     cur = createCur()
#     cur.execute(sql)  # 执行sql
#     return cur.fetchall()  # 获取查询结果，输出元祖对象
#
#
# def otherMethod(sql):
#     '''
#     非查询方法（增删改）
#     :param sql: sql语句
#     :return: 无
#     '''
#     cur = createCur()
#     cur.execute(sql)
#
#
# if __name__ == '__main__':
#     db = connect_mysql()
#     # 查询方法
#     selectSql = "select * from test_datas"
#     print(selectMethod(selectSql)[0])
#     # 非查询方法
#     # insertSql =""
#     # otherMethod(insertSql, cur)
#     db.commit()
#     db.close()


import pymysql
import cx_Oracle
import os

# 在python文件中执行查询语句前添加编码格式（oracle语句查询，设置编码格式房子查询中文乱码）PS:查询oracle数据库的编码格式sql ：select userenv('language') from dual;
os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AL32UTF8'

def connect_mysql(type):
    # 连接mysql数据库
    conn = pymysql.Connect(host="192.168.100.55",
                         port=3306,
                         user="root",
                         password="root",
                         db="db_test_jk",
                         charset="utf8")
    if type == "caseDB":
        pass
    elif type == "ywDB":
        # 连接oracle数据库
        conn = cx_Oracle.connect("xz_timp35/ZZCWMFiehetf1ZbvaUBZp@192.168.0.94:1525/DAQDATA")  # conn = cx_Oracle.connect("用户名 / 密码 @ 主机ip地址：端口号 / oracle_service")
    return conn

def createCur(type):
    conn = connect_mysql(type)  # 数据库对象
    cur = conn.cursor()  # 创建游标，作用，启动/激活数据库
    return cur


def selectMethod(sql, type="caseDB"):
    '''
    查询方法
    :param sql: sql语句
    :return: 查询结果，元祖
    '''
    cur = createCur(type)
    cur.execute(sql)  # 执行sql
    return cur.fetchall()  # 获取查询结果，输出元祖对象


def otherMethod(sql, type="caseDB"):
    '''
    非查询方法（增删改）
    :param sql: sql语句
    :return: 无
    '''
    cur = createCur(type)
    cur.execute(sql)


if __name__ == '__main__':
    db = connect_mysql()
    # 查询方法
    selectSql = "select * from test_datas"
    print(selectMethod(selectSql)[0])
    # 非查询方法
    # insertSql =""
    # otherMethod(insertSql, cur)
    db.commit()
    db.close()

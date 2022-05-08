# -*- coding: utf-8 -*-
# @Time    : 2022/5/7 14:17
# @Author  : xyx
# @Description:

import time
import pymysql


def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年", "月", "日")


def get_conn():
    # 建立连接
    conn = pymysql.connect(host="127.0.0.1", user="root", password="12345678", db="shdata", charset="utf8")
    # 创建游标
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()


def query(sql, *args):
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res


def get_total_data():
    sql = "select time,sum(confirm),sum(wzz) from sh_cov group by time"
    res = query(sql)
    return res


def get_all_data():
    sql = "select * from sh_cov"
    res = query(sql)
    return res


def get_dic_total_data():
    sql = "select dic,sum(confirm),sum(wzz) from sh_cov group by dic"
    res = query(sql)
    return res


def get_today_data():
    sql = "select time,sum(confirm),sum(wzz) from sh_cov group by time order by time desc limit 1"
    res = query(sql)
    return res


if __name__ == '__main__':
    print(get_today_data())

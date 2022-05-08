# -*- coding: utf-8 -*-
# @Time    : 2022/5/7 13:46
# @Author  : xyx
# @Description:

import traceback
import pymysql
import pandas as pd
import requests


def getdata():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    url = 'http://m.sh.bendibao.com/news/249468.html'  # 3月数据
    url1 = 'http://m.sh.bendibao.com/news/250518.html'  # 4月数据
    url2 = 'http://m.sh.bendibao.com/news/251728.html'  # 5月数据
    data = []  # 保存数据
    # 数据库已存在3 4月份数据，只需更新五月份数据即可
    '''
    response = requests.get(url, headers=headers)
    html_doc = str(response.content, 'utf-8')
    df3 = pd.read_html(html_doc, encoding='utf-8')[0]
    df3 = df3.drop([0, len(df3) - 1, len(df3) - 2, len(df3) - 3]).fillna(value=0)

    df3.columns = df3.iloc[0]
    df3 = df3.drop([1])

    df3['时间'] = df3['时间'].apply(lambda x: pd.to_datetime('2022-03-' + x[:-1]))
    df3['时间'] = df3['时间'].dt.date
    qu = df3.columns[3:]

    
    for idx in range(0, len(df3), 2):
        idx = df3.index[idx]
        time = df3.loc[idx, '时间']

        for d in qu:
            data.append((time, d, df3.loc[idx, d], df3.loc[idx + 1, d]))
    #         print(time,d,df3.loc[idx,d],df3.loc[idx+1,d])

    response1 = requests.get(url1, headers=headers)
    html_doc1 = str(response1.content, 'utf-8')
    df4 = pd.read_html(html_doc1, encoding='utf-8')[0]
    df4 = df4.drop([0, len(df4) - 1, len(df4) - 2, len(df4) - 3]).fillna(value=0)

    df4.columns = df4.iloc[0]
    df4 = df4.drop([1])

    df4['时间'] = df4['时间'].apply(lambda x: pd.to_datetime('2022-04-' + x[:-1]))
    df4['时间'] = df4['时间'].dt.date

    for idx in range(0, len(df4), 2):
        idx = df4.index[idx]
        time = df4.loc[idx, '时间']

        for d in qu:
            #         print(time,d,df4.loc[idx,d],df4.loc[idx+1,d])
            data.append((time, d, df4.loc[idx, d], df4.loc[idx + 1, d]))
    '''

    response2 = requests.get(url2, headers=headers)
    html_doc2 = str(response2.content, 'utf-8')
    df5 = pd.read_html(html_doc2, encoding='utf-8')[0]
    df5 = df5.drop([0, len(df5) - 1, len(df5) - 2, len(df5) - 3]).fillna(value=0)

    df5.columns = df5.iloc[0]
    df5 = df5.drop([1])

    df5['时间'] = df5['时间'].apply(lambda x: pd.to_datetime('2022-05-' + x[:-1]))
    df5['时间'] = df5['时间'].dt.date
    qu = df5.columns[3:]
    for idx in range(0, len(df5), 2):
        idx = df5.index[idx]
        time = df5.loc[idx, '时间']

        for d in qu:
            #         print(time,d,df5.loc[idx,d],df5.loc[idx+1,d])
            data.append((time, d, df5.loc[idx, d], df5.loc[idx + 1, d]))
    return data


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


def update_data():
    conn, cursor = get_conn()
    try:
        data = getdata()
        conn, cursor = get_conn()
        sql = "insert into sh_cov value (%s,%s,%s,%s)"
        # 根据爬虫得到的最新数据数据表中查询是否包含此条记录，如果包含则不必插入数据，如果不包含则插入
        sql_query = "select confirm from sh_cov where time = %s and dic = %s"
        for d in data:
            # 如果不包含数据则返回None
            if not cursor.execute(sql_query, [d[0], d[1]]):
                cursor.execute(sql, d)
        conn.commit()
        print("数据获取成功！")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


if __name__ == '__main__':
    update_data()

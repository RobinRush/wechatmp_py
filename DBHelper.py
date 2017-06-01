# coding=gbk
__author__ = 'RobinLin'
import sqlite3
import time
from functools import wraps, partial


class Member:
    def __init__(self):
        self.user_name = None
        self.mobile = None
        self.wechat_id = None
        self.card_type = 1
        self.balance = 0.0
        self.exp = 0.0

    def to_value(self):
        ret_value = (
            self.user_name,
            self.mobile,
            self.wechat_id,
            self.card_type,
            self.balance,
            self.exp,
        )
        return ret_value


class helper():
    def __init__(self):
        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS user_account
                      (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                       user_name TEXT,
                       mobile TEXT UNIQUE,
                       wechat_id TEXT UNIQUE,
                       card_type INT,
                       balance REAL,
                       exp REAL
                       )''')
        conn.commit()
        conn.close()
        pass

    def query(self):
        conn = sqlite3.connect("data.db")
        print(conn)
        c = conn.cursor()
        c.execute('SELECT * FROM user_account')
        ret_list = c.fetchall()
        conn.commit()
        conn.close()
        return ret_list

    def add_member(self, member):
        conn = sqlite3.connect("data.db")
        print(conn)
        c = conn.cursor()
        try:
            ret = c.execute("INSERT INTO user_account VALUES (NULL, ?, ?, ?, ?, ?)", member)
            conn.commit()
        except:
            ret = None
            pass

        conn.close()
        return ret


h = helper()
m = Member()
m.user_name = 'eden'
m.mobile = '15858273513'
m.wechat_id = 'abd321dg0.0'
print(h.add_member(m.to_value()))
print(h.query())
h2 = helper()
print(h2.query())
#
# def run2():
#     l = []
#     for i in range(5000000):
#         l.extend([i])
#     return len(l)
#
#
# class ElapsedTime():
#
#     def __enter__(self):
#         self.start_time = time.time()
#         return self
#
#     def __exit__(self, exception_type, exception_value, traceback):
#         self.end_time = time.time()
#         print('运行花费时间：{:.6f}s'.format(self.end_time - self.start_time))
# conn = sqlite3.connect("test.db")
# with ElapsedTime(conn):
#     run2(conn)

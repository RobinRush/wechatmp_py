# coding=gbk
__author__ = 'RobinLin'
import sqlite3
import time
from functools import wraps, partial
import DBHelper_log

class Member:
    def __init__(self):
        self.id = None
        self.user_name = None
        self.mobile = None
        self.wechat_id = None
        self.card_type = 1
        self.balance = 0.0
        self.exp = 0.0

    def to_value(self):
        ret_value = (
            None,
            self.user_name,
            self.mobile,
            self.wechat_id,
            self.card_type,
            self.balance,
            self.exp,
        )
        return ret_value

    def build(self, item):
        self.id = item[0]
        self.user_name = item[1]
        self.mobile = item[2]
        self.wechat_id = item[3]
        self.card_type = item[4]
        self.balance = item[5]
        self.exp = item[6]

_conn = sqlite3.connect("data.db")
_c = _conn.cursor()
_c.execute('''CREATE TABLE IF NOT EXISTS user_account
                      (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                       user_name TEXT,
                       mobile TEXT UNIQUE,
                       wechat_id TEXT UNIQUE,
                       card_type INT,
                       balance REAL,
                       exp REAL
                       )''')
_conn.commit()
_conn.close()


# public
def add_user(member):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO user_account VALUES (?, ?, ?, ?, ?, ?, ?)", member.to_value())
        conn.commit()
        ret = True
    except:
        ret = False
        pass

    conn.close()
    return ret

# test = Member()
# test.mobile='123456'
# test.wechat_id='bac'
# print(add_member(test))

# public
def is_exsit(user_id):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute('SELECT * FROM user_account WHERE user_name=? OR mobile=? OR wechat_id=?', (user_id, user_id, user_id))
    ret_list = c.fetchmany(1)
    list_size = (len(ret_list))
    conn.commit()
    conn.close()
    if list_size > 0:
        return True
    return False


# public
def get_user(user_id):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute('SELECT * FROM user_account WHERE user_name=? OR mobile=? OR wechat_id=?', (user_id, user_id, user_id))
    ret_list = c.fetchmany(1)
    list_size = (len(ret_list))
    conn.commit()
    conn.close()
    if list_size == 0:
        return None
    item = ret_list[0]
    user = Member()
    user.build(item)
    return user
# print(get_user('15858273511'))

# public
def get_user_balance(user_id):
    user = get_user(user_id)
    if user is None:
        return 0
    return user.balance
# print(get_user_balance('15858273511'))

def _update_user(user):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute('UPDATE user_account SET user_name=?,mobile=?,wechat_id=?,card_type=?,balance=?,exp=? WHERE id=?',
              (user.user_name, user.mobile, user.wechat_id, user.card_type, user.balance, user.exp, user.id))
    conn.commit()
    conn.close()
    return

# public IMPORTANT
def charge(user_id, money):
    user = get_user(user_id)
    user.balance += money
    user.exp += money
    _update_user(user)
    log_action = '充值'
    DBHelper_log.add_action(log_action, money, user.user_name, user.mobile, user.wechat_id)
    return
# charge('bac', 10)

# public IMPORTANT
def cost(user_id, money):
    user = get_user(user_id)
    user.balance -= money
    user.exp += money
    _update_user(user)
    log_action = '消费'
    DBHelper_log.add_action(log_action, money, user.user_name, user.mobile, user.wechat_id)
    return


# public IMPORTANT
def add_exp(user_id, exp):
    user = get_user(user_id)
    user.exp += exp
    _update_user(user)
    log_action = '积分变更'
    DBHelper_log.add_action(log_action, exp, user.user_name, user.mobile, user.wechat_id)
    return

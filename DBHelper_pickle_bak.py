# coding=gbk
__author__ = 'RobinLin'
import sqlite3
import time
from functools import wraps, partial
import pickle


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
            self.card_type,
            self.balance,
            self.wechat_id
        )
        return ret_value


users_wechat = {}

try:
    pickle_file = open("users_wechat.txt", "rb")
    users_wechat = pickle.load(pickle_file)
    pickle_file.close()

except:
    users_wechat = {}

def save_users():
    pickle_file = open("users_wechat.txt", "wb")
    pickle.dump(users_wechat, pickle_file)
    pickle_file.close()

def query_wechat():
    return users_wechat

# public
def add_user( member):
    wx_id = member.wechat_id
    mobile = member.mobile
    if users_wechat.get(wx_id) is not None:
        return False
    if users_wechat.get(mobile) is not None:
        return False
    users_wechat[wx_id] = member
    users_wechat[mobile] = member
    save_users()
    return True

# public
def is_exsit(user_id):
    if users_wechat.get(user_id) is not None:
        return True
    if users_wechat.get(user_id) is not None:
        return True
    return False

# public
def get_user(user_id):
    return users_wechat.get(user_id)

# public
def get_user_balance( user_id):
    user = get_user(user_id)
    return user.balance

def set_user_balance(user_id, balance):
    user = get_user(user_id)
    wx_id = user.wechat_id
    mobile = user.mobile
    user.balance = balance
    users_wechat[wx_id] = user
    users_wechat[mobile] = user
    save_users()

# public
def charge(user_id, money):
    now_bala = get_user_balance(user_id)
    set_user_balance(user_id, now_bala+money)
    add_exp(user_id, money)

# public
def cost(user_id, money):
    now_bala = get_user_balance(user_id)
    set_user_balance(user_id, now_bala-money)
    add_exp(user_id, money)

def get_user_exp( user_id):
    user = get_user(user_id)
    return user.exp

def set_user_exp(user_id, exp):
    user = get_user(user_id)
    wx_id = user.wechat_id
    mobile = user.mobile
    user.exp = exp
    users_wechat[wx_id] = user
    users_wechat[mobile] = user
    save_users()

# public
def add_exp(user_id, exp):
    now_exp = get_user_exp(user_id)
    set_user_exp(user_id, now_exp+exp)
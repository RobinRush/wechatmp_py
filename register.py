# coding=gbk
__author__ = 'RobinLin'
'''
无状态：    action=0
注册中：    action=1001
'''
user_action_map = {}
import DBHelper_pickle


def register(user_id, msg, ret_msg):
    if msg.find('注册') == 0:
        # 注册
        if DBHelper_pickle.is_exsit(user_id):
            ret_msg[0] = '您已经注册了水帘洞的VIP会员，请输入【查询】查看您的信息'
            return True
        ret_msg[0] = '请输入您的手机号码，注册水帘洞VIP会员'
        user_action_map[user_id] = 1001
        return True
    elif user_action_map.get(user_id) is not None and user_action_map.get(user_id) == 1001:
        # 正在输入手机号
        try:
            int(msg)
        except:
            ret_msg[0] = '注册出错，请重新输入您的手机号'
            return True
        if DBHelper_pickle.is_exsit(msg):
            ret_msg[0] = '该手机号已被注册，如果确认是你的手机，请联系掌柜：17091609800，微信号：zhongdadan'
            user_action_map[user_id] = 0
            return True
        user = DBHelper_pickle.Member()
        user.wechat_id = user_id
        user.mobile = msg
        DBHelper_pickle.add_user(user)
        ret_msg[0] = '注册成功，恭喜您成为水帘洞的一员，爱你么么哒，掌柜的电话：17091609800'
        user_action_map[user_id] = 0
        return True
    return False

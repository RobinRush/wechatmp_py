# coding=gbk
__author__ = 'RobinLin'
import DBHelper_pickle
import admin_config
# 管理员微信id
admin_list = admin_config.admin_list
admin_action_map = {}
admin_charge_map = {}


def charge(user_id, msg, ret_msg):
    if msg.find('充值') == 0:
        if user_id not in admin_list:
            ret_msg[0] = '您不是管理员，充值请联系掌柜：17091609800，微信号：zhongdadan'
            return True
        ret_msg[0] = '猴王，你要给哪个手机号码充值？输入手机号'
        admin_action_map[user_id] = 1001
        return True
    elif admin_action_map.get(user_id) is not None and admin_action_map.get(user_id) == 1001:
        if user_id not in admin_list:
            ret_msg[0] = '您不是管理员，充值请联系掌柜：17091609800，微信号：zhongdadan'
            return True
        try:
            int(msg)
        except:
            ret_msg[0] = '手机号格式不对'
            return True
        if not DBHelper_pickle.is_exsit(msg):
            ret_msg[0] = '这个号码不是我们的会员，充值失败'
            admin_action_map[user_id] = 0
            return True
        ret_msg[0] = '充值多少？'
        admin_charge_map[user_id] = msg
        admin_action_map[user_id] = 1002
        return True
    elif admin_action_map.get(user_id) is not None and admin_action_map.get(user_id) == 1002:
        if user_id not in admin_list:
            ret_msg[0] = '您不是管理员，充值请联系掌柜：17091609800，微信号：zhongdadan'
            return True
        charge_value = 0.0
        try:
            charge_value = float(msg)
        except:
            ret_msg[0] = '金额格式不对'
            return True
        if charge_value < 0:
            ret_msg[0] = '金额必须大于0啊'
            return True
        charge_user_id = admin_charge_map.get(user_id)
        DBHelper_pickle.charge(charge_user_id, charge_value)
        admin_action_map[user_id] = 0
        ret_msg[0] = '给{}充值{}成功！'.format(charge_user_id, charge_value)
        return True
    return False


def query_command_list(user_id, msg, ret_msg):
    if msg.find('指令') == 0:
        # 指令
        ret_msg[0] = '指令列表：\n【查询】：查询会员信息\n【消费】：用于水帘洞付款、埋单\n其他任何问题，请联系水帘洞猴王。手机17091609800，微信号：zhongdadan'
        if user_id in admin_list:
            ret_msg[0] += '\n管理员指令：\n【充值】：对某手机号充值\n【修改经验】：修改某手机号的经验，可以为负数'
        return True
    return False


def add_exp(user_id, msg, ret_msg):
    if msg.find('修改经验') == 0:
        if user_id not in admin_list:
            ret_msg[0] = '您不是管理员，充值请联系掌柜：17091609800，微信号：zhongdadan'
            return True
        ret_msg[0] = '猴王，你要给哪个手机号码增加经验？输入手机号'
        admin_action_map[user_id] = 2001
        return True
    elif admin_action_map.get(user_id) is not None and admin_action_map.get(user_id) == 2001:
        if user_id not in admin_list:
            ret_msg[0] = '您不是管理员，充值请联系掌柜：17091609800，微信号：zhongdadan'
            return True
        try:
            int(msg)
        except:
            ret_msg[0] = '手机号格式不对'
            return True
        if not DBHelper_pickle.is_exsit(msg):
            ret_msg[0] = '这个号码不是我们的会员，增加经验失败'
            admin_action_map[user_id] = 0
            return True
        ret_msg[0] = '增加多少经验？可以为负数'
        admin_charge_map[user_id] = msg
        admin_action_map[user_id] = 2002
        return True
    elif admin_action_map.get(user_id) is not None and admin_action_map.get(user_id) == 2002:
        if user_id not in admin_list:
            ret_msg[0] = '您不是管理员，充值请联系掌柜：17091609800，微信号：zhongdadan'
            return True
        charge_value = 0.0
        try:
            charge_value = float(msg)
        except:
            ret_msg[0] = '经验数值格式不对'
            return True
        charge_user_id = admin_charge_map.get(user_id)
        DBHelper_pickle.add_exp(charge_user_id, charge_value)
        admin_action_map[user_id] = 0
        ret_msg[0] = '给{}修改经验{}点成功！'.format(charge_user_id, charge_value)
        return True
    return False


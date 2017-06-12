# coding=gbk
__author__ = 'RobinLin'
import DBHelper
import admin_config

user_action_map = {}

def exist(user_id, ret_msg):
    if DBHelper.is_exsit(user_id):
        return False
    ret_msg[0] = '亲爱的，你还没成为水帘洞的一员呢，快输入【注册】加入我们吧~'
    return True


def query(user_id, msg, ret_msg):
    if msg.find('查询') == 0:
        # 查询
        user = DBHelper.get_user(user_id)
        if user is None:
            ret_msg[0] = '亲爱的，你还没成为水帘洞的一员呢，快输入【注册】加入我们吧~'
            return True
        mobile = user.mobile
        balance = user.balance
        exp = user.exp
        ret_msg[0] = '亲爱的VIP\n您绑定的手机号：{}\n您的账户余额：{}元\n您的经验值：{}'.format(mobile, '%.2f' % balance, exp)
        return True
    return False


def cost(user_id, msg, ret_msg):
    if msg.find('消费') == 0:
        user_action_map[user_id] = 1001
        ret_msg[0] = '您消费了多少金额？'
        return True
    elif user_action_map.get(user_id) is not None and user_action_map.get(user_id) == 1001:
        try:
            float(msg)
        except:
            ret_msg[0] = '消费金额格式不对，请重新输入'
            return True
        cost_value = float(msg)
        now_bala = DBHelper.get_user_balance(user_id)
        if cost_value > now_bala:
            ret_msg[0] = 'oops...余额不足，消费失败\n余额：{}\n请联系猴王充值：17091609800，微信号：zhongdadan'.format('%.2f' % now_bala)
            user_action_map[user_id] = 0
            return True
        DBHelper.cost(user_id, cost_value)
        user_action_map[user_id] = 0
        user = DBHelper.get_user(user_id)
        ret_msg[0] = '消费成功，增加{}点经验值！\n欢迎下次光临\n余额：{}\n经验值：{}'.format(cost_value, '%.2f' % user.balance, user.exp)
        import itchat
        ret_list = itchat.search_friends(admin_config.admin_name)
        if len(ret_list) > 0:
            user_name = ret_list[0]['UserName']
            itchat.send_msg('顾客{}消费了{}金额。\n余额：{}\n经验值：{}'.format(user.mobile, cost_value, '%.2f' % user.balance, user.exp), user_name)
        return True
    return False
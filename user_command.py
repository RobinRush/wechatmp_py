# coding=gbk
__author__ = 'RobinLin'
import DBHelper

user_action_map = {}

def exist(user_id, ret_msg):
    if DBHelper.is_exsit(user_id):
        return False
    ret_msg[0] = '�װ��ģ��㻹û��Ϊˮ������һԱ�أ������롾ע�᡿�������ǰ�~'
    return True


def query(user_id, msg, ret_msg):
    if msg.find('��ѯ') == 0:
        # ��ѯ
        user = DBHelper.get_user(user_id)
        if user is None:
            ret_msg[0] = '�װ��ģ��㻹û��Ϊˮ������һԱ�أ������롾ע�᡿�������ǰ�~'
            return True
        mobile = user.mobile
        balance = user.balance
        exp = user.exp
        ret_msg[0] = '�װ���VIP\n���󶨵��ֻ��ţ�{}\n�����˻���{}Ԫ\n���ľ���ֵ��{}'.format(mobile, '%.2f' % balance, exp)
        return True
    return False


def cost(user_id, msg, ret_msg):
    if msg.find('����') == 0:
        user_action_map[user_id] = 1001
        ret_msg[0] = '�������˶��ٽ�'
        return True
    elif user_action_map.get(user_id) is not None and user_action_map.get(user_id) == 1001:
        try:
            float(msg)
        except:
            ret_msg[0] = '���ѽ���ʽ���ԣ�����������'
            return True
        cost_value = float(msg)
        now_bala = DBHelper.get_user_balance(user_id)
        if cost_value > now_bala:
            ret_msg[0] = 'oops...���㣬����ʧ��\n��{}\n����ϵ������ֵ��17091609800��΢�źţ�zhongdadan'.format(now_bala)
            user_action_map[user_id] = 0
            return True
        DBHelper.cost(user_id, cost_value)
        bala = DBHelper.get_user_balance(user_id)
        ret_msg[0] = '���ѳɹ�������{}�㾭��ֵ��\n��ӭ�´ι���\n��{}'.format(cost_value, bala)
        user_action_map[user_id] = 0
        return True
    return False
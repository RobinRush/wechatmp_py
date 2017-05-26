# coding=gbk
__author__ = 'RobinLin'
import DBHelper_pickle
import admin_config
# ����Ա΢��id
admin_list = admin_config.admin_list
admin_action_map = {}
admin_charge_map = {}


def charge(user_id, msg, ret_msg):
    if msg.find('��ֵ') == 0:
        if user_id not in admin_list:
            ret_msg[0] = '�����ǹ���Ա����ֵ����ϵ�ƹ�17091609800��΢�źţ�zhongdadan'
            return True
        ret_msg[0] = '��������Ҫ���ĸ��ֻ������ֵ�������ֻ���'
        admin_action_map[user_id] = 1001
        return True
    elif admin_action_map.get(user_id) is not None and admin_action_map.get(user_id) == 1001:
        if user_id not in admin_list:
            ret_msg[0] = '�����ǹ���Ա����ֵ����ϵ�ƹ�17091609800��΢�źţ�zhongdadan'
            return True
        try:
            int(msg)
        except:
            ret_msg[0] = '�ֻ��Ÿ�ʽ����'
            return True
        if not DBHelper_pickle.is_exsit(msg):
            ret_msg[0] = '������벻�����ǵĻ�Ա����ֵʧ��'
            admin_action_map[user_id] = 0
            return True
        ret_msg[0] = '��ֵ���٣�'
        admin_charge_map[user_id] = msg
        admin_action_map[user_id] = 1002
        return True
    elif admin_action_map.get(user_id) is not None and admin_action_map.get(user_id) == 1002:
        if user_id not in admin_list:
            ret_msg[0] = '�����ǹ���Ա����ֵ����ϵ�ƹ�17091609800��΢�źţ�zhongdadan'
            return True
        charge_value = 0.0
        try:
            charge_value = float(msg)
        except:
            ret_msg[0] = '����ʽ����'
            return True
        if charge_value < 0:
            ret_msg[0] = '���������0��'
            return True
        charge_user_id = admin_charge_map.get(user_id)
        DBHelper_pickle.charge(charge_user_id, charge_value)
        admin_action_map[user_id] = 0
        ret_msg[0] = '��{}��ֵ{}�ɹ���'.format(charge_user_id, charge_value)
        return True
    return False


def query_command_list(user_id, msg, ret_msg):
    if msg.find('ָ��') == 0:
        # ָ��
        ret_msg[0] = 'ָ���б�\n����ѯ������ѯ��Ա��Ϣ\n�����ѡ�������ˮ���������\n�����κ����⣬����ϵˮ�����������ֻ�17091609800��΢�źţ�zhongdadan'
        if user_id in admin_list:
            ret_msg[0] += '\n����Աָ�\n����ֵ������ĳ�ֻ��ų�ֵ\n���޸ľ��顿���޸�ĳ�ֻ��ŵľ��飬����Ϊ����'
        return True
    return False


def add_exp(user_id, msg, ret_msg):
    if msg.find('�޸ľ���') == 0:
        if user_id not in admin_list:
            ret_msg[0] = '�����ǹ���Ա����ֵ����ϵ�ƹ�17091609800��΢�źţ�zhongdadan'
            return True
        ret_msg[0] = '��������Ҫ���ĸ��ֻ��������Ӿ��飿�����ֻ���'
        admin_action_map[user_id] = 2001
        return True
    elif admin_action_map.get(user_id) is not None and admin_action_map.get(user_id) == 2001:
        if user_id not in admin_list:
            ret_msg[0] = '�����ǹ���Ա����ֵ����ϵ�ƹ�17091609800��΢�źţ�zhongdadan'
            return True
        try:
            int(msg)
        except:
            ret_msg[0] = '�ֻ��Ÿ�ʽ����'
            return True
        if not DBHelper_pickle.is_exsit(msg):
            ret_msg[0] = '������벻�����ǵĻ�Ա�����Ӿ���ʧ��'
            admin_action_map[user_id] = 0
            return True
        ret_msg[0] = '���Ӷ��پ��飿����Ϊ����'
        admin_charge_map[user_id] = msg
        admin_action_map[user_id] = 2002
        return True
    elif admin_action_map.get(user_id) is not None and admin_action_map.get(user_id) == 2002:
        if user_id not in admin_list:
            ret_msg[0] = '�����ǹ���Ա����ֵ����ϵ�ƹ�17091609800��΢�źţ�zhongdadan'
            return True
        charge_value = 0.0
        try:
            charge_value = float(msg)
        except:
            ret_msg[0] = '������ֵ��ʽ����'
            return True
        charge_user_id = admin_charge_map.get(user_id)
        DBHelper_pickle.add_exp(charge_user_id, charge_value)
        admin_action_map[user_id] = 0
        ret_msg[0] = '��{}�޸ľ���{}��ɹ���'.format(charge_user_id, charge_value)
        return True
    return False


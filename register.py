# coding=gbk
__author__ = 'RobinLin'
'''
��״̬��    action=0
ע���У�    action=1001
'''
user_action_map = {}
import DBHelper_pickle


def register(user_id, msg, ret_msg):
    if msg.find('ע��') == 0:
        # ע��
        if DBHelper_pickle.is_exsit(user_id):
            ret_msg[0] = '���Ѿ�ע����ˮ������VIP��Ա�������롾��ѯ���鿴������Ϣ'
            return True
        ret_msg[0] = '�����������ֻ����룬ע��ˮ����VIP��Ա'
        user_action_map[user_id] = 1001
        return True
    elif user_action_map.get(user_id) is not None and user_action_map.get(user_id) == 1001:
        # ���������ֻ���
        try:
            int(msg)
        except:
            ret_msg[0] = 'ע��������������������ֻ���'
            return True
        if DBHelper_pickle.is_exsit(msg):
            ret_msg[0] = '���ֻ����ѱ�ע�ᣬ���ȷ��������ֻ�������ϵ�ƹ�17091609800��΢�źţ�zhongdadan'
            user_action_map[user_id] = 0
            return True
        user = DBHelper_pickle.Member()
        user.wechat_id = user_id
        user.mobile = msg
        DBHelper_pickle.add_user(user)
        ret_msg[0] = 'ע��ɹ�����ϲ����Ϊˮ������һԱ������ôô�գ��ƹ�ĵ绰��17091609800'
        user_action_map[user_id] = 0
        return True
    return False

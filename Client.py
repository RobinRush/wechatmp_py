# coding=gbk
__author__ = 'RobinLin'
import register
import user_command
import admin_command

def get_input_command(user_id, msg):
    ret_msg = ['']
    if register.register(user_id, msg, ret_msg):
        # ע��
        pass
    elif user_command.exist(user_id, ret_msg):
        # �ж�һ�£��û��Ƿ�Ϊ��Ա
        pass
    elif user_command.query(user_id, msg, ret_msg):
        # ��ѯ
        pass
    elif user_command.cost(user_id, msg, ret_msg):
        # ����
        pass
    elif admin_command.charge(user_id, msg, ret_msg):
        # ����Ա
        pass
    elif admin_command.add_exp(user_id, msg, ret_msg):
        # ����Ա
        pass
    elif admin_command.query_command_list(user_id, msg, ret_msg):
        # ����Ա
        pass
    else:
        ret_msg[0] = '�������յ���лл~'
    pass
    return ret_msg[0]

# coding=gbk
__author__ = 'RobinLin'
import register
import user_command
import admin_command

def get_input_command(user_id, msg):
    ret_msg = ['']
    if register.register(user_id, msg, ret_msg):
        # 注册
        pass
    elif user_command.exist(user_id, ret_msg):
        # 判断一下，用户是否为会员
        pass
    elif user_command.query(user_id, msg, ret_msg):
        # 查询
        pass
    elif user_command.cost(user_id, msg, ret_msg):
        # 消费
        pass
    elif admin_command.charge(user_id, msg, ret_msg):
        # 管理员
        pass
    elif admin_command.add_exp(user_id, msg, ret_msg):
        # 管理员
        pass
    elif admin_command.query_command_list(user_id, msg, ret_msg):
        # 管理员
        pass
    else:
        ret_msg[0] = '留言已收到，谢谢~'
    pass
    return ret_msg[0]

# coding=gbk
__author__ = 'RobinLin'
import register
import user_command
import admin_command
import admin_config
import DBHelper


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
    elif user_command.set_mobile(user_id, msg, ret_msg):
        # 更改手机号
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
        user = DBHelper.get_user(user_id)
        if user is None:
            name = '未注册用户'
        else:
            name = user.mobile
        import itchat
        ret_list = itchat.search_friends(admin_config.admin_name)
        if len(ret_list) > 0:
            user_name = ret_list[0]['UserName']
            itchat.send_msg('顾客{}留言：{}'.format(name, msg), user_name)
        ret_msg[0] = '留言已收到，谢谢~'
    pass
    return ret_msg[0]

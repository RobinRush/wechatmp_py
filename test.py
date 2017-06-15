# coding=utf-8
__author__ = 'RobinLin'
import itchat
import itchatmp
import Client
import admin_config

itchatmp.update_config(itchatmp.WechatConfig(
    token=admin_config.token,
    appId=admin_config.appId,
    appSecret=admin_config.appSecret
    ))


@itchatmp.msg_register(itchatmp.content.INCOME_MSG)
def text_reply(msg):
    type = msg['MsgType']
    if type == 'text':
        print(msg)
        toUserName = msg['FromUserName']
        content = msg['Content']
        ret_msg = Client.get_input_command(toUserName, content)
        return ret_msg
    elif type == 'event':
        print(msg)
        content = msg['Event']
        if content == 'subscribe':
            return '欢迎关注【水帘洞】公众号，可以输入【指令】查看可以玩的内容。'
    return ''

itchat.auto_login(True)
itchatmp.run()


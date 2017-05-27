# coding=utf-8
__author__ = 'RobinLin'
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
    print(msg)
    type = msg['MsgType']
    if type == 'text':
        toUserName = msg['FromUserName']
        content = msg['Content']
        ret_msg = Client.get_input_command(toUserName, content)
        return ret_msg
    return ''

try:
    itchatmp.run()
except:
    import os
    os.system('TASKKILL /F /IM python.exe"')

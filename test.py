# coding=utf-8
__author__ = 'RobinLin'
import itchatmp
import Client

itchatmp.update_config(itchatmp.WechatConfig(
    token='robinrush',
    appId = 'wx652ddcf9dc1b3782',
    appSecret = '34d0a605a489bd692aef22bb9012c370',
    ))

@itchatmp.msg_register(itchatmp.content.INCOME_MSG)
def text_reply(msg):
    # print(msg)
    toUserName = msg['FromUserName']
    content = msg['Content']
    ret_msg = Client.get_input_command(toUserName, content)
    return ret_msg

try:
    # import itchat
    # itchat.auto_login(True)
    # list = itchat.search_friends(name='xxxman')
    # print(list)
    # robin = list[0]
    # print(robin)
    # uid = robin['UserName']
    # itchat.send('hello', uid)
    itchatmp.run()
except:
    import os
    os.system('TASKKILL /F /IM python.exe"')
    # itchatmp.run()

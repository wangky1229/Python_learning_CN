"""
用户身份验证

Version: 0.1
Author: 骆昊
"""
import msvcrt
import getpass
username = input('请输入用户名: ')
#password = input('请输入口令: ')
# 如果希望输入口令时 终端中没有回显 可以使用getpass模块的getpass函数

 password = getpass.getpass('请输入口令: ')
if username == 'admin' and password == '123456':
    print('身份验证成功!')
else:
    print('身份验证失败!')
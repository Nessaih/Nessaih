# coding: utf-8

import os
import re


file = os.popen('netsh wlan show profiles name="SEA-LEVEL" key=clear')

psw = re.search('关键内容\s*:(.*)', file.read())
print('Wifi密码: ',psw.group(1))
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2019/09/27 16:10:20
@Author  :   baoy.bao 
@Version :   1.0
@Contact :   zeroleavebaoy@163.com
@License :   (C)Copyright 2019-2021
@Desc    :   None
'''

# here put the import lib
import paramiko



ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.16.8.35', 12598, 'root', 'jhyf')
stdin, stdout, stderr = ssh.exec_command('df')
print(stdout.read())
ssh.close()
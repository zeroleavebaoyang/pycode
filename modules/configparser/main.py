#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2019/09/27 16:02:59
@Author  :   baoy.bao 
@Version :   1.0
@Contact :   zeroleavebaoy@163.com
@License :   (C)Copyright 2019-2021
@Desc    :   None
'''

# here put the import lib
import configparser

config = configparser.ConfigParser()    # 注意大小写
config.read('logging.ini', encoding='utf-8')

result = config.get('logger_root', 'level')
print(result)
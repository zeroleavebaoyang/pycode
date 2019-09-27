#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2019/09/27 15:13:19
@Author  :   baoy.bao 
@Version :   1.0
@Contact :   zeroleavebaoy@163.com
@License :   (C)Copyright 2019-2021
@Desc    :   如果你的应用使用的是Python 3.5及以上的版本（目前应该还很少），Python官方给出的建议是尽量使用subprocess.run()函数。
当subprocess.call()、subprocess.check_call()、subprocess.check_output()和subprocess.run()这些高级函数无法满足需求时，我们可以使用subprocess.Popen类来实现我们需要的复杂功能。
'''

# here put the import lib

import subprocess

#subprocess.check_call('dir D:\\dev\\workspaces\\python\\pycode\\modules\\os\\', shell=True)

p = subprocess.check_output('dir D:\\dev\\workspaces\\python\\pycode\\modules\\os\\')

print(p)
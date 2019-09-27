#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2019/09/27 15:55:33
@Author  :   baoy.bao 
@Version :   1.0
@Contact :   zeroleavebaoy@163.com
@License :   (C)Copyright 2019-2021
@Desc    :   None
'''

# here put the import lib
import json

_dict = {"name":"Tom", "age":23}
r = json.dumps(_dict)
print(r)

with open('test.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(_dict, indent=4))
    # json.dump(a,f,indent=4)   # 和上面的效果一样

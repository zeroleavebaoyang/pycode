#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2019/09/27 16:18:27
@Author  :   baoy.bao 
@Version :   1.0
@Contact :   zeroleavebaoy@163.com
@License :   (C)Copyright 2019-2021
@Desc    :   None
'''

# here put the import lib
import requests
import json
 
ret = requests.get('https://github.com/timeline.json')
 
print(ret.url)
print(ret.text)



payload = {'key1': 'value1', 'key2': 'value2'}
ret = requests.get("http://httpbin.org/get", params=payload)
 
print(ret.url)
print(ret.text)


# 1、基本POST实例
 
 
payload = {'key1': 'value1', 'key2': 'value2'}
ret = requests.post("http://httpbin.org/post", data=payload)
 
print(ret.text)
 
 
# 2、发送请求头和数据实例
 

 
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}
 
ret = requests.post(url, data=json.dumps(payload), headers=headers)
 
print(ret.text)
print(ret.cookies)
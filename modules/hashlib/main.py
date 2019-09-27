#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2019/09/27 11:53:04
@Author  :   baoy.bao 
@Version :   1.0
@Contact :   zeroleavebaoy@163.com
@License :   (C)Copyright 2019-2021
@Desc    :   None
'''

# here put the import lib
import hashlib



string = "123"


md5 = hashlib.md5()
md5.update(string.encode('utf-8'))     #注意转码
res = md5.hexdigest()
print("md5加密结果:",res)

# ######## sha1 ########

sha1 = hashlib.sha1()
sha1.update(string.encode('utf-8'))
res = sha1.hexdigest()
print("sha1加密结果:",res)

# ######## sha256 ########

sha256 = hashlib.sha256()
sha256.update(string.encode('utf-8'))
res = sha256.hexdigest()
print("sha256加密结果:",res)


# ######## sha384 ########

sha384 = hashlib.sha384()
sha384.update(string.encode('utf-8'))
res = sha384.hexdigest()
print("sha384加密结果:",res)

# ######## sha512 ########

sha512= hashlib.sha512()
sha512.update(string.encode('utf-8'))
res = sha512.hexdigest()
print("sha512加密结果:",res)




# ######## 更加安全的key加密 ########

low = hashlib.md5()
low.update('ab'.encode('utf-8'))
res = low.hexdigest()
print("普通加密:",res)

high = hashlib.md5(b'beyondjie')
high.update('ab'.encode('utf-8'))
res = high.hexdigest()
print("采用key加密:",res)
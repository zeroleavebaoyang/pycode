#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2019/09/24 10:52:37
@Author  :   baoy.bao 
@Version :   1.0
@Contact :   zeroleavebaoy@163.com
@License :   (C)Copyright 2019-2021
@Desc    :   None
'''

#os模块就是对操作系统进行操作，使用该模块必须先导入模块：
import os

#getcwd() 获取当前工作目录(当前工作目录默认都是当前文件所在的文件夹)
result = os.getcwd()
print(result)

#chdir()改变当前工作目录
# os.chdir('/home/sy')
# result = os.getcwd()
# print(result)

# open('02.txt','w')

#操作时如果书写完整的路径则不需要考虑默认工作目录的问题,按照实际书写路径操作
# open('/home/sy/下载/02.txt','w')

#listdir() 获取指定文件夹中所有内容的名称列表
# result = os.listdir('/home/sy')
# print(result)

#mkdir()  创建文件夹
#os.mkdir('girls')
#os.mkdir('boys',0o777)

#makedirs()  递归创建文件夹
#os.makedirs('/home/sy/a/b/c/d')

#rmdir() 删除空目录
#os.rmdir('girls')

#removedirs 递归删除文件夹  必须都是空目录
#os.removedirs('/home/sy/a/b/c/d')

#rename() 文件或文件夹重命名
#os.rename('/home/sy/a','/home/sy/alibaba'
#os.rename('02.txt','002.txt')

#stat() 获取文件或者文件夹的信息
result = os.stat('D:\\dev\\workspaces\\python\\pycode\\modules\\os\\main.py')
print(result)

#system() 执行系统命令(危险函数)
result = os.system('dir')  #获取隐藏文件
print(result)



#环境变量
'''
环境变量就是一些命令的集合
操作系统的环境变量就是操作系统在执行系统命令时搜索命令的目录的集合
'''
#getenv() 获取系统的环境变量
result = os.getenv('PATH')
print(result.split(':'))


#exit() 退出终端的命令

#os模块中的常用值
#curdir  表示当前文件夹   .表示当前文件夹  一般情况下可以省略
print(os.curdir)

#pardir  表示上一层文件夹   ..表示上一层文件夹  不可省略!
print(os.pardir)

#os.mkdir('../../../man')#相对路径  从当前目录开始查找
#os.mkdir('/home/sy/man1')#绝对路径  从根目录开始查找

#name 获取代表操作系统的名称字符串
print(os.name) #posix -> linux或者unix系统  nt -> window系统

#sep 获取系统路径间隔符号  window ->\    linux ->/
print(os.sep)

#extsep 获取文件名称和后缀之间的间隔符号  window & linux -> .
print(os.extsep)

#linesep  获取操作系统的换行符号  window -> \r\n  linux/unix -> \n
print(repr(os.linesep))

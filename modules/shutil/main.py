#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2019/09/27 16:08:52
@Author  :   baoy.bao 
@Version :   1.0
@Contact :   zeroleavebaoy@163.com
@License :   (C)Copyright 2019-2021
@Desc    :   None
'''

# here put the import lib
import shutil


'''
copy()
功能：复制文件
格式：shutil.copy('来源文件','目标地址')
返回值：复制之后的路径
copy2()
功能：复制文件，保留元数据
格式：shutil.copy2('来源文件','目标地址')
返回值：复制之后的路径
copyfileobj()
将一个文件的内容拷贝的另外一个文件当中
格式：shutil.copyfileobj(open(来源文件,'r'),open（'目标文件','w'）)
返回值：无
copyfile()
功能：将一个文件的内容拷贝的另外一个文件当中
格式:shutil.copyfile(来源文件,目标文件)
返回值：目标文件的路径
copytree()
功能：复制整个文件目录
格式:shutil.copytree(来源目录,目标目录)
返回值：目标目录的路径
注意：无论文件夹是否为空，均可以复制，而且会复制文件夹中的所有内容
copymode()
功能：拷贝权限
copystat()
功能：拷贝元数据（状态）
rmtree()
功能：移除整个目录，无论是否空
格式：shutil.rmtree(目录路径)
返回值：无
move()
功能：移动文件或者文件夹
格式：shutil.move(来源地址,目标地址)
返回值：目标地址
which()
功能：检测命令对应的文件路径
格式：shutil.which(‘命令字符串’)
返回值：命令文件所在位置
注意：window和linux不太一样。 window的命令都是.exe结尾，linux则不是
disk_usage()
功能：检测磁盘使用信息
格式：disk_usage(‘盘符’)
返回值：元组


归档和解包操作
归档：将多个文件合并到一个文件当中，这种操作方式就是归档。

解包：将归档的文件进行释放。

压缩：压缩时将多个文件进行有损或者无损的合并到一个文件当中。

解压缩：就是压缩的反向操作，将压缩文件中的多个文件，释放出来。

注意：压缩属于归档！
make_archive()
功能：归档函数，归档操作
格式：shutil.make_archive('目标文件路径','归档文件后缀','需要归档的目录')
返回值：归档文件的最终路径
unpack_archive()
功能：解包操作
格式：shutil.unpack_archive('归档文件路径','解包目标文件夹')
返回值:None
注意：文件夹不存在会新建文件夹
get_archive_formats()
功能：获取当前系统已注册的归档文件格式（后缀）
格式：shutil.get_archive_formats()
返回值：列表   [(后缀,解释),(后缀,解释),(后缀,解释)...]
get_unpack_formats()
功能：获取当前系统已经注册的解包文件格式(后缀)
格式:shutil.get_unpack_formats()
返回值：列表   [(后缀,解释),(后缀,解释),(后缀,解释)...]
 

'''
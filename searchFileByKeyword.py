# -*- coding: UTF-8 -*-
#__author__ = 'zeroleavebaoyang@gmail.com'

import sys
import os

filterType = ['gif', 'png', 'bmp', 'jpg', 'jpeg', 'rar', 'zip', 'ico', 'apk', 'ipa', 'doc', 'docx', 'xls', 'jar', 'xlsx', 'ppt', 'pptx', 'pdf', 'gz', 'pyc', 'class']


def searchDir(path, keyword):
    arr = path.split('\\')
    if not arr[-1].startswith('.'):
        if os.path.isdir(path):
            folderList = os.listdir(path)
            for x in folderList:
                searchDir(path + '\\' +  x, keyword)
        elif os.path.isfile(path):
            searchContent(path, keyword)


def searchContent(path, keyword):
    if path.split('.')[-1] in filterType:
        return
    fh = open(path, 'r')
    content = fh.readlines()
    fh.close
    for index, x in enumerate(content):
        if keyword in x:
            print('%s     %s' % (path, index + 1))
        pass
    pass


if __name__ == "__main__":
    searchDir('D:\\dev\\workspaces\\python', 'keyword')

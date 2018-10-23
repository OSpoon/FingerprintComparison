#!/usr/bin/env python
# encoding: utf-8

"""
@author: Spoon
@contact: zxin088@gmail.com
@file: InitDir.py
@time: 2018/10/23 18:02
@desc:
"""

import os

if __name__ == '__main__':
    if not os.path.exists(os.getcwd()+'/all/dist'):
        os.makedirs('all/dist')
    if not os.path.exists(os.getcwd() + '/diff'):
        os.makedirs('diff')
    if not os.path.exists(os.getcwd() + '/old'):
        os.makedirs('old')
    input("执行完毕 ==> Prease <enter>")

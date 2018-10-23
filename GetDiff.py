#!/usr/bin/env python
# encoding: utf-8
'''
@author: Spoon
@contact: zxin088@gmail.com
@file: GetDiff.py
@time: 2018/10/23 18:02
@desc:
'''

import os
import json
import shutil


'''
统计差异文件
1.旧指纹文件不存在的文件指纹进行记录
2.旧指纹文件存在但指纹不一致的进行记录
'''
def get_diff_list():
    diff_list = []
    ishave_old = os.path.exists(os.getcwd() + '/old/manifest.config')
    ishave_all = os.path.exists(os.getcwd() + '/all/manifest.config')
    if not ishave_old:
        print('请确认old目录中指纹文件(manifest.config)是否存在')
    if not ishave_all:
        print('请确认all目录中指纹文件(manifest.config)是否存在')
    if ishave_old and ishave_all:
        with open('old/manifest.config', 'r', encoding='utf-8') as old_rf, \
                open('all/manifest.config', 'r', encoding='utf-8') as all_rf:
            old_dict = json.loads(old_rf.read())
            all_dict = json.loads(all_rf.read())
            for all_key in all_dict.keys():
                # 旧指纹文件不存在的文件指纹进行记录
                if old_dict.get(all_key) is None:
                    diff_list.append(all_key)
                else:
                    # 旧指纹文件存在但指纹不一致的进行记录
                    if all_dict.get(all_key) != old_dict.get(all_key):
                        diff_list.append(all_key)
            return diff_list


'''
输出差异文件
'''
def output():
    diff_list = get_diff_list()
    if diff_list:
        for item in diff_list:
            diff_path = os.getcwd() + '/diff/dist/' + os.path.dirname(item)
            ishave = os.path.exists(diff_path)
            if not ishave:
                os.makedirs(diff_path)
            result = shutil.copyfile('all/dist' + item, 'diff/dist' + item)
            print('输出到diff目录 => ' + result)
        print('差异文件提取完成')
    else:
        print('无差异文件')


'''
获取差异文件
'''
def get_diff():
    output()


if __name__ == '__main__':
    get_diff()
    input("执行完毕 ==> Prease <enter>")

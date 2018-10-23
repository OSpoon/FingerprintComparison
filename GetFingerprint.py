import hashlib
import os
import json

file_list = []

'''
获取输入路径文件的指纹
'''
def get_file_md5(filepath):
    if not os.path.isfile(filepath):
        return
    myhash = hashlib.md5()
    f = open(filepath, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()


'''
遍历当前输入目录下ALL文件
'''
def traverse(f):
    fs = os.listdir(f)
    for f1 in fs:
        tmp_path = os.path.join(f, f1)
        if not os.path.isdir(tmp_path):
            file_list.append(tmp_path)
        else:
            traverse(tmp_path)

'''
输出指纹文件
'''
def output(file_path):
    traverse(file_path)
    print('统计文件总数: ' + str(file_list.__len__()) + '   ' + str(file_list.__len__() * 2))
    ishave = os.path.exists(os.getcwd() + '/all/manifest.config')
    if ishave:
        # 清空已生成的指纹统计文件
        os.remove(os.getcwd() + '/all/manifest.config')
    dict = {}
    for path in file_list:
        md5 = get_file_md5(path)
        dict[path.split('dist')[1]] = md5
        print('文件 : ' + path.split('dist')[1] + '\n指纹 : ' + md5)
    with open('all/manifest.config', 'a+', encoding='utf-8') as wf:
        wf.write(json.dumps(dict))
    print('文件MD5值统计完成')


def get_fingerprint(path):
    ishave = os.path.exists(path)
    if not ishave:
        print('请确认文件是否已放置完成')
    else:
        output(path)


if __name__ == '__main__':
    get_fingerprint(os.getcwd() + '/all/dist')
    input("执行完毕 ==> Prease <enter>")

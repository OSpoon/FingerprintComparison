##### 源码

##### GetFingerprint.py 获取文件夹内文件指纹(MD5值)

    #!/usr/bin/env python
    # encoding: utf-8

    """
    @author: Spoon
    @contact: zxin088@gmail.com
    @file: GetFingerprint.py
    @time: 2018/10/23 18:02
    @desc:
    """

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


    '''
    获取指纹
    '''


    def get_fingerprint(path):
        ishave = os.path.exists(path)
        if not ishave:
            print('请确认文件是否已放置完成')
        else:
            output(path)


    if __name__ == '__main__':
        get_fingerprint(os.getcwd() + '/all/dist')
        input("执行完毕 ==> Prease <enter>")

##### GetDiff.py 获取指纹不一致文件

    #!/usr/bin/env python
    # encoding: utf-8


    """
    @author: Spoon
    @contact: zxin088@gmail.com
    @file: GetDiff.py
    @time: 2018/10/23 18:02
    @desc:
    """

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

##### InitDir.py 初始化目录

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

##### 使用说明

##### 一、初始化项目目录

1. 如项目目录不存在all,diff,old目录时可执行InitDir.py文件

##### 二、第一次执行获取初始文件指纹

1. 需将要进行对比的文件目录放置all/dist文件夹

2. 执行GetFingerprint.py文件,提取成功会在all/dist下生成manifest.config文件

3. 将生成的manifest.config文件复制到old目录

##### 三、第二次执行进行新旧文件对比

1. 需将要进行对比的文件目录再次放置all/dist文件夹

2. 执行GetFingerprint.py文件,提取成功会在all/dist下生成manifest.config文件

3. 确保old目录下存在上次复制进去的manifest.config文件

4.  执行GetDiff.py文件,如检测到存在差异文件会输出到diff目录


##### [文件指纹验证](https://baike.baidu.com/item/%E6%96%87%E4%BB%B6%E6%8C%87%E7%BA%B9%E9%AA%8C%E8%AF%81/6027261 "文件指纹验证")

  - 当你从网络上下载了软件后，想确保此软件没有被人修改过（如添加了木马/病毒/非官方插件），或在下载中被破坏，可以用文件指纹验证（MD5）技术进行确认。

  - 通过某种算法，对具体的文件进行校验，得出了一个32位的十六进制数（校验和）。待校验文件的文件名和后缀名都可以更改，不影响校核。由于原来的信息只要有稍许改动，通过md5运算后，结果都会有很大的改变。所以，如果再次校验以后所得到的值（md5代码）和此软件发布站或官方网站公布的值不同，就可以认为，文件已被改动过。

  注:内容来自百度百科
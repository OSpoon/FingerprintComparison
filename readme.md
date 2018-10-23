### 使用说明

##### 一、初始化项目目录

    如项目目录不存在all,diff,old目录时可执行init_dir.py文件

##### 二、第一次执行获取初始文件指纹

    1、需将要进行对比的文件目录放置all/dist文件夹

    2、执行GetFingerprint.py文件,提取成功会在all/dist下生成manifest.config文件

    3、将生成的manifest.config文件复制到old目录

##### 三、第二次执行进行新旧文件对比

    1、需将要进行对比的文件目录再次放置all/dist文件夹

    2、执行GetFingerprint.py文件,提取成功会在all/dist下生成manifest.config文件

    3、确保old目录下存在上次复制进去的manifest.config文件

    4、执行GetDiff.py文件,如检测到存在差异文件会输出到diff目录


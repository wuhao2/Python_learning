# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/20 10:42'
import tarfile
import os


def tarXml(tfname):
    tf = tarfile.open(tfname, "w:gz")
    for fname in os.listdir('../regular_file/'):  # 遍历regular_file目录中的所有文件
    # for fname in os.listdir('.'):  # 遍历当前目录中的所有文件
        if fname.endswith('.xml'):  # 找到xml文件
            tf.add(fname)  # 加入到tar文件中
            # os.remove(fname)  # 删除
    tf.close()
    if not tf.members:  # 如果目录中一个xml文件都没有，则tar包也是空的，删除掉tar包
        os.remove(tfname)
    print("done tar......")
tarXml('test.tgz')
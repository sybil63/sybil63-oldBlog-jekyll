# -*- coding: utf8 -*-
from upyun import UpYun,md5,md5file
import sys

if __name__ == '__main__':
    imgDir = './images';

    u = UpYun('sybil-blog','sybil63','cx1121212231')

    #开启调试
    u.debug = True

    #查看版本信息
    print u.version()

    #设定api所调用的域名
    u.setApiDomain('v0.api.upyun.com')

    #创建目录
    a = u.mkDir('/testa')
    a = u.mkDir('/test')
    print a
    #a = u.mkDir('/a/b/c', True) 可自动创建父级目录（最多10级）

    #显示目录下的文件
    a = u.readDir('/')
    for i in a:
        print i.filename

    data = open(sourceFile,'rb')
    #设置待上传文件的 Content-MD5 值
    #如又拍云服务端收到的文件MD5值与用户设置的不一致，将回报 406 Not Acceptable 错误
    u.setContentMD5(md5file(data))

    #置待上传文件的 访问密钥（注意：仅支持图片空！，设置密钥后，无法根据原文件URL直接访问，需带 URL 后面加上 （缩略图间隔标志符+密钥） 进行访问）
    #如缩略图间隔标志符为 ! ，密钥为 bac，上传文件路径为 /folder/test.jpg ，那么该图片的对外访问地址为： http://空间域名/folder/test.jpg!bac
    #u.setFileSecret('bbbb')

    #开始上传文件
    a = u.writeFile(destFile, data)
    print a
    #a = u.writeFile('/a/b/c/d/e/f/g/logo.jpg',data, True) 可自动创建父级目录（最多10级）

    #获取上传后的图片信息（仅图片空间有返回数据）
    print(u.getWritedFileInfo('x-upyun-width')) # 图片宽度
    print(u.getWritedFileInfo('x-upyun-height')) # 图片高度
    print(u.getWritedFileInfo('x-upyun-frames')) # 图片帧数
    print(u.getWritedFileInfo('x-upyun-file-type')) # 图片类型

    #获取文件信息
    print u.getFileInfo(destFile)

    #a = u.writeFile('/testd.jpg','sdfsdf')
    #print a
    #a = u.deleteFile('/testd.jpg')
    #print a
    a = u.readDir('/')
    if a:
        for i in a:
            print i.filename
    else : 
        print a


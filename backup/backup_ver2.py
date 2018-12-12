#!/usr/bin/env python
# coding=utf-8

import os
import time

#源目录
source='/root/docker/'

#目的目录
target_dir='/home/lijinian/backup/'


#如果目标目录不存在则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

#以当前日期作为主备份目录下的子目录名称
today=target_dir+os.sep+time.strftime('%Y%m%d')

#将当前时间作为zip文件的文件名
now=time.strftime('%H%M%S')

#zip文件名称格式
target=today+os.sep+now+'.zip'

#如果子目录不存在则创建
if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory',today

#打包
zip_command = 'zip -r {0} {1}'.format(target,''.join(source))

#备份
print 'Zip command is:',zip_command
print 'Running:',
if os.system(zip_command)==0:
    print 'Successful backup to',target
else:
    print 'Backup Failed.'

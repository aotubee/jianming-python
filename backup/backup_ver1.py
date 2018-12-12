#!/usr/bin/env python
# coding=utf-8

import os
import time

#源目录
source='/root/docker/'

#目的目录
target_dir='/home/lijinian/backup/'


#备份文件
target=target_dir+os.sep+time.strftime('%Y%m%d%H%M%S')+'.zip'


#如果目标目录不存在则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

#打包
zip_command = 'zip -r {0} {1}'.format(target,''.join(source))

#备份
print 'Zip command is:',zip_command
print 'Running:',
if os.system(zip_command)==0:
    print 'Successful backup to',target
else:
    print 'Backup Failed.'

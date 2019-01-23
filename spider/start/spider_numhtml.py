#!/usr/bin/env python
# coding=utf-8

import requests
import re


class Spider:

    def __init__(self):
       self.page=40001
       self.switch=True

    def loadPage(self):
        """下载页面"""
        print  "正在下载页面..."
        url='https://bh.sb/post/'+str(self.page)+'/'
        print url
        response=requests.get(url)
        status=response.status_code
        if status==200:
            print "下载成功"

        #获取网页内容：
        content=response.content


        #设置分割字符串
        string='<article class="article-content">.*?</article>'

        #通过正则表达式进行筛选内容
        pattern=re.compile(string,re.S)
        content_list=pattern.findall(content)

        #调用下面的处理方法：
        self.dealPage(content_list)


    def dealPage(self,content_list):
        """处理网页内容，获取所需内容"""
        for item in content_list:
        #替换遍历后的段落中不要的字符
            item=item.replace('<p>',"").replace('<article class="article-content"> <img src="https://wx1.sinaimg.cn/mw690/6f077982gy1fvsd543skyj21jk0v9b29.jpg" alt="image">',"")
            item=item.replace('</p>',"\n")
            item=item.replace('未经允许不得转载：<a href="https://bh.sb">博海拾贝</a> &raquo; <a href="https://bh.sb/post/40001/">微语录精选1101：您愿望单中的8件商品正在促销!</a>',"")
            item=item.replace('<br />',"").replace('</article>',"")
            #print item
            #调用下面的写入方法：
            self.writePage(item)

    def writePage(self,item):
        """将处理后的数据写入指定文件中"""
        with open("duanzi.txt",'a+') as f:
            f.write(item)

    def startWork(self):
        while self.switch:
            self.loadPage()
            command=raw_input("如果继续，请输入回车，退出输入quit:")
            if command=="quit":
                self.switch=False

if __name__=="__main__":
    spider=Spider()
    spider.startWork()

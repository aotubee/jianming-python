#!/usr/bin/env python
# coding=utf-8

import re
import requests

class Spider:
    def __init__(self):
       self.switch=True

    def getHtml(self):
        """获取网页地址"""

        #主页
        response=requests.get('https://bh.sb/post/category/main/')
        index=response.content

        #筛选所需地址
        html="https://bh.sb/post/\d+"
        pattern=re.compile(html,re.S)
        content_list=pattern.findall(index)

        #去重
        content_list=list(set(content_list))

        #所爬网页筛选
        content_len=len(content_list)
        for num in range(content_len):
            req=content_list[num]
            response=requests.get(req)

            global load
            load=req
            #筛选出所爬网页
            content=response.content

            self.loadPage(content)


    def loadPage(self,content):
        """下载页面"""
        print  "正在下载页面:",load
        #匹配所需内容
        sp='<article class="article-content">(.*?)</article>'

        #通过正则表达式进行内容筛选
        pattern=re.compile(sp,re.S)
        content_list=pattern.findall(content)

        self.dealPage(content_list)

    def dealPage(self,content_list):
        """处理网页内容，获取所需文字"""
        for item in content_list:
            #过滤掉无用信息
            #pattern=re.compile('<img.*?/>',re.S)
            #m=pattern.sub('',item)
            item=re.sub('<img.*?>','',item)
            item=re.sub('<a.*?</a>','',item,re.S)
            item=re.sub('<a.*?>.*?</a>','',item,re.S)
            item=re.sub('<.*?>','',item,re.S)
            item=re.sub('<strong>.*?</strong>','',item,re.S)
            item=item.replace(' style="text-align: left;"','').replace('<p>','').replace('</p>','').replace('<br />','').replace('&raquo;','').replace('未经允许不得转载：','')

        self.writePage(item)

    def writePage(self,item):
        """将处理后的数据写入指定文件中"""
        with open("bohaishibei.txt",'a+') as f:
            f.write(item)

if __name__=="__main__":

    spider=Spider()
    spider.getHtml()

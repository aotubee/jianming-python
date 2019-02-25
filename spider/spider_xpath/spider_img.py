#!/usr/bin/env python
# coding=utf-8

import requests
import re,os
from lxml import etree


class Spider:

    def loadPage(self):
        """下载页面"""
        #首页
        url='https://tieba.baidu.com/f?ie=utf-8&kw=%E7%81%AB%E5%BD%B1&fr=search'
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        request=requests.get(url,headers=headers)
        html=request.content
        #筛选出子页面地址
        selector=etree.HTML(html)
        links=selector.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/@href')

        self.dealPage(links)

    def dealPage(self,links):
        """处理网页内容"""
        for link in links:
            #获取页面完整地址
            img_url='https://tieba.baidu.com/'+link
            #处理页面
            img_HTML=requests.get(img_url)
            img_links=etree.HTML(img_HTML.content).xpath('//img[@class="BDE_Image"]/@src')
            self.writePage(img_links)

       # for page in range(len(links)):
       #     if page < 2:
                #command=raw_input("如果继续，请输入回车，退出输入quit:")

    def writePage(self,img_links):
        """将数据写入指定文件中"""
        #处理图片地址，返回地址请求信息
        for img_link in img_links:
            req=requests.get(img_link)
            img=req.content

            #命名图片地址并写入文件
            #检测指定目录是否存在,若不存在则创建
            path='./image'
            if not os.path.exists(path):
                os.mkdir(path)
                print "新建文件夹："+path
            filename=img_link[-10:]
            with open('./image/'+filename,'wb') as f:
                f.write(img)
                print "图片下载："+filename

    def startWork(self):
        self.loadPage()

if __name__=="__main__":
    spider=Spider()
    spider.startWork()

#!/usr/bin/env python
# coding=utf-8

import requests
import urllib
import re,os
from lxml import etree


class Spider:

    def loadPage(self,url):
        """下载页面"""
        #首页
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        request=requests.get(url,headers=headers)
        html=request.content
        #筛选出子页面地址
        selector=etree.HTML(html)
        links=selector.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/@href')
        for link in links:
            fulllink='https://tieba.baidu.com/'+link
            self.dealPage(fulllink)

    def dealPage(self,fulllink):
        """处理网页内容"""
        #处理页面
        img_HTML=requests.get(fulllink)
        img_links=etree.HTML(img_HTML.content).xpath('//img[@class="BDE_Image"]/@src')
        self.writePage(img_links)

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
        bPage=int(raw_input("请输入起始页："))
        ePage=int(raw_input("请输入结束页："))
        url='https://tieba.baidu.com/f?'
        kw=raw_input("输入贴吧名：")
        key=urllib.urlencode({"kw":kw})
        #要爬取的贴吧地址
        fullurl=url+key
        #帖子页面设置
        for page in range(bPage,ePage+1):
            pn=(page-1)*50
            #实际爬取的页面地址，交给下面的方法进程处理。
            img_url=fullurl+"&pn="+str(pn)
            print img_url
            self.loadPage(img_url)

if __name__=="__main__":
    spider=Spider()
    spider.startWork()


#!/usr/bin/env python
# coding=utf-8
#!/usr/bin/env python2
# -*- coding=utf-8 -*-

'''使用进程模式爬取豆瓣电影名字和评分'''

from multiprocessing import Process, Queue

import time
from lxml import etree
import requests


class Spider(Process):
    def __init__(self, url, q):
        #重写父类__init__方法：
        super(Spider, self).__init__()
        self.url = url
        self.q = q
        self.headers={
            'Host':'movie.douban.com',
            'Referer':'https://movie.douban.com/top250?start=225&filter=',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        }

    def run(self):
        '''定义一个方法调用网页处理方法：'''
        self.dealPage()

    def dealPage(self):
        '''使用xpath对网页进行处理,筛选电影评分和名字'''
        response = requests.get(url=self.url,headers=self.headers).content
        html = etree.HTML(response)
        node_list = html.xpath("//div[@class='info']")
        for move in node_list:
            title=move.xpath('.//a/span[@class="title"][1]/text()')[0]
            score=move.xpath('.//span[@class="rating_num"]/text()')[0]
            self.q.put(score + "\t" + title)


#创建一个方法调用类
def main():
    #创建队列来保存进程获取到的数据
    q = Queue()
    base_url = 'https://movie.douban.com/top250?start='
    url_list = [base_url+str(num) for num in range(0,225+1,25)]

    #保存进程
    Process_list = []

    for url in url_list:
        p = Spider(url,q)
        #启动进程
        p.start()
        Process_list.append(p)

    for i in Process_list:
        #让主进程等待子进程执行完成
        i.join()

    while not q.empty():
        print q.get()

if __name__=="__main__":
    #开始时间
    start = time.time()
    #执行方法
    main()
    #当前时间减去开始时间
    print '[info]耗时：%s'%(time.time()-start)


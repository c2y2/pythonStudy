#!/usr/bin/env python
# encoding: utf-8

import urllib2

headers={
         'Cache-Control':'max-age=0',
         'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
         'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36',
         'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2'
         }

def classReques(url,data,header):
        request=urllib2.Request(url,data,header)
        res=urllib2.urlopen(request,timeout=6000)
        content=res.readlines()
        for i in content:
            print i
        
if __name__ == '__main__':
    url="http://www.baidu.com"
    classReques(url, None, header=headers)
    
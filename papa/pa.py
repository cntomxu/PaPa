#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import requests
import random

# 定义HTTP请求使用的 User Agent
USER_AGENTS = [ 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)'
               ,'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)'
               ,'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'
               ,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'
               ,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31'
               ,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:9.0.1) Gecko/20100101 Firefox/9.0.1'
               ,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8) AppleWebKit/536.25 (KHTML, like Gecko) Version/6.0 Safari/536.25'
              ]

class Pa:
  def __init__(self):
    pass

  def get(self, url):
    return requests.get(url, headers=self._headers())

  def post(self, url):
    return requests.post(url, headers=self._headers())

  def _headers(self):
    """ Custom headers
    """
    return {
      'User-Agent': self._randomUserAgent()
    }

  def _randomUserAgent(self):
    """ Get random user-agent
    """
    index = random.randint(0, len(USER_AGENTS) -1)
    return USER_AGENTS[index]


if __name__ == "__main__":
  # 设置系统编码为utf-8
  if sys.getdefaultencoding() is not 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8') 

  #r = requests.get('http://localhost:3000/login')
  #print r.status_code
  pa = Pa()
  res = pa.get("http://localhost:3000/login")
  #print res.encoding
  print res.text
   
  # TODO: 追加测试页到本地服务器
  # TODO: 解析内容



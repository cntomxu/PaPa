#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import re
import random
import logging
import requests
from pyquery import PyQuery as pq


# 定义HTTP请求使用的 User Agent
USER_AGENTS = [ 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)'
               ,'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)'
               ,'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'
               ,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'
               ,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31'
               ,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:9.0.1) Gecko/20100101 Firefox/9.0.1'
               ,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8) AppleWebKit/536.25 (KHTML, like Gecko) Version/6.0 Safari/536.25'
              ]

MAIN_URL = "xxxxxxx"


class Log:
  logger = None
  def __init__(self):
    level = logging.DEBUG
    logger = logging.getLogger('PaPaLogger')
    logger.setLevel(level)
    # 创建日志文件的Handler
    fh = logging.FileHandler('papa.log')
    fh.setLevel(level)
    # 创建命令行的Handler
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # 定义输出格式
    outFormatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(outFormatter)
    ch.setFormatter(outFormatter)

    logger.addHandler(fh)
    logger.addHandler(ch)
    Log.logger = logger
logger = Log().logger

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

class Target:
  def __init__(self):
    self.pa = Pa()

  def parseTop(self):
    res = self.pa.get("http://localhost:3000/top.html")
    
    d = pq(res.text)
    f50links = d('.f50list').find('a')
    for link in f50links:
      if link is not "#":
        print MAIN_URL + pq(link).attr('href')

  def parseList(self):
    res = self.pa.get("http://localhost:3000/a.html")

    d = pq(res.text)
    items = d('.list_type_pt_02').find('a')
    for item in items:
      a = pq(item)
      link = a.attr('href')
      text = a.text()

      # 拆分取得日文和英文名。
      m = re.search(r'（.*）', text.encode('utf-8'))
      if m:
        name_en = m.group(0)
        name_ja = text.replace(name_en, '')
        name_en = name_en[len('（') : len(name_en) - len('）')] # 移除左右括号
      else:
        name_en = ""
        name_ja = ""

      print "JA: " + name_ja  + "    " + "EN: "  + name_en  + "    LINK: " + MAIN_URL + link

  def parseDesc1(self):
    res = self.pa.get("http://localhost:3000/a_1.html")    

    d = pq(res.text)
    rows = d('.talent_detail').find('tr')
    for row in rows:
      tr = pq(row)
      title = tr.find('th').text()

      country = ""
      genre = ""
      # 解析Title
      if cmp(title, 'ブランド名') == 0:
        country = tr.find('a').text()
        print country
      elif cmp(title, 'カテゴリ') == 0:
        genre_links = tr.find('a')
        for link in genre_links:
          a = pq(link)
          genre_text = a.text()
          genre_link = a.attr('href')
        print genre_text + "   " + genre_link
      elif cmp(title, 'ブランド詳細') == 0:
        print 'ブランド詳細'
      elif cmp(title, '公式HP') == 0:
        print '公式HP'

if __name__ == "__main__":
  # 设置系统编码为utf-8
  if sys.getdefaultencoding() is not 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8') 

  #r = requests.get('http://localhost:3000/login')
  #print r.status_code
   
  # TODO: 追加测试页到本地服务器
  # TODO: 解析内容
  #target = Target()
  #target.parseTop()
  #target.parseList()
  #target.parseDesc1()

  #logger.info("ddd")



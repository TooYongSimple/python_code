#coding=utf-8  
import urllib2
import re
from bs4 import BeautifulSoup
import pycurl
import StringIO  #这个用到里面的write函数

def get_image(url):
	req = urllib2.urlopen(url)
	buf = req.read()
	return re.findall(r'http://.+\.jpg', buf)

def get_tieba_image(url):
	req = urllib2.urlopen(url)
	buf = req.read()
	return re.findall(r'src="(.+?\.jpg)" pic_ext', buf)

def save(L):
	i = 0
	for url in L:
		f = open(str(i)+'.jpg', 'w')
		response = urllib2.urlopen(url)

		if response.getcode() == 200:
			print 'success' + str(i)
			buf = response.read()
			f.write(buf)
			i += 1

#youwu = get_image('http://www.youwu.cc/guonei')
#print youwu
#save(youwu)

tieba = get_tieba_image('https://tieba.baidu.com/p/2460150866?red_tag=1658667561')
print tieba
#save(tieba)


# 方法: find_all(name, attrs, string)
# 方法: find(name, attrs, string)

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
"""
soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf8')
print '获取所有的链接'
linkes = soup.find_all('a')
for link in linkes:
	print link.name, link['href'], link.get_text()


print '获取LaCie的链接'
link_node = soup.find('a', href='http://example.com/lacie')
print link_node.name, link_node['href'], link_node.get_text()

print '正则匹配'
link_node = soup.find('a', href=re.compile(r'ill'))
print link_node.name, link_node['href'], link_node.get_text()

print '获取p段落文字'
p_node = soup.find('p', class_='title')
print p_node.name, p_node['class'], p_node.get_text()

#1：确定抓取的页面
#2：分析目标（url的格式，数据格式，网页编码）
#3：代码编写
#4：执行爬虫

#1.0：目标 百度百科Python词条相关词条网页-标题和简介
#入口页：https://baike.baidu.com/item/Python/407313
#2.0：页面URL: /item/xxx
#2.1：标题：<dd class="lemmaWgt-lemmaTitle-title"><h1>***</h1></dd>
#2.2：简介：<div class="para" label-module="para">***</div>
#2.3：页面编码：UTF-8
"""


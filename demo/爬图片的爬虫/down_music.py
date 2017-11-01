#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html)

print soup.title
print soup.head
print soup.a
print soup.p

print type(soup.a)
print soup.name
print soup.head.name
print soup.p.attrs
print soup.p['class']
print soup.p.get('class')
print soup.p.string
print soup.a.string

print soup.find_all('b')
print soup.find_all('a')
for tag in soup.find_all(re.compile(r'^b')):
	print tag.name

print soup.find_all(['a','b'])

for tag in soup.find_all(True):
	print tag.name

def has_class_but_no_id(tag):
	return tag.has_attr('class') and not tag.has_attr('id')

print soup.find_all(has_class_but_no_id)

print soup.find_all(id = 'link2')
import urllib2

req = urllib2.urlopen('http://www.imooc.com/course/list')

buf = req.read()

#print buf

import re

listurl = re.findall(r'//img\d.+\.jpg', buf)
#print listurl

M = []
for url in listurl:
	for url1 in re.split(r' src="', url):
		M.append(url1)
	#print M
	
N = []
for url in M:
	url = 'http:'+ url
	N.append(url)
print N

i = 0
for url in N:
	f = open(str(i)+'.jpg', 'w')
	req = urllib2.urlopen(url)
	buf = req.read()
	f.write(buf)
	i+=1

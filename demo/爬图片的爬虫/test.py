#coding=utf-8  

import urllib2
import urllib
import cookielib

url = 'https://www.aqistudy.cn/historydata/monthdata.php'

print 'First method'
resonse1 = urllib2.urlopen(url)
if resonse1.getcode() == 200:
	print 'success'
	print len(resonse1.read())
else:
	print 'faile'

print '-'*99
print 'Sconed method'
values = {'city': '上海'}
data = urllib.urlencode(values)
request = urllib2.Request(url, data)
request.add_header('user-agent', 'Mozilla/5.0')
response2 = urllib2.urlopen(request)
if response2.getcode() == 200:
	print 'success'
	print len(response2.read())
	stuff = response2.read()
	f = open('weather.txt', 'w')
	buf = response2.read()
	f.write(buf)

else:
	print 'fail'

print '-'*99
print 'Third method'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
if response3.getcode() == 200:
	print 'Success'
	print cj
	print len(response3.read())
else:
	print 'fail'

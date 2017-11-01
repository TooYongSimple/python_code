#coding=utf-8  
import urllib2
import urllib
import cookielib

root_url = 'https://www.zhihu.com/explore'
def urllib2_get_info(url):
	response = urllib2.urlopen(url)
	if response.getcode() == 200:
		return response.read()
	return None

print urllib2_get_info(root_url)

def request_get_info(url):
	request = urllib2.Request('http://blog.csdn.net/cqcre')
	try:
		print urllib2.urlopen(request)
	except urllib2.HTTPError, e:
		print e.code
		print e.reason
	
#request_get_info(root_url)

def post_get_info(url):
	values = {'username':'1092487614@qq.com', 'password': '123456'}
	data = urllib.urlencode(values)
	request = urllib2.Request(url, data)
	response = urllib2.urlopen(request)
	if response.getcode() == 200:
		return response.read()
	return None

#print post_get_info(root_url)

def get_get_info(url):
	values = {}
	values['username'] = '1092487614@qq.com'
	values['password'] = '123456'
	data = urllib.urlencode(values)
	url = url + '?' + data
	request = urllib2.Request(url, data)
	response = urllib2.urlopen(request)
	if response.getcode() == 200:
		return response.read()
	return None

#print get_get_info(root_url)

def set_url_header(url):
	try:
		user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		values = {'username': 'root', 'password': 'word'}
		headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  ,
                        'Referer': 'http://www.zhihu.com/articles' }  
		data = urllib.urlencode(values)
		request = urllib2.Request(url, data, headers)
		response = urllib2.urlopen(request)
		if response.getcode() == 200:
			return response.read()
		return None

	except Exception:
		print 'failed'

#print set_url_header(root_url)

def proxy_set(url):
	enable_proxy = True
	proxy_handler = urllib2.ProxyHandler({'http': 'http://some-proxy.com:8080'})
	null_proxy_handler = urllib2.ProxyHandler({})
	if enable_proxy:
		openr = urllib2.build_opener(proxy_handler)
	else:
		openr = urllib2.build_opener(null_proxy_handler)
	urllib2.install_opener(openr)

def cookie_get_info(url):
	cookie = cookielib.CookieJar()
	

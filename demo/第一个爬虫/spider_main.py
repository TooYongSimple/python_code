#coding=utf-8  
import url_manage
import html_downloader
import html_parser
import html_outputer

class SpiderMain(object):
	"""docstring for SpiderMain"""
	def __init__(self):
		super(SpiderMain, self).__init__()
		#url 管理器
		self.urls = url_manage.UrlManage()
		#下载器
		self.downloader = html_downloader.HtmlDownloader()
		#解析器
		self.parser = html_parser.HtmlPaser()
		#输出器
		self.outputer = html_outputer.HtmlOutputer()

# 首先将入口url添加进url管理器，然后就可以开始循环
# 然后从url管理器中获取一个待爬去的url
# 然后下载器开始下载
# 然后调用解析器，得到新的url列表和新的数据
# 然后将url 添加进url管理器
# 然后输入器收集数据

	def craw(self, root_url):
		count = 1
		self.urls.add_new_url(root_url)
		if self.urls.has_new_url:
			try:
				new_url = self.urls.get_new_url()
				print 'craw %d : %s' % (count, new_url)
				html_cont = self.downloader.download(new_url)
				new_urls, new_data = self.parser.parse(new_url, html_cont)
				print 'new_urls is %s' % new_urls
				self.urls.add_new_urls(new_urls)
				self.outputer.collect_data(new_data)

				'''
				if count == 10:
					break
				count = count + 1
				'''
			except:
				print 'craw failed'
			

		self.outputer.output_html()

if __name__ =='__main__':
	root_url = 'https://baike.baidu.com/item/Python/407313'
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)


def find_imooc(file_name):

	for line in open(file_name):
		if line.startswith('imooc'):
			print line

#find_imooc('imooc.txt')

def find_start_end_imooc(file_name):
	for line in open(file_name):
		if line.startswith('imooc') and line[:-1].endswith('imooc'):
			print line

#find_start_end_imooc('imooc.txt')

a = '_value1'

b = a and (a[0] == '_' or 'a' <= a[0] <= 'z')

import re

str1 = 'imooc python'
ma = re.match(r'[1-9]?\d$|100', '9')
if ma:
	print ma.group()
else:
	print 'fail'

str2 = 'imooc videonum = 1000 and 1001'
print str2.find('1000')

info = re.search(r'\d+',str2)
if info:
	print info.group()

str3 = 'c++=100, java = 90, python = 80'

info1 = re.findall(r'\d+', str3)
sum = sum([int(x) for x in info1])
print sum

def add1(match):
	va1 = match.group()
	num = int(va1) + 1
	return str(num)

str4 = 'imooc videonum = 9999'
info4 = re.sub(r'\d+', add1, str4)
print info4

str5 = 'imooc:C C++ Java,Python'
info5 =re.split(r':| |,', str5)
print info5
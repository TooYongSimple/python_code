# -*- coding:utf-8 -*-
def power(x):
	return x * x

print power(3)
print power(5)
print power(15)

def power1(x, n):	
	s = 1
	while n > 0:
		n = n-1
		s = s * x
	return s

print power1(2, 4)
print power1(5, 2)

def power2(x, n = 2):
	s = 1
	while n > 0:
		n = n-1
		s = s * x
	return s

print power2(5)
print power2(6)

def enroll(name, gender):
	print 'name:', name
	print 'gegnder:', gender

enroll('Sarah', 'F')

def enroll1(name, gender, age = 6, city = 'Beijing'):
	print 'name:', name
	print 'gender:', gender
	print 'age:', age
	print 'city:', city


enroll1('Bob', 'A')
enroll1('张三', 'S', 8, '天津')


def add_end(L = []):
	L.append('END')
	return L

print add_end([1, 2, 3])
print add_end(['x', 'y', 'z'])
print add_end()


def calc(numbers):
     sum = 0
     for n in numbers:
         sum = sum + n*n
     return sum
 
print calc([1,2,3])

def calc1(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

print calc1(1,2)
print calc1()


numbers = [1,3,5,7]
print calc1(*numbers)


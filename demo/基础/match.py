# -*- coding:utf-8 -*-
import math

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print x, y

r = move(100, 100, 60, math.pi / 6)
print r

def quadratic(a, b, c):

	s = b*b - 4*a*c
	t = 2*a
	if s >= 0:
		one = (-b + math.sqrt(s)) / t
		two = (-b - math.sqrt(s)) / t
		return one, two
	else:
		return 'error'

r = quadratic(2, 3, 1)
print r

t = quadratic(1, 3, -4)
print t

t = quadratic(1, 3, 5)
print t

def person(name, age, **kw):
	print 'name:', name, 'age:', age, 'other:', kw

person('Michael', 30)

person('Bob', 35, city = 'Beijing')

person('Adam', 45, gender = 'M', job = 'Engineer')

extra = {'city': 'Beijing', 'Job': 'Engineer'}

person('Jack', 24, city = extra['city'],job = extra['Job'])

person('Jack', 24, **extra)

def person1(name, age, **kw):
	if 'city' in kw:
		
		pass
	if 'job' in kw:
		
		pass
	print 'This is the person1 function'
	print 'name:', name, 'age:', age, 'other:',kw

person1('Jack', 24, city = 'Beijing', addr = 'Chaoyang', zipcode = 123456)
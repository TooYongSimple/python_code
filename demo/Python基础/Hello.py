import math
import time
import functools
from math import pow, sin, log

def calc_prod(lst):
    def lazy_prod():
        def f(x, y):
            return x * y
        return reduce(f, lst, 1)
    return lazy_prod
f = calc_prod([1, 2, 3, 4])
print f()

def calc_prod(lst):
	def lazy_prod():
		def f(x,y):
			return x * y
		return reduce(f,lst)
	return lazy_prod

f = calc_prod([1,2,3,4])
print f()

def count():
	fs = []
	for i in range(1,4):
		def f(j):
			def g():
				return j*j
			return g
		r = f(i)
		fs.append(r)
	return fs

f1,f2,f3 = count()	
print f1(), f2(), f3()
def is_sqr(x):
	return math.sqrt(x) % 1 == 0
print filter(is_sqr, range(1,101))

print map(lambda x: x*x,[1,2,3,4])
print reduce(lambda x,y: x*y,[1,2,3,4])
print filter(lambda x: math.sqrt(x) % 1 == 0, range(1,101))

print filter(lambda s: s and len(s.strip()) > 0, ['test', None, '', 'str', ' ', 'end'])

# def new_factorial(f):
# 	def fn(x):
# 		print time.clock()
# 		return f(x)	
# 	return fn
# factorial = new_factorial(factorial)
# print factorial(5)


def new_func(func):
	def log_time(x):
		print time.clock()
		return func(x)
	return log_time
@new_func
def factorial(n):
	return reduce(lambda x,y: x*y,range(1,n+1))

print factorial(5)

import time

def performance(unit):
    def log_time(func):
        def factorial(n):
            print str(time.clock()) + unit
            func(n)
        return factorial
    return log_time

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)

print '-------------         ---------------'

def log(f):
	def wrapepr(*args, **kw):
		print 'call...'
		return f(*args, **kw)
	return wrapepr
@log
def f2(x):
	pass
print f2.__name__

def log(f):
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    return wrapper
@log
def f2(x):
    pass
print f2.__name__

print '-------------         ---------------'
print int('12345')
print int('12345',base=8)
print int('12345',16)

def int2(x,base=2):
	return int(x,base)

print int2('1000000')
print int2('1010101')

int3 = functools.partial(int,base=2)

print int3('101')

def new_sort(x,y):
	if x.lower() < y.lower():
		return -1
	if x.lower() > y.lower():
		return 1
	return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'],new_sort)

sort = functools.partial(sorted,cmp=lambda x,y: cmp(x.lower(),y.lower()))

print sort(['bob', 'about', 'Zoo', 'Credit'])

print '-------------    mukuai   ---------------'

print math.pow(2,3)
print math.pi
print math.pow(2,10)
print math.sin(3.14)
print pow(2,11)
print sin(3.14)


class Person(object):
	"""docstring for Person"""
	def __init__(self, name, gender, birth, **kw):
		super(Person, self).__init__()
		self.name = name
		self.gender = gender
		self.birth = birth
		for k, v in kw.iteritems():
			setattr(self,k, v)
xiaoming = Person('Xiao Ming', 'Male', '1990-1-1',job='Student')

print xiaoming.name
print xiaoming.job
		

class Person1(object):
	"""docstring for Person1"""
	def __init__(self, name, score):
		super(Person1, self).__init__()
		self.name = name
		self.score = score

p = Person1('Bob',59)
print p.name
print p.score
		
print '-------------    mukuai   ---------------'
class Person2(object):
	"""docstring for Person2"""
	address = 'Earth'
	count = 0
	def __init__(self, name):
		super(Person2, self).__init__()
		self.name = name
		Person2.count = Person2.count +1

#
print Person2.count

p1 = Person2('Bob')
print p1.count
p2 = Person2('Alice')
print p2.count

class Person(object):

    def __init__(self, name, score):
        self.__score = score

    def get_grade(self):
        if self.__score == 90:
            return 'A-'
        if self.__score == 65:
            return 'B-'
        if self.__score == 48:
            return 'C-'

p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print p1.get_grade()
print p2.get_grade()
print p3.get_grade()

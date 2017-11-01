# This Python file uses the following encoding: utf-8

ten_things = 'Apples Oranges Crows Telephone Light Sugar'

print 'wait there are not 10 thongs in thta list. Let\'s fix that.'

stuff = ten_things.split(' ')
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

while  len(stuff) != 10:
	next_one = more_stuff.pop()
	print 'Adding: ', next_one
	stuff.append(next_one)
	print 'There are %d items now.' % len(stuff) 

print 'There we go: ', stuff

print 'Let\'s do some things with stuff.'

print stuff[1]

print stuff[-1] # whoa! fancy

print stuff.pop()
print ' '.join(stuff)  #是使用一个字符串将列表内容链接起来
print '#'.join(stuff[3:5]) # 是把3，4 两个对象提出来

stuff = {'name': 'Zed', 'age': 39, 'height': 6*12+2}
print stuff['name']
print stuff['age']
print stuff['height']

stuff['city'] = 'San Francisco'
print stuff['city']
del stuff['city']

print stuff

states = {

	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

citis = {
	
	'CA': 'San Francisico',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

citis['NY'] = 'New York'
citis['OR'] = 'Portland'

print '-' * 10
print 'NY State has: ', citis['NY']
print 'OR State has: ', citis['OR']

print '-' * 10
print 'Michigan\'s abbreviation is: ',states['Michigan']
print 'Florida\'s abbreviation is: ', states['Florida']

print '-' * 10
print 'Michigan has:', citis[states['Michigan']]
print 'Florida has:', citis[states['Florida']]

print '-' * 10
for state, abbrev in states.items():
	print '%s is abbreiated %s' % (state, abbrev)

print '-' * 10
for city, abbrev in citis.items():
	print '%s has the city %s' % (city, abbrev)

state = states.get('Texas')

if not state:
	print 'Sorry, no texas'

# get 方法的第二个参数是没取到之后的提示
city = citis.get('TX','Does not Exist.')
print 'The city for the state \'TX\' is: %s' % city

print '-' * 100
class myStuff(object):
	"""docstring for myStuff"""
	def __init__(self):
		super(myStuff, self).__init__()
		self.tangerine = 'And now a thousand years between'
	def apple(self):
			print 'I AM CLASS APPLESS!'	

sting = myStuff()
sting.apple()
print sting.tangerine

print '-' * 100
class Song(object):
	"""docstring for Song"""
	def __init__(self, lyrics):
		super(Song, self).__init__()
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_birthday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_birthday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
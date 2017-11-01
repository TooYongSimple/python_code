print True and True
print False and True
print 1 == 1 and 2 == 1
print "test" == "test"
print 1==1 or 2 != 1

people = 30
cars = 40
trucks = 15

if cars > people:
	print 'We should take the cars.'
elif cars < people:
	print 'We should not take the cars.'
else:
	print 'We can\'t decide.'


if trucks > cars:
	print 'That\'s too many trucks.'
elif trucks < cars:
	print 'Maybe we could take the trucks.'
else:
	print 'We still can\'t decide.'

the_count = [1,2,3,4,5]
for i in the_count:
	print 'This is count %d' % i

fruits = ['apples', 'oranges', 'pears', 'apricots']
for i in fruits:
	print 'A fruit of type : %s' % i


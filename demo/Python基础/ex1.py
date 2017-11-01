print 3+2 < 5-7

print 'what is 5-7?',5-7

print 'is it greater or equal?', 5>=-2


x = 'three are %d types of people.' % 10

birthday = 'birthday'
do_not ='don\'t'
y = 'those who konw %s and those who %s.' % (birthday, do_not)

print x
print y

print 'i said: %r' % x
print 'i also said:\'%s\.' %y

hilarious = False
joke_evaluation = 'isn\'t that joke so funny?!%r'

print joke_evaluation % hilarious

w = 'this is the left side of ...'
e = 'a string with a right side'
print w+ e

print '.' *90

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12


formatter = '%s %s %s %s'

print formatter % (1,2,3,4)
print formatter % ('one', 'two', 'three','four')
print formatter % (True, False,False, True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % ('i had this thing.',
	'i had you',
	'but it idi not sing',
	'so i said.')
for i in ['/', '-', '|', '\\','|']:
	print '%s\r' % i
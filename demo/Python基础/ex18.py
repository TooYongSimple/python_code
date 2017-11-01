def print_two(*args):
	arg1, arg2 = args
	print 'arg1: %r, arg2: %r' % (arg1, arg2)

print_two('xiaohei','xiaohong')

def print_two_again(arg1,arg2):
	print 'arg1: %r, arg2: %r' % (arg1, arg2)

print_two_again('1','2')

def print_one(arg1):
	print 'arg1: %r' % arg1

print_one(3)

def print_onne():
	print 'I got nothing'

print_onne()

def cheese_and_crackers(cheese_count, boxes_of_crachers):
	print 'You have %d cheeses!' % cheese_count
	print 'You have %d boxes of crackers!' % boxes_of_crachers
	print 'Man that\'s enough for a party!'
	print 'Get ablanket.\n'

cheese_and_crackers(10,12)

amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

cheese_and_crackers(10+20,30+40)

cheese_and_crackers(amount_of_cheese +100, amount_of_crackers + 200)

def print_count():
	cheese =  raw_input('input cheese number:')
	print 'You have %d cheeses!' % int(cheese)
	boxes = raw_input('input boxes number:')
	print 'You have %d crackers!' % int(boxes)

print_count()

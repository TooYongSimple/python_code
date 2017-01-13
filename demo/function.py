a = 255
print hex(a)

print 'a =', abs(a)

def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x

print '-2 = ',my_abs(-2)
print '2 = ',my_abs(2)


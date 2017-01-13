#!/usr/bin/env python
# -*- coding: utf-8 -*-
#print absolute value of an integer;
age = 3
if age >= 18:
    print 'your age is', age
    print 'adult'
elif age >= 6:
    print 'teenage'
else:
    print 'kid'

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name

sum = 0
for x in range(101):
    sum += x
print sum

sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print sum


#brith = int(raw_input('birth:'))
#if brith < 2000:
#    print '00 前'
#else:
#    print '00 后'

def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

x = int(raw_input('请输入数字：'))
xx = my_abs(x)

print xx




def power(x, n = 2):
    s = 1
    while n > 0:
        n -= 1
        s = s*x
    return s

print power(3)
print power(3,5)












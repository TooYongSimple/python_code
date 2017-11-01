from ex25 import *

print 'Let\'s practice everything.'

poem = '\tThe lovely world with logic so firmly planted cannnot discern \n the needs of love nor comprehend passion from intuition and requires an explanation \n\twhere there is none.'

print '----------------'
print poem
print '----------------'

five = 10-2+3-6

print 'This should be five:%s' % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print 'With a starting point of: %d' % start_point
print 'We\'d have %d beans, %d jars, and %d crates.' % (beans, jars, crates)

start_point = start_point / 10

print 'We can also do that this way:'
print 'We\'d have %d beans, %d jars, and %d crates.' % secret_formula(start_point)

print '----------------'

sentence = 'All good things come to those who wait.'
words = break_words(sentence)
print words

sorted_words = sort_words(words)
print sorted_words

word = print_first_word(words)
print word

word = print_last_word(words)
print word

print words

word = print_first_word(sorted_words)
print word

word = print_last_word(sorted_words)
print word

print sorted_words

sorted_words = sort_sentence(sentence)
print sorted_words

print_first_and_last(sentence)
print_fist_and_last_sorted(sentence)


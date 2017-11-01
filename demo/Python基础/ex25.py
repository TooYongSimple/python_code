def break_words(stuff):
	'''This function will break up words for us.'''
	words = stuff.split(' ')
	return words

def sort_words(words):
	'''Sorts the words.'''
	return sorted(words)

def print_first_word(words):
	'''Prints the first word after popping it off.'''
	word = words.pop(0)
	return word

def print_last_word(words):
	word = words.pop(-1)
	return word

def sort_sentence(sentence):
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	word = break_words(sentence)
	print print_first_word(word)
	print print_last_word(word)

def print_fist_and_last_sorted(sentence):
	words = sort_sentence(sentence)
	print print_first_word(words)
	print print_last_word(words)
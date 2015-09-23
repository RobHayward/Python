def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the ords."""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after poping it off."""
	word = words.pop(0)
	print word

def print_Last_word(words):
	"""Prints the last word after poping it of"""
	word = words.pop(-1)
	print word 
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words"""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the irst and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_lst_sorted(sentence):
	"""Sorts the words and tten prints the irst and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)


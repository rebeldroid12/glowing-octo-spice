class ParserError(Exception):
	"""docstring for ParserError"""
	pass
		

class Sentence(object):
	"""docstring for Sentence"""
	def __init__(self, subject, verb, obj):
		#takes ('noun','princess') tuples & converts them
		#want the tuple value not tuple key
		self.subject = subject[1]
		self.verb = verb[1]
		self.object = obj[1]


def peek(word_list):
	''' if word_list is present grab the first tuple pair
	return the type ie ('noun','princess')...return 'noun'
	'''
	if word_list:
		word = word_list[0]
		return word[0]
	else:
		return None

def match(word_list,expecting):
	""" if word_list is present grab first tuple pair & 
		pop it off 0th element,check if you have the type you were expecting

	"""
	if word_list:
		word = word_list.pop(0)

		if word[0] == expecting:
			return word

		else:
			return None

	else:
		return None

def skip(word_list, word_type):
	""" check the word type and if it's the type you want then keep it
	else skip it

	"""
	# ex: 'noun' == 'noun'
	while peek(word_list) == word_type:
		#ex: pop off from list
		match(word_list,word_type)


def parse_verb(word_list):
	#take out type stop words
	skip(word_list,'stop')

	#grabbing just verbs
	if peek(word_list) == 'verb':
		return match(word_list,'verb')

	else:
		raise ParserError('Expected a verb next')

def	parse_object(word_list):
	#skips stop words
	skip(word_list, 'stop')
	#returns the next word type
	next_word = peek(word_list)

	if next_word == 'noun':
		return match(word_list, 'noun')
	elif next_word == 'direction':
		return match(word_list, 'direction')
	else:
		raise ParserError('Expected noun or direction next')


def parse_subject(word_list):
	skip(word_list,'stop')
	next_word = peek(word_list)

	if next_word == 'noun':
		return match(word_list,'noun')
	elif next_word == 'verb':
		return ('noun','player')
	else:
		raise ParserError('Expected a verb next')

def parse_sentence(word_list):
	subj = parse_subject(word_list)
	verb = parse_verb(word_list)
	obj = parse_object(word_list)

	return Sentence(subj,verb,obj)

	













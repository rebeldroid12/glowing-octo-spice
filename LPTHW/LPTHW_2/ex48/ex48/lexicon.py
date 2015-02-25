#Game Lexicon


def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None


def scan(s):
	#check if it's a string
	if not s:
		return 'nope, not string. try again'
	
	#make all lowercase & split them
	#frag = s.lower().split()
	frag = s.split()

	#the lexicon words/numbers
	directions = ['north', 'south', 'east', 'west','down','up','left','right','back']
	verbs = ['go','stop','kill','eat']
	stops = ['the','in','of','from','at','it']
	nouns = ['door','bear','princess','cabinet']
	numbers = range(0,10)

	#make tuples like ('direction','north')
	token = ''
	word = ''
	sentence = []

	for w in frag:
		if w.isdigit():

				token = 'number'
				word = convert_number(w)

		elif w in directions:
			token = 'direction'
			word = str(w)

		elif w in verbs:
			token = 'verb'
			word = str(w)

		elif w in stops:
			token = 'stop'
			word = str(w)

		elif w in nouns:
			token = 'noun'
			word = str(w)

		elif w in numbers:
			token = 'number'
			word = int(w)

		else:
			token = 'error'
			word = str(w)

		tup = (token,word)
		sentence.append(tup)

	return sentence
	

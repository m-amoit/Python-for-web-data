import re

def roman_to_int(s):
	'''
	Convert roman numerals to integers
	'''
	keys = {"M" : 1000,
			"CM": 900, "D" : 500, "CD": 400, "C" : 100,
			"XC": 90,  "L" : 50,  "XL": 40,  "X" : 10,
			"IX": 9,   "V" : 5,   "IV": 4,   "I" : 1 
			}

	pattern = ('(^M?M?M?M?)(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$')
	
	if not re.search (pattern, s):
		return 'Invalid Roman Numeral'

	x = re.findall(pattern, s)
	print x
	
	result = 0
	for item in x:
		for i in item:
			if i == '':
				continue
			try:
				result += keys[i]
			except KeyError:
				for item in i:
					result += keys[item]
	return result





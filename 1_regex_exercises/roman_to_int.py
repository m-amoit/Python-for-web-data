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

	pattern = ('^(M{0,4})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
	
	if not re.search (pattern, s):
		return 'Invalid Roman Numeral'
	
	result = 0
	for item in re.findall(pattern, s):
		for i in item:
			if i == '':
				continue
			try:
				result += keys[i]
			except KeyError:
				for item in i:
					result += keys[item]
	return result

print roman_to_int('MCMLXX')




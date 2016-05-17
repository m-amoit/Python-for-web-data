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

	pattern = '''
		^					# Beginning of string
		(M{0,4})			# Thousands - 0-4 M's
		(CM|CD|D?C{0,3})	#Hundreds: CM or CD or optional D followed by 3 optional C's 
		(XC|XL|L?X{0,3})	#Tens: XC or XL or optional L and 3 optional X's
		(IX|IV|V?I{0,3})	#Ones: IX or IV or optional V and 3 optional I's
		$					# End of string
		'''
	
	if not re.search (pattern, s, re.VERBOSE):
		return 'Invalid Roman Numeral'
	
	result = 0
	for item in re.findall(pattern, s, re.VERBOSE):
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




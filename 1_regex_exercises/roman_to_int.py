def roman_to_int(A):
	'''
	Convert roman numerals to integers
	'''
	keys = {"M" : 1000,
			"D" : 500,
			"C" : 100,
			"L" : 50,
			"X" : 10,
			"V" : 5,
			"I" : 1
			}
	
	integer = 0
	for i in A:
		integer += keys[i]
	return integer

print roman_to_int('MDC')

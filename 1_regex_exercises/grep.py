import re
hand = open('mbox-short.txt')
def grep(A):
	'''
	Write a simple program to simulate the operation of the grep command 
	on Unix. Ask the user to enter a regular expression and count the 
	number of lines that match the regular expression. 
	Output:
		$ python grep.py
		Enter a regular expression: java$
		mbox.txt has 60 lines that match java$
	'''

	count = 0
	for line in hand:
		line = line.rstrip()
		
		x = re.findall(A, line)
		
		if len(x) > 0:
			count += 1

	return 'mbox-short.txt has %d lines that match %s' % (count, A)

print grep(raw_input('Enter a regular expression: '))





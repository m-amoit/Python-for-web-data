import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	'''search all lines starting with X followed by any
	number of non whitespace characters and extract only 
	the floating point
	'''
	# x = re.findall('^X\S*: ([0-9.]+)', line)
	# if len(x) > 0:
	# 	print x
	'''print the whole line'''
	# x = re.findall('^Details:.*rev=[0-9]+', line)
	# if len(x) > 0:
	# 	print x
	'''
	parenthesis only extraxts the portion of the string
	we are interested in
	'''
	# x = re.findall('Details:.*rev=([0-9]+)', line)
	# if len(x) > 0:
	# 	print x

	y = re.findall('^From .* ([0-9][0-9]:..:..).*', line)
	if len(y) > 0: print y
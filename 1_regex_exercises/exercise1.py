import re
'''
Write a program to look for lines of the form
		New Revision: 39772
and extract the number from each of the lines using a regular 
expression and the findall() method. Compute the average of the numbers 
and print out the average.
'''
hand = open('mbox-short.txt')
# count = 0
# sum = 0
l = []
for line in hand:
	line = line.rstrip()
	x = re.findall('^New .* ([0-9].*)', line)
	for i in x:
		l.append(int(i))
	# if len(x) > 0:
	# 	count += 1
	# 	sum += int(x[0])
print sum(l)/len(l)
	





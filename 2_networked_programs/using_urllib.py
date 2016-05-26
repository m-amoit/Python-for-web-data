import urllib
import re

# a library that does all the socket work and makes web pages look like files.
# compare output with http.py

fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
# for line in fhand:
# 	print line.rstrip()
counts = dict()
for line in fhand:
	for word in line.split():
		counts[word] = counts.get(word, 0) + 1
print counts

'''extracting links'''
# url = raw_input('Enter - ')
# html = urllib.urlopen(url).read()
# links = re.findall('href="(http://.*?)"', html)
# for link in links:
# 	print link




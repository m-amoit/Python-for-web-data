import urllib
import re

fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
	print line.rstrip()

# url = raw_input('Enter - ')
# html = urllib.urlopen(url).read()
# links = re.findall('href="(http://.*?)"', html)
# for link in links:
# 	print link




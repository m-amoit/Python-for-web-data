import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve a list of anchor tags
# Each tag is like a dictionary of HTML attributes

tags = soup('a')

# for tag in tags:
# 	print tag.get('href', None)

for tag in tags:
	# Look at the parts of a tag
	print 'TAG:', tag
	print 'URL:', tag.get('href', None)
	print 'Content:', tag.contents[0]
	print 'Attrs:', tag.attrs 
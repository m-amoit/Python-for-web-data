import xml.etree.ElementTree as ET
#allows extraction of data from XML without worrying about 
#the rules of XML

input = '''
	<stuff>
		<users>
			<user x="2">
				<id>001</id>
				<name>Chuck</name>
			</user>
			<user x="7">
				<id>009</id>
				<name>Brent</name>
			</user>
		</users>
	</stuff>
	'''

stuff = ET.fromstring(input)
l = stuff.findall('users/user')
print 'User count:', len(l)

for item in l:
	print ('Name: %s Id: %s Attr: %s') % \
	(item.find('name').text, item.find('id').text, item.get('x'))
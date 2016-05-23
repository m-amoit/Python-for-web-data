import xml.etree.ElementTree as ET
#allows extraction of data from XML without worrying about 
#the rules of XML

data = '''
	<person>
		<name>Chuck</name>
		<phone type = "intl">+254 729 240 618</phone>
		<email hide = "yes"/>
	</person>'''

tree = ET.fromstring(data)
#Converts string representation of XML into a tree of XML nodes
print 'Name:',tree.find('name').text
#retrieve a node that matches the specified tag
print 'Attr:',tree.find('email').get('hide')
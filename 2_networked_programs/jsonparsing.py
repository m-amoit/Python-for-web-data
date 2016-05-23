import json
#JSON format is nearly identical to a combination 
#of Python lists and dictionaries
input = '''
	[
		{ "id" : "001",
		  "x"  : "2",
		 "name": "Chuck"
		},
		{ "id" : "009",
		  "x"  : "7",
		 "name": "Brent"
		}
	]'''

info = json.loads(input)
print 'User count:', len(info)

for item in info:
	print ('Name: %s Id: %s Attr: %s') % \
	(item['name'], item['id'], item['x'])

#Output exactly the same as in the xml version
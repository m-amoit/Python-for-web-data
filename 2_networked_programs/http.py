import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
# mysock.connect(('www.amoiteumot.wordpress.com', 80))
# mysock.send('GET https://www.amoiteumot.wordpress.com/2016/05/11/what-potential/ HTTP/1.0\n\n')
'''prints html'''

while True:
	data = mysock.recv(512)
	if (len(data) < 1):
		break
	print data

mysock.close()

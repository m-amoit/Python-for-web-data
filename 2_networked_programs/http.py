'''making a low level network connection with sockets'''
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80)) #makes a connection to port 80 on the server www.py4info.com
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
'''prints html'''

while True:
	'''data is received in 512 character chunks until there's 
	no more data to be read - recv() returns an empty string'''
	data = mysock.recv(512)
	if (len(data) < 1):
		break
	print data

mysock.close()

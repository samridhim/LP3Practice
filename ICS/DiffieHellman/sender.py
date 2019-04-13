import socket
a = 5
p = 13
g = 5
server = socket.socket()
host =socket.gethostname()
port = 12345
server.bind((host, port))
server.listen(5)
while True:
	client, addr = server.accept()
	print "Got connection from", addr
	print "Sending: ", g**a
	client.send(str(g**a))
	B = client.recv(1024)
	shared_key = (int(B,10)**a) % p
	print shared_key
	shr_key = client.recv(1024)
	print shr_key
	if(int(shr_key,10) == shared_key):
		print "Communication Secure"
	client.close()
	


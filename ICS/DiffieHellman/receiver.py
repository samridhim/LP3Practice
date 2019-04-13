import socket
b = 6
p = 13
g = 5

client = socket.socket()
host =socket.gethostname()
port = 12345
client.connect((host, port))
A = client.recv(1024)
print A
print "Sending: ", g**b
client.send(str(g**b))
shared_key = (int(A,10)**b) % p
print shared_key
client.send(str(shared_key))
client.close()

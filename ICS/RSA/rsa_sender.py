import socket
import json
import binascii
from decimal import *
server = socket.socket()
host = socket.gethostname()
server.bind((host, 12345))

def _gcd(a,b):
	if b ==0:
		return a
	else:
		return _gcd(b, a%b)

def _fmod(x,d,n):
	a = 1
	for i in range(d):
		a = (x * a) % n
	return a

p = 53
q = 59

n = p*q
print "n:", n
phi = (p-1) * (q-1)
e = 2
for i in range(2, phi):
	if _gcd(i, phi) ==1:
		e = i
		break

public_key = {"n" : n, "e":e}
public_key = json.dumps(public_key)

print "e:" , e
d = 1
i =1


while True:
	d = float((phi * i) + 1)
	if(d%e)==0:
		d = d/e
		break
	i = i +1
print "d:", d

server.listen(5)
while True:
	client, addr = server.accept()
	client.send(public_key)
	encrypted_msg =[]
	decrypted_msg = []
	encrypted_msg = client.recv(1024)
	enc = encrypted_msg.split(',')
	for e in enc:
		decrypted_msg.append(chr(_fmod(int(e), int(d), n)))
	print ''.join(decrypted_msg)
	client.close()






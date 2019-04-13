import socket
import json 
import binascii

def _fmod(x,d,n):
	a = 1
	for i in range(d):
		a = (x * a) % n
	return a


client = socket.socket()
host = socket.gethostname()
client.connect((host, 12345))
public_key = client.recv(1024)

public_key = json.loads(public_key)
M = "HI Samridhi here!"
message_list = []
for letter in M:
	base = ord(letter)
	encrypted_msg = _fmod(base, public_key["e"], public_key["n"])
	message_list.append(str(encrypted_msg))

client.send(','.join(message_list))

client.close()

def _gcd(a,b):
	if(b==0):
		return a
	else:
		return _gcd(b, a%b)
p = input()
q = input()

n = p*q

phi = (p-1) * (q -1)

print phi

e = 2
for i in range(2, phi):
	if(_gcd(i, phi))==1:
		e = i
		break

print e

pub_key = (n,e)

d = 1
i =1
while True:
	d = float(i * phi + 1 )
	if(d%e)==0:
		d = d / e
		break
print d

priv_key = (n,d)

m = 21
encrypt = m**e % n


decrypt = encrypt **d 	% n
print decrypt

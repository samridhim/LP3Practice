

# key generation

#K = "1010000010"

def genKey(K):
	P10 = [3,5,2,7,4,10,1,9,8,6]
	P8 =[6, 3,  7, 4, 8, 5, 10, 9]
	K_temp = []
	for p in P10:
		K_temp.append(K[p-1])

	K = ''.join(K_temp)
	#print K


	key_left =K[:5]
	key_right = K[5:]

	key_left = key_left[1:] + key_left[:1]

	key_right = key_right[1:] + key_right[:1]
	print key_left, key_right
	K = key_left + key_right

	#print K

	K1 = []
	for p in P8:
		K1.append(K[p-1])

	K1 = ''.join(K1)
	#print K1

	key_left = key_left[2:] + key_left [:2]
	key_right = key_right[2:] + key_right[:2]

	K = key_left + key_right

	#print K

	K2 = []
	for p in P8:
		K2.append(K[p-1])

	K2 = ''.join(K2)

	#print K2

	return K1, K2

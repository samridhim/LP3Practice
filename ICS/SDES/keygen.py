def keyGen(K):
	P10 = [3,5,2,7,4,10,1,9,8,6]
	P8 =[6, 3,  7, 4, 8, 5, 10, 9]
	
	K_temp = []
	for p in P10:
		K_temp.append(K[p-1])
	
	K = ''.join(K_temp)
	
	K_left = K[:5]
	K_right = K[5:]
	
	K_left = K_left[1:] + K_left[:1]
	K_right = K_right[1:] + K_right[:1]


	K1 = K_left + K_right 
	K1_temp = []
	for p in P8:
		K1_temp.append(K1[p-1])
	
	K1 = ''.join(K1_temp)

	K_left = K_left[2:] + K_left[:2]
	K_right = K_right[2:] + K_right[:2]
	K2 = K_left + K_right 
	K2_temp = []
	for p in P8:
		K2_temp.append(K2[p-1])
	
	K2 = ''.join(K2_temp)
	return K1, K2

	
	

from keygen import keyGen
IP = [2 ,6 ,3 ,1 ,4 ,8 ,5 ,7]
EP = [ 4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4,3, 1]
IPInv = [4, 1, 3, 5, 7, 2, 8, 6]
S0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
S1 = [[0,1,2,3], [2,0,1,3], [3,0,1,0], [2,1,0,3]]
K = raw_input("Enter 10 bit Key")
K1, K2 = keyGen(K)
print K1, K2
P = raw_input("Enter 8 bit Plain Text")

def sbox(left, right):

	#print left,right
	r0 = int(left[0] + left[3],2)
	c0 = int(left[1] + left[2],2)
	r1 = int(right[0] + right[3],2)
	c1 = int(right[1] + right[2],2)
	#print r0,c0
	left_nib = S0[r0][c0]
	right_nib =  S1[r1][c1]
	
	left_nib = bin(left_nib)[2:].zfill(2)
	right_nib = bin(right_nib)[2:].zfill(2)

	return left_nib + right_nib
	

def encrypt(P, K):
	P_left = P[:4]
	P_right = P[4:]
	
	expanded_temp = []
	
	for p in EP:
		expanded_temp.append(P_right[p-1])
	
	expanded = ''.join(expanded_temp)
	
	#print len(expanded)
	expanded = bin(int(expanded,2) ^ int(K,2))[2:].zfill(8)
	
	expanded_left = expanded[:4]
	expanded_right = expanded[4:]

	#print len(expanded)
	s_box_output = sbox(expanded_left, expanded_right)
	print s_box_output
	p4 = []
		
	for p in P4:
		p4.append(s_box_output[p-1])
	
	p4 = ''.join(p4)
	print p4
	
	p4_xor = bin(int(p4,2) ^ int(P_left,2))[2:].zfill(4)
	
	output = p4_xor + P_right
	
	return output


#encryption
P_IP = []
for p in IP:
	P_IP.append(P[p-1])

P = ''.join(P_IP)

output = encrypt(P, K1)
print output

output_left = output[:4]
output_right = output[4:]

output = output_right + output_left

output = encrypt(output, K2)

print output

P_IP = []
for p in IPInv:
	P_IP.append(output[p-1])

cipher_text = ''.join(P_IP)

print cipher_text







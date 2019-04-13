from sdes import genKey
IP = [2 ,6 ,3 ,1 ,4 ,8 ,5 ,7]
EP = [ 4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4,3, 1]
IPInv = [4, 1, 3, 5, 7, 2, 8, 6]
S0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
S1 = [[0,1,2,3], [2,0,1,3], [3,0,1,0], [2,1,0,3]]

def sbox(left, right):
	print left, right
	r0 = int(left[0] + left[3], 2)
	c0 = int(left[1] + left[2], 2)
	r1 = int(right[0] + right[3], 2)
	c1 = int(right[1] + right[2], 2)
	print r0,c0
	print r1,c1
	left_nib = []
	right_nib = []
	if(S0[r0][c0]) == 2:		
		left_nib.append('1')
		left_nib.append('0')
	elif(S0[r0][c0]) == 3:
		left_nib.append('1')
		left_nib.append('1')
	elif(S0[r0][c0]) == 0:
		left_nib.append('0')
		left_nib.append('0')
	elif(S0[r0][c0]) == 1:
		left_nib.append('0')
		left_nib.append('1')
	
	if(S1[r1][c1]) == 2:		
		right_nib.append('1')
		right_nib.append('0')
	elif(S1[r1][c1]) == 3:
		right_nib.append('1')
		right_nib.append('1')
	elif(S1[r1][c1]) == 0:
		right_nib.append('0')
		right_nib.append('0')
	elif(S1[r1][c1]) == 1:
		right_nib.append('0')
		right_nib.append('1')
	
	left_nib = ''.join(left_nib)
	right_nib = ''.join(right_nib)

	return left_nib + right_nib

	

def encrypt(P,K):
	print "Key is" , K
	P_left = P[:4]
	P_right = P[4:]

	expanded = []	
	for p in EP:
		expanded.append(P_right[p-1])
	expanded = ''.join(expanded)
	print "Expansion output: ", expanded
	expanded = bin(int(expanded,2) ^ int(K,2))[2:]
	expanded = expanded.zfill(8)
	print "Expansion xor with K", expanded

	expanded_left = expanded[:4]
	expanded_right = expanded[4:]
	
	sbox_output = sbox(expanded_left, expanded_right)
	
	print "SBOX output:", sbox_output
	
	p4_output = []
	for p in P4:
		p4_output.append(sbox_output[p-1])
	p4_output = ''.join(p4_output)

	print "P4 output : ", p4_output
	p4_output = bin(int(p4_output,2) ^ int(P_left,2))[2:]
	p4_output = p4_output.zfill(4)
	
	print "P4 output xor with left half: ", p4_output 
	output = p4_output + P_right
	
	print "output of round: ", output
	return output


K = raw_input("Enter 10 bit key: ")
K1, K2 = genKey(K)
print "Key1:", K1, "Key2:", K2

P = raw_input("Enter 8 bit Plain text: ")

#encryption
P_IP = []
for p in IP:
	 P_IP.append(P[p-1])
P = ''.join(P_IP)
print "-----Round 1-----"
output = encrypt(P, K1)

output_left = output[:4]
output_right = output[4:]
print "output round1 :" , output
output = output_right + output_left

print "swapped output round1 :" , output
print "-----Round 2-----"
output = encrypt(output, K2)
print output

CT = []
for p in IPInv:
	 CT.append(output[p-1])
CT = ''.join(CT)
print "Cipher Text", CT


#decryption
P_IP = []
for p in IP:
	 P_IP.append(CT[p-1])
CT = ''.join(P_IP)
print "-----Round 1-----"
output = encrypt(CT, K2)

output_left = output[:4]
output_right = output[4:]
print "output round1 :" , output
output = output_right + output_left

print "swapped output round1 :" , output
print "-----Round 2-----"
output = encrypt(output, K1)
print output

PT = []
for p in IPInv:
	 PT.append(output[p-1])
PT = ''.join(PT)
print "Plain Text", PT

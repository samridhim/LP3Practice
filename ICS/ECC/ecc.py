import numpy as np
import random

def genPoint(a,b):
	y = random.randint(-100,100)
	roots = np.roots([1, 0, a, b - y **2])
	roots = [val.real for val in roots if val.imag ==0]
	x =  random.choice(roots)
	return np.array([x,y])

a = input("Enter A's private Key")
b = input("Enter B's private Key")


G = genPoint(a,b)

A = np.array([])
B = np.array([])
A = a*G
B= b*G

k1 = B*a
k2 = A*b

M = np.array([6,7])

c1 = np.multiply(a, G)
c2 = M + np.multiply(a, B)
d1 = c1 * b

decrypt = c2 - d1
print decrypt

"""
p = 13
q = 31
e = 19
M = 2

n = p * q
print(n)
C = M ** e % n
print(C)
print()
pn = (p-1) * (q-1)
print(pn)
d = e**-1 % pn
print(d)
M = C**d % n
print(M)
print(C ** (e ** -1 % ( (p-1) * (q - 1) ) ) % n)
"""

#x = 8/3

#deling = f""" 8 / 3 = {x:.4f}"""
#print(deling)


print( (1/7) % 289)
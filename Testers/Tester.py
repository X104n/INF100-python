import sys, time

def encrypting(M, e, n):
    # C = M^e mod n
    C = M ** e % n
    return C
"""
def decrypting(C, e, n):
    # M = C^d mod n
    # d = e^-1 mod phi(n)
    # phi(n) = (p-1) (q-1)

    x = 2

    while x >= n
        if n % x == 0:
            print(x)
            n = n/x
        else:
            x += 1
"""

start = input("Would you like to (e)ncrypt or (d)ecrypt: ")
if start == "e" or start == "d":
    print("Welcome")
else:
    print("You did not follow instructions >:(")
    time.sleep(5)
    sys.exit()

M = int(input("Skriv inn M: "))
e = int(input("Skriv inn e: "))
n = int(input("Skriv inn n: "))
print(encrypting(M, e, n))
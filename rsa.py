import math

def gcd(a, h):
    while True:
        temp = a % h
        if temp == 0:
            return h
        a = h
        h = temp

p = int(input("Enter a prime number: "))
q = int(input("Enter another prime number: "))
n = p * q
e = 2
phi = (p - 1) * (q - 1)

while e < phi:
    if gcd(e, phi) == 1:
        break
    e += 1

d = 2
while d < phi:
    if (d * e) % phi == 1:
        break
    d += 1

print("Public Key: (", e, ", ", n, ")")
print("Private Key: (", d, ", ", n, ")")
msg = int(input("Enter the message to be encrypted: "))
print("Message data = ", msg)
c = pow(msg, e)
c = c % n
print("Encrypted data = ", c)
m = pow(c, d)
m = m % n
print("Original Message Sent = ", m)
import random

P = 23
G = 5

X_A = random.randint(1, P-1)
X_B = random.randint(1, P-1)

Y_A = pow(G, X_A, P)
Y_B = pow(G, X_B, P)

shared_secret_A = pow(Y_B, X_A, P)
shared_secret_B = pow(Y_A, X_B, P)

print(f"Alice's Private Key (X_A): {X_A}")
print(f"Bob's Private Key (X_B): {X_B}")
print(f"Alice's Public Key (Y_A): {Y_A}")
print(f"Bob's Public Key (Y_B): {Y_B}")
print(f"Alice's Shared Secret: {shared_secret_A}")
print(f"Bob's Shared Secret: {shared_secret_B}")

if shared_secret_A == shared_secret_B:
    print("Key exchange successful. Shared secret is established.")
else:
    print("Key exchange failed. Shared secrets do not match.")
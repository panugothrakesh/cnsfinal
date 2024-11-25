def vigenere_encrypt(plaintext, key):
    key = (key * (len(plaintext) // len(key))) + key[:len(plaintext) % len(key)]
    ciphertext = ''
    for p, k in zip(plaintext, key):
        if p.isalpha():
            shift = ord(k.lower()) - ord('a')
            if p.islower():
                ciphertext += chr((ord(p) - ord('a') + shift) % 26 + ord('a'))
            else:
                ciphertext += chr((ord(p) - ord('A') + shift) % 26 + ord('A'))
        else:
            ciphertext += p
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    key = (key * (len(ciphertext) // len(key))) + key[:len(ciphertext) % len(key)]
    plaintext = ''
    for c, k in zip(ciphertext, key):
        if c.isalpha():
            shift = ord(k.lower()) - ord('a')
            if c.islower():
                plaintext += chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
            else:
                plaintext += chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
        else:
            plaintext += c
    return plaintext

plaintext = "HELLO VIGENERE CIPHER"
key = "KEY"

ciphertext = vigenere_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")

decrypted_text = vigenere_decrypt(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")
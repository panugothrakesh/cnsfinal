def vernam_encrypt(plaintext, key):
    if len(plaintext) != len(key):
        raise ValueError("Key must be the same length as plaintext")
    ciphertext = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, key))
    return ciphertext

def vernam_decrypt(ciphertext, key):
    if len(ciphertext) != len(key):
        raise ValueError("Key must be the same length as ciphertext")
    plaintext = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(ciphertext, key))
    return plaintext

plaintext = "HELLO"
key = "XMCKL"

ciphertext = vernam_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")

decrypted_text = vernam_decrypt(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")
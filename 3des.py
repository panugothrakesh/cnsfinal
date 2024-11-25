from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def generate_key():
    key_size = 24
    return get_random_bytes(key_size)

def triple_des_encrypt(plaintext, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    padded_plaintext = pad(plaintext.encode(), DES3.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def triple_des_decrypt(ciphertext, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), DES3.block_size)
    return plaintext.decode()

if __name__ == "__main__":
    key = generate_key()
    plaintext = "Confidential Data"
    print(f"Original Plaintext: {plaintext}")
    ciphertext = triple_des_encrypt(plaintext, key)
    print(f"Ciphertext (in hex): {ciphertext.hex()}")
    decrypted_text = triple_des_decrypt(ciphertext, key)
    print(f"Decrypted Plaintext: {decrypted_text}")
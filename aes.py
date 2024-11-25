from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

BLOCK_SIZE = AES.block_size
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC)
iv = cipher.iv
data = b"Confidential Data"
padded_data = pad(data, BLOCK_SIZE)
ciphertext = cipher.encrypt(padded_data)
print(f"Ciphertext (encrypted data): {ciphertext}")
cipher_decrypt = AES.new(key, AES.MODE_CBC, iv=iv)
decrypted_padded_data = cipher_decrypt.decrypt(ciphertext)
decrypted_data = unpad(decrypted_padded_data, BLOCK_SIZE)
print(f"Decrypted data: {decrypted_data.decode('utf-8')}")
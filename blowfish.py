from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
import base64

class SimpleBlowfish:
    def __init__(self, key):
        self.key=key
        self.bs=Blowfish.block_size

    def encrypt(self, plaintext):
        cipher=Blowfish.new(self.key,Blowfish.MODE_ECB)
        padded_data=pad(plaintext.encode('utf-8'),self.bs)
        encrypted_bytes=cipher.encrypt(padded_data)
        encrypted_string=base64.b64encode(encrypted_bytes).decode('utf-8')
        return encrypted_string

    def decrypt(self, encrypted_string):
        encrypted_bytes=base64.b64decode(encrypted_string)
        cipher=Blowfish.new(self.key,Blowfish.MODE_ECB)
        decrypted_padded=cipher.decrypt(encrypted_bytes)
        return unpad(decrypted_padded,self.bs).decode('utf-8')

if __name__=="__main__":
    key=b'SimpleKey12345'
    blowfish=SimpleBlowfish(key)
    string_to_encrypt=input("Enter the string to encrypt: ")
    encrypted=blowfish.encrypt(string_to_encrypt)
    print(f"Encrypted Value: {encrypted}")
    decrypted=blowfish.decrypt(encrypted)
    print(f"Decrypted Value: {decrypted}")
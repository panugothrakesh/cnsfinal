def swap(a,b):
    return b,a

def KSA(key):
    key_length=len(key)
    S=list(range(256))
    j=0
    for i in range(256):
        j=(j+S[i]+key[i%key_length])%256
        S[i],S[j]=swap(S[i],S[j])
    return S

def PRGA(S,data_length):
    i=0
    j=0
    keystream=[]
    for _ in range(data_length):
        i=(i+1)%256
        j=(j+S[i])%256
        S[i],S[j]=swap(S[i],S[j])
        K=S[(S[i]+S[j])%256]
        keystream.append(K)
    return keystream

def rc4(key,data):
    key=[ord(c) for c in key]
    S=KSA(key)
    keystream=PRGA(S,len(data))
    return [data[i]^keystream[i] for i in range(len(data))]

def main():
    key=input("Enter the key: ")
    plaintext=input("Enter the plaintext: ")
    plaintext_bytes=[ord(c) for c in plaintext]
    ciphertext=rc4(key,plaintext_bytes)
    print("Ciphertext: ",end="")
    for byte in ciphertext:
        print(f"{byte:02X}",end=" ")
    print()
    decrypted_bytes=rc4(key,ciphertext)
    decrypted_text=''.join([chr(byte) for byte in decrypted_bytes])
    print("Decrypted Text:",decrypted_text)

if __name__=="__main__":
    main()
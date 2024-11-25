import numpy as np
N = 3

def encrypt(key, item):
    key_matrix = np.array([ord(char) - ord('A') for char in key]).reshape(N, N)
    item_matrix = np.array([ord(char) - ord('A') for char in item])
    encrypted_matrix = np.dot(key_matrix, item_matrix) % 26
    encrypted_message = ''.join(chr(int(num) + ord('A')) for num in encrypted_matrix)
    return encrypted_message

def decrypt(inverse_key_matrix, encrypted_message):
    encrypted_matrix = np.array([ord(char) - ord('A') for char in encrypted_message])
    decrypted_matrix = np.dot(inverse_key_matrix, encrypted_matrix) % 26
    decrypted_message = ''.join(chr(int(num) + ord('A')) for num in decrypted_matrix)
    return decrypted_message

if __name__ == "__main__":
    key = "GYBNQKURP"  # Key for the Hill Cipher (3x3 matrix)
    item = "ACT"       # Message to be encrypted (must have a length of N)
    encrypted_message = encrypt(key, item)
    print(f"Encrypted Message: {encrypted_message}")
    inverse_key_matrix = np.array([
        [8, 5, 10],
        [21, 8, 21],
        [21, 12, 8]
    ])
    decrypted_message = decrypt(inverse_key_matrix, encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")
import math

def simple_columnar_encrypt(plaintext, key):
    """Encrypts plaintext using a simple columnar transposition technique."""
    # Create the grid
    num_cols = len(key)
    num_rows = math.ceil(len(plaintext) / num_cols)
    grid = ['' for _ in range(num_cols)]

    # Fill the grid row by row
    for i, char in enumerate(plaintext):
        grid[i % num_cols] += char

    # Sort the columns by the key
    sorted_indices = sorted(range(num_cols), key=lambda k: key[k])
    ciphertext = ''.join(grid[i] for i in sorted_indices)

    return ciphertext

def simple_columnar_decrypt(ciphertext, key):
    """Decrypts ciphertext using a simple columnar transposition technique."""
    num_cols = len(key)
    num_rows = math.ceil(len(ciphertext) / num_cols)
    sorted_indices = sorted(range(num_cols), key=lambda k: key[k])

    grid = ['' for _ in range(num_cols)]

    # Calculate actual column lengths
    col_lengths = [num_rows] * num_cols
    for i in range(len(ciphertext) % num_cols):
        col_lengths[i] -= 1

    # Fill the grid column by column
    pos = 0
    for index in sorted_indices:
        grid[index] = ciphertext[pos:pos + col_lengths[index]]
        pos += col_lengths[index]

    # Read the plaintext row by row
    plaintext = ''.join(''.join(row) for row in zip(*grid))
    return plaintext

def advanced_columnar_encrypt(plaintext, key1, key2):
    """Encrypts plaintext using advanced columnar transposition with double transposition."""
    intermediate_cipher = simple_columnar_encrypt(plaintext, key1)
    return simple_columnar_encrypt(intermediate_cipher, key2)

def advanced_columnar_decrypt(ciphertext, key1, key2):
    """Decrypts ciphertext using advanced columnar transposition with double transposition."""
    intermediate_plain = simple_columnar_decrypt(ciphertext, key2)
    return simple_columnar_decrypt(intermediate_plain, key1)

if __name__ == "__main__":
    plaintext = "HELLO, WORLD!"
    key1 = "ZEBRA"  # Key for simple columnar encryption
    key2 = "PLANE"

    encrypted_text = simple_columnar_encrypt(plaintext, key2)
    print("Simple Columnar Encryption : ",encrypted_text)

    print('Simple Columnar Encryption')
    decrypted_text = simple_columnar_decrypt(encrypted_text,key2)
    print("Simple Columnar Decryption : ",decrypted_text)
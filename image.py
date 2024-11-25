import cv2
import numpy as np
from matplotlib import pyplot as plt

def encrypt_image(image_path, key):
    """Encrypts an image by applying a bitwise XOR operation with a key."""
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Load the image in grayscale
    encrypted_image = np.bitwise_xor(image, key)  # XOR each pixel with the key
    cv2.imwrite("encrypted_image.png", encrypted_image)
    return encrypted_image

def decrypt_image(encrypted_image, key):
    """Decrypts an image by reversing the XOR operation with the same key."""
    decrypted_image = np.bitwise_xor(encrypted_image, key)
    cv2.imwrite("decrypted_image.png", decrypted_image)
    return decrypted_image

def display_images(original, encrypted, decrypted):
    """Displays the original, encrypted, and decrypted images side by side."""
    plt.figure(figsize=(12, 4))

    # Original Image
    plt.subplot(1, 3, 1)
    plt.title("Original Image")
    plt.imshow(original, cmap='gray')
    plt.axis('off')

    # Encrypted Image
    plt.subplot(1, 3, 2)
    plt.title("Encrypted Image")
    plt.imshow(encrypted, cmap='gray')
    plt.axis('off')

    # Decrypted Image
    plt.subplot(1, 3, 3)
    plt.title("Decrypted Image")
    plt.imshow(decrypted, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

# Main Script
image_path = '/content/sample_data/pngtype.jpeg'  # Replace with your image path
key = 25  # Encryption key (must be kept secret)

# Load original image
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Encrypt and decrypt the image
encrypted_image = encrypt_image(image_path, key)
decrypted_image = decrypt_image(encrypted_image, key)

# Display the images
display_images(original_image, encrypted_image, decrypted_image)
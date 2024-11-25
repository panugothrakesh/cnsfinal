import hashlib

def hash_image(image_path):
    with open(image_path, "rb") as f:
        image_data = f.read()
        image_hash = hashlib.sha256(image_data).hexdigest()
        return image_hash

# Calculate hash
image_hash = hash_image("/content/sample_data/pngtype.jpeg")
print("Image Hash:", image_hash)
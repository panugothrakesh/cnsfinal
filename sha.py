import hashlib

text = "Hello, this is a sample text for SHA-1 digest."
sha1_hash = hashlib.sha1()
sha1_hash.update(text.encode('utf-8'))
digest = sha1_hash.hexdigest()
print(f"SHA-1 Digest: {digest}")
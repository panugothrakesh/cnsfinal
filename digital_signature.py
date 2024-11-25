from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate RSA Key Pair (Private and Public Keys)
def generate_keys():
    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()

    # Save private and public keys to files
    with open('private_key.pem', 'wb') as private_file:
        private_file.write(private_key.export_key())
    with open('public_key.pem', 'wb') as public_file:
        public_file.write(public_key.export_key())

    return private_key, public_key

# Sign a message
def sign_message(message, private_key):
    # Hash the message
    message_hash = SHA256.new(message.encode('utf-8'))

    # Create the signature
    signature = pkcs1_15.new(private_key).sign(message_hash)

    return signature

# Verify the signature
def verify_signature(message, signature, public_key):
    # Hash the message
    message_hash = SHA256.new(message.encode('utf-8'))

    try:
        # Verify the signature
        pkcs1_15.new(public_key).verify(message_hash, signature)
        return True
    except (ValueError, TypeError):
        return False

if __name__ == "__main__":
    private_key, public_key = generate_keys()
    message = "This is a secure message."
    signature = sign_message(message, private_key)
    is_valid = verify_signature(message, signature, public_key)
    if is_valid:
        print("The signature is valid.")
    else:
        print("The signature is invalid.")
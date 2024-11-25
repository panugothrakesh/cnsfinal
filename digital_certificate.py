from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from datetime import datetime, timedelta

# Step 1: Generate RSA Private Key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Step 2: Define Certificate Subject and Issuer (self-signed)
subject = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "IN"),  # Country
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Telangana"),  # State
    x509.NameAttribute(NameOID.LOCALITY_NAME, "Hyderabad"),  # City
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Simple Example Inc."),  # Organization
    x509.NameAttribute(NameOID.COMMON_NAME, "example.com"),  # Domain or Common Name
])

# Step 3: Build the Certificate
certificate = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    subject  # Self-signed, so issuer is the same as subject
).public_key(
    private_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.utcnow()  # Start validity
).not_valid_after(
    datetime.utcnow() + timedelta(days=365)  # Valid for 1 year
).sign(
    private_key, hashes.SHA256()  # Sign the certificate with the private key
)

# Step 4: Save Private Key and Certificate to Files
with open("private_key.pem", "wb") as key_file:
    key_file.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,  # Corrected Encoding
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ))

with open("certificate.pem", "wb") as cert_file:
    cert_file.write(certificate.public_bytes(
        encoding=serialization.Encoding.PEM  # Corrected Encoding
    ))

print("Private key and certificate created successfully!")
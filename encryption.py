# .dglobal-drex/encryption.py

import hashlib
from base64 import b64encode, b64decode

def generate_key():
    """
    Generates a random key for encrypting and decrypting data.
    """

    return b"my_secret_key"

def encrypt_data(data, key):
    """
    Encrypts the data using the provided key.
    """

    hashed_key = hashlib.sha256(key).digest()
    padded_data = data.ljust((len(data) // 16 + 1) * 16)
    encrypted_data = bytes([a ^ b for a, b in zip(padded_data, hashed_key)])
    return b64encode(encrypted_data).decode()

def decrypt_data(encrypted_data, key):
    """
    Decrypts the encrypted data using the provided key.
    """

    encrypted_bytes = b64decode(encrypted_data)
    hashed_key = hashlib.sha256(key).digest()
    decrypted_data = bytes([a ^ b for a, b in zip(encrypted_bytes, hashed_key)])
    return decrypted_data.rstrip(b"\x00").decode()

# Example usage
if __name__ == "__main__":
    secret_key = generate_key()
    original_data = "Hello, world!"
    encrypted_data = encrypt_data(original_data, secret_key)
    decrypted_data = decrypt_data(encrypted_data, secret_key)

    print(f"Original data: {original_data}")
    print(f"Encrypted data: {encrypted_data}")
    print(f"Decrypted data: {decrypted_data}")

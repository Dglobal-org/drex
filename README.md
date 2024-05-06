# Dglobal Drex

Dglobal Drex provides functions for secure data encryption, decryption, key generation, and hashing.

## Installation

You can install the library using pip:

```bash
pip install dglobal-drex
```

## Usage

```python
from dglobal-drex import generate_key, encrypt_data, decrypt_data

# Generate a secret key
secret_key = generate_key()

# Encrypt data
original_data = "Hello, world!"
encrypted_data = encrypt_data(original_data, secret_key)

# Decrypt data
decrypted_data = decrypt_data(encrypted_data, secret_key)

print(f"Original data: {original_data}")
print(f"Encrypted data: {encrypted_data}")
print(f"Decrypted data: {decrypted_data}")
```

## Functions

- `generate_key()`: Generates a random key for encryption and decryption.
- `encrypt_data(data, key)`: Encrypts the provided data using the given key.
- `decrypt_data(encrypted_data, key)`: Decrypts the encrypted data using the key.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you find any bugs or want to improve the library.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Dglobal-org/drex/blob/main/LICENSE) file for details.

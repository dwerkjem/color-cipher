# Color Based Cryptography

## Description

This is a Python program that encrypts and decrypts text using color-based cryptography. The program utilizes a key that is used for both encryption and decryption of the text. The structure of the key is as follows:

```Pseudo code
key 'MMEEIIIIII'

MM - Mode of encryption
EE - Error correction level
IIII - Initialization vector

example key '2K54332221'
```

## Usage

### Encryption

To encrypt a text, you will need to provide the key and the text to be encrypted.

```python
# Example code for encryption
key = '2K54332221'
text = 'Hello, World!'
encrypted_text = encrypt(text, key)
print(encrypted_text)
```

### Decryption

To decrypt a text, you will need to provide the same key used for encryption and the encrypted text.

```python
# Example code for decryption
key = '2K54332221'
encrypted_text = '...'  # the encrypted text
decrypted_text = decrypt(encrypted_text, key)
print(decrypted_text)
```

## Documentation

For more details on contributing to this project, please refer to [docs/contributing.md](docs/contributing.md).

For licensing information, please refer to [docs/license.md](docs/license.md).

## License

This project is licensed under terms that allow use for any non-profit ventures and permits profit-making ventures only with written consent from the owner, Derek R. Neilson. For more information, see [docs/license.md](docs/license.md).

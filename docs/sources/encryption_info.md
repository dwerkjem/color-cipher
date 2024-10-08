# Cryptographic Info

- [Cryptographic Info](#cryptographic-info)
  - [Encryption](#encryption)
    - [What is Encryption?](#what-is-encryption)
    - [How Does Encryption Work?](#how-does-encryption-work)
    - [Overview of Color Cipher Encryption](#overview-of-color-cipher-encryption)
      - [Method of Encryption](#method-of-encryption)
      - [Advantages of Color Cipher Encryption](#advantages-of-color-cipher-encryption)
      - [Limitations of Color Cipher Encryption](#limitations-of-color-cipher-encryption)
      - [Variations of Color Cipher Encryption](#variations-of-color-cipher-encryption)

## Encryption

### What is Encryption?

Encryption is the process of converting data into a code to prevent unauthorized access. It is a way of protecting data by converting it into a code that can only be read by someone who has the key to decode it. Encryption is used to protect data in transit and at rest.

### How Does Encryption Work?

Encryption works by taking data and converting it into a format that is unreadable without the key to decrypt it. The key is a piece of information that is used to encrypt and decrypt the data. The key can be a password, a passphrase, or a cryptographic key.

### Overview of Color Cipher Encryption

Color Cipher encryption is a method of encrypting data using images (steganography) and a key. The key is used to encode and decode the data hidden in the images. The data is hidden in the color values of the pixels in the images.

For more information on steganography, you can refer to the following resources:
- [Wikipedia on Steganography](https://en.wikipedia.org/wiki/Steganography)
- [Steganography Techniques - GeeksforGeeks](https://www.geeksforgeeks.org/steganography-techniques/)
- [Introduction to Steganography - Digital Forensics Magazine](https://www.digitalforensicsmagazine.com/index.php?option=com_content&view=article&id=62:introduction-to-steganography&catid=43:steganography&Itemid=69)

#### Method of Encryption

The Color Cipher encryption method involves the following steps:

1. **Data Encoding**: The data to be encrypted is encoded into binary format.
2. **Image Selection**: An image is selected to hide the data in. An algorithm is used to determine the viability of the image for steganographic encryption.
3. **Key Generation**: A key is generated to encrypt and decrypt the data.
4. **Data Embedding**: The data is embedded into the image using the color values of the pixels.

#### Advantages of Color Cipher Encryption

- **Obscurity**: The data is hidden in plain sight, making it difficult to detect.
- **Security**: The encryption process makes it difficult for unauthorized users to access the data.
- **Ease of Use**: The encryption and decryption process is straightforward and can be done with minimal technical knowledge.

#### Limitations of Color Cipher Encryption

- **Speed**: The encryption process can be slow, especially for large amounts of data.
- **Detection**: If the source image is widely known, the presence of hidden data can be detected.
- **Key Management**: The security of the encryption relies on the strength of the key used.
- **Data Loss**: If the image is compressed or altered, the hidden data may be lost.

For more information on the Color Cipher encryption method, you can refer to the following [method documentation](../method/method.md).

Inspired by the [AES encryption method](https://www.techtarget.com/searchsecurity/definition/Advanced-Encryption-Standard#:~:text=The%20Advanced%20Encryption%20Standard%20(AES)%20is%20a%20symmetric%20block%20cipher,cybersecurity%20and%20electronic%20data%20protection.).

#### Variations of Color Cipher Encryption

There are several variations of the Color Cipher encryption method that can be used to enhance security and obfuscation. From least complex to most complex, these variations include:

1. **1 I**: First Insecure Variation, Basic encryption with no key.
  - **Security Level**: Low
  - **Complexity**: Low
  - **Key**: None
  - **Use Case**: Basic data hiding for non-sensitive information. Not recommended for sensitive data. maybe useful for educational purposes.
  - **No Input Image**: The data is hidden in a randomly generated image.

<!-- TODO: Add more variations.  -->
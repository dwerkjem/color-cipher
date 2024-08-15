# Cryptographic Info

- [Cryptographic Info](#cryptographic-info)
  - [Encryption](#encryption)
    - [What is Encryption?](#what-is-encryption)
    - [How Does Encryption Work?](#how-does-encryption-work)
    - [Overview of Color Cipher Encryption](#overview-of-color-cipher-encryption)
      - [Method of Encryption](#method-of-encryption)
      - [Advantages of Color Cipher Encryption](#advantages-of-color-cipher-encryption)
      - [Limitations of Color Cipher Encryption](#limitations-of-color-cipher-encryption)
    - [in-depth](#in-depth)
      - [Data Encoding](#data-encoding)

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

### in-depth

#### Data Encoding

The data to be encrypted (plaintext) is encoded into binary format using a 6 bit encoding scheme. Each character in the plaintext is encoded into a 6 bit binary value.

The encoding scheme used in Color Cipher encryption is as follows:

```plaintext
               Value  Binary
0                     000000
1                  1  000001
2                  2  000010
3                  3  000011
4                  4  000100
5                  5  000101
6                  6  000110
7                  7  000111
8                  8  001000
9                  9  001001
10                 0  001010
11                 a  001011
12                 b  001100
13                 c  001101
14                 d  001110
15                 e  001111
16                 f  010000
17                 g  010001
18                 h  010010
19                 i  010011
20                 j  010100
21                 k  010101
22                 l  010110
23                 m  010111
24                 n  011000
25                 o  011001
26                 p  011010
27                 q  011011
28                 r  011100
29                 s  011101
30                 t  011110
31                 u  011111
32                 v  100000
33                 w  100001
34                 x  100010
35                 y  100011
36                 z  100100
37       END OF LINE  100101
38       END OF TEXT  100110
39     START OF TEXT  100111
40             blank  101000
41  START OF NEW KEY  101001
42    END OF NEW KEY  101010
43         UPPERCASE  101011
44   START OF SYMBOL  101100
45     END OF SYMBOL  101101
46        SKIP AHEAD  101110
47            REPEAT  101111
```

Each Color has 3 values (RGB) and each value can store 8 bits of data. So, each pixel can store 24 bits of data. Or 4 characters of the encoded data.

The Colors need to be converted to an integer to store the data.

To convert a color represented by its Red, Green, and Blue (RGB) components in 24-bit color depth to an integer, you would use the formula:

\[
\text{Color\_int} = (R \times 2^{16}) + (G \times 2^8) + B
\]

Where:
- \( R \) is the red component (8 bits)
- \( G \) is the green component (8 bits)
- \( B \) is the blue component (8 bits)

To convert an integer to a color represented by its Red, Green, and Blue (RGB) components in 24-bit color depth, you would use the formula:

\[
R = \left(\frac{\text{Color\_int}}{2^{16}}\right) \mod 256
\]
\[
G = \left(\frac{\text{Color\_int}}{2^{8}}\right) \mod 256
\]
\[
B = \text{Color\_int} \mod 256
\]


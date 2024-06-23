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

### Installation

To run the program, you will need to install the required dependencies. You can use Docker, pyvenv, or Poetry to set up the environment. docker is recommended for running the program.

#### Docker (Recommended)

To run the program using Docker, you can build the Docker image and run the container.

```bash
docker build -t color-cipher .
docker run -it color-cipher
```

#### pyvenv

To run the program using a Python virtual environment, you can create a virtual environment and install the required packages.

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### poetry

To run the program using Poetry, you can install the dependencies using Poetry.

```bash
poetry install
```

### Encryption

TODO: Add instructions for encryption and decryption.

### Decryption

TODO: Add instructions for encryption and decryption.

## Documentation

For more details on contributing to this project, please refer to [docs/contributing.md](docs/contributing.md).

For licensing information, please refer to [docs/license.md](docs/license.md).

## License

This project is licensed under terms that allow use for any non-profit ventures and permits profit-making ventures only with written consent from the owner, Derek R. Neilson. For more information, see [docs/license.md](docs/license.md).

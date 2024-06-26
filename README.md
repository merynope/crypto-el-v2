# Quantum-Resistant Messaging 🔐

## Introduction

This project demonstrates how to securely send a message using advanced cryptographic techniques that are secure even against future quantum computers. The goal of this app is to showcase quantum-resistant technologies and educate users on how these technologies work practically. It utilizes the Kyber512 algorithm for key encapsulation and AES for message encryption.

## Features

- **Key Pair Generation:** Generate a public and private key pair using the Kyber512 algorithm.
- **Public Key Exchange:** Share the public key with the receiver.
- **Shared Secret Encryption:** Use the public key to create and encrypt a shared secret.
- **Shared Secret Decryption:** Decrypt the shared secret using the private key.
- **Message Encryption:** Encrypt a message using AES with the shared secret.
- **Message Decryption:** Decrypt the message using AES with the shared secret.
- **Educational Explanations:** Step-by-step explanations of the cryptographic processes.

## Overview

The project is divided into two phases:

1. **Authentication**
2. **Message Encryption**

### Phase 1: Authentication

1. **Generate Key Pair:** The sender creates a set of keys. One key can be shared (public key) and the other is kept secret (private key).
2. **Send Public Key:** The sender shares the public key with the receiver.
3. **Encrypt Shared Secret:** The receiver uses the public key to create a secret that only the sender can decrypt.
4. **Send Encrypted Shared Secret:** The receiver sends the encrypted secret back to the sender.
5. **Decrypt Shared Secret:** The sender uses their private key to decrypt the secret.

### Phase 2: Message Encryption

6. **Encrypt Message:** The sender uses the shared secret to encrypt a message and sends it to the receiver.
7. **Decrypt Message:** The receiver uses the shared secret to decrypt the message.

## Liboqs and AES in PQC

### Liboqs

Liboqs is an open-source C library for quantum-resistant cryptographic algorithms. It is part of the Open Quantum Safe (OQS) project, which aims to develop and prototype quantum-resistant cryptography. In this project, we use Liboqs to leverage the Kyber512 algorithm for secure key encapsulation.

### AES in PQC

AES (Advanced Encryption Standard) is a widely used symmetric encryption algorithm. In the context of post-quantum cryptography (PQC), we use AES for the actual message encryption and decryption. The shared secret generated through the Kyber512 algorithm is used as a key for AES, ensuring that the encryption remains secure even against quantum computer attacks.

## Running the Project

### Prerequisites

- Python 3.x
- Streamlit
- Liboqs
- Liboqs-python
- PyCryptodome

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/quantum-resistant-messaging.git
    cd quantum-resistant-messaging
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

## License

This project is licensed under the MIT License.

## Acknowledgements

- Open Quantum Safe Project
- PyCryptodome Library

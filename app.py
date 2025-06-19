import streamlit as st
import oqs
from Crypto.Cipher import AES
import hashlib
import base64

st.set_page_config(page_title="Quantum-Resistant Messaging", page_icon="📱")

st.title("Quantum-Resistant Messaging 🔐")
st.markdown("This guide will show you how to securely send a message using advanced cryptographic techniques that are secure even against future quantum computers.")

# Function to encrypt a message using AES
def encrypt_message(shared_secret, message):
    key = hashlib.sha256(shared_secret).digest()
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
    return nonce, ciphertext, tag

# Function to decrypt a message using AES
def decrypt_message(shared_secret, nonce, ciphertext, tag):
    key = hashlib.sha256(shared_secret).digest()
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted_message = cipher.decrypt_and_verify(ciphertext, tag)
    return decrypted_message.decode('utf-8')

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'public_key' not in st.session_state:
    st.session_state.public_key = None
if 'ciphertext' not in st.session_state:
    st.session_state.ciphertext = None
if 'shared_secret_enc' not in st.session_state:
    st.session_state.shared_secret_enc = None
if 'shared_secret_dec' not in st.session_state:
    st.session_state.shared_secret_dec = None
if 'message' not in st.session_state:
    st.session_state.message = ""
if 'decrypted_message' not in st.session_state:
    st.session_state.decrypted_message = ""
if 'encrypted_message' not in st.session_state:
    st.session_state.encrypted_message = ""
if 'nonce' not in st.session_state:
    st.session_state.nonce = None
if 'tag' not in st.session_state:
    st.session_state.tag = None

# Overview of the process
if st.session_state.step == 0:
    st.header("Overview")
    with st.expander("Phase 1: Authentication"):
        st.markdown("""
        1. **Generate Key Pair:** The sender creates a set of keys. One key can be shared (public key) and the other is kept secret (private key).
        2. **Send Public Key:** The sender shares the public key with the receiver.
        3. **Encrypt Shared Secret:** The receiver uses the public key to create a secret that only the sender can decrypt.
        4. **Send Encrypted Shared Secret:** The receiver sends the encrypted secret back to the sender.
        5. **Decrypt Shared Secret:** The sender uses their private key to decrypt the secret.
        """)
    with st.expander("Phase 2: Message Encryption"):
        st.markdown("""
        6. **Encrypt Message:** The sender uses the shared secret to encrypt a message and sends it to the receiver.
        7. **Decrypt Message:** The receiver uses the shared secret to decrypt the message.
        """)
    if st.button("**Start Process**"):
        st.session_state.step = 1
        st.rerun()

# Phase 1: Authentication Kyber1024 can be used instead of Kyber512
if st.session_state.step >= 1:
    st.header("Phase 1: Authentication")

if st.session_state.step >= 1:
    st.subheader("Step 1: Generate Key Pair")
    st.markdown("""The sender creates a set of keys using the Kyber512 algorithm.
    """, help="Kyber512 is a post-quantum key encapsulation mechanism (KEM) based on lattice cryptography. It is designed to be secure against quantum computer attacks, which could potentially break traditional cryptographic algorithms like RSA and ECC.")
    if st.session_state.step == 1 and st.button("Generate Key Pair with Kyber512"):
        kemalg = "Kyber512"
        st.session_state.kem = oqs.KeyEncapsulation(kemalg)
        st.session_state.public_key = st.session_state.kem.generate_keypair()
        st.session_state.step = 2
        st.rerun()
    if st.session_state.public_key is not None:
        st.success("Public Key generated successfully.")

if st.session_state.step >= 2:
    st.subheader("Step 2: Send Public Key to Receiver")
    st.markdown("""The sender shares the **public key** with the receiver. The receiver will use this public key to create a secret that only the sender can decrypt.
    """)
    if st.session_state.public_key is not None:
        st.code(st.session_state.public_key, language='python')
        if st.session_state.step == 2 and st.button("Send Public Key"):
            st.session_state.step = 3
            st.rerun()
    if st.session_state.step > 2:
        st.success("Public Key sent to Receiver.")

if st.session_state.step >= 3:
    st.subheader("Step 3: Encrypt Shared Secret")
    st.markdown("""The receiver uses the public key to create a secret that only the sender can decrypt. This secret is then encrypted so that only the sender can read it.
    """)
    if st.session_state.public_key is not None:
        st.code(st.session_state.public_key, language='python')
        if st.session_state.step == 3 and st.button("Encrypt Shared Secret"):
            st.session_state.ciphertext, st.session_state.shared_secret_enc = st.session_state.kem.encap_secret(st.session_state.public_key)
            st.session_state.step = 4
            st.rerun()
    if st.session_state.ciphertext is not None:
        st.success("Shared secret encrypted successfully.")

if st.session_state.step >= 4:
    st.subheader("Step 4: Send Encrypted Shared Secret to Sender")
    st.markdown("""The receiver sends the **encrypted shared secret** back to the sender. The sender will use their private key to decrypt this secret.
    """)
    if st.session_state.ciphertext is not None:
        st.code(f"Ciphertext: {base64.b64encode(st.session_state.ciphertext).decode('utf-8')}", language='python')
        st.code(f"Encrypted Shared Secret: {base64.b64encode(st.session_state.shared_secret_enc).decode('utf-8')}", language='python')
        if st.session_state.step == 4 and st.button("Send Encrypted Shared Secret"):
            st.session_state.step = 5
            st.rerun()
    if st.session_state.step > 4:
        st.success("Encrypted Shared Secret sent to Sender.")

if st.session_state.step >= 5:
    st.subheader("Step 5: Decrypt Shared Secret")
    st.markdown("""The sender uses their private key to decrypt the shared secret from the receiver. This ensures that only the sender can access the shared secret.
    """)
    if st.session_state.ciphertext is not None:
        st.code(f"Ciphertext: {base64.b64encode(st.session_state.ciphertext).decode('utf-8')}", language='python')
        st.code(f"Encrypted Shared Secret: {base64.b64encode(st.session_state.shared_secret_enc).decode('utf-8')}", language='python')
        if st.session_state.step == 5 and st.button("Decrypt Shared Secret"):
            st.session_state.shared_secret_dec = st.session_state.kem.decap_secret(st.session_state.ciphertext)
            st.session_state.step = 6
            st.rerun()
    if st.session_state.shared_secret_dec is not None:
        st.success("Shared secret decrypted successfully.")

# Phase 2: Message Encryption
if st.session_state.step >= 6:
    st.header("Phase 2: Message Encryption")

if st.session_state.step >= 6:
    st.subheader("Step 6: Encrypt a Message and Send to Receiver")
    st.markdown("""The sender uses the shared secret to encrypt a message using AES. The encrypted message is then sent to the receiver.
    """, help="AES (Advanced Encryption Standard) is a widely used symmetric encryption algorithm that ensures data security. By using the shared secret, we can encrypt and decrypt messages securely.")
    if st.session_state.shared_secret_dec is not None:
        st.code(f"Decrypted Shared Secret: {base64.b64encode(st.session_state.shared_secret_dec).decode('utf-8')}", language='python')
        st.session_state.message = st.text_input("Enter a message to encrypt", "Please encrypt this text. I don't want anyone to see it.")
        if st.session_state.step == 6 and st.button("Encrypt & Send Message using AES"):
            nonce, ciphertext, tag = encrypt_message(st.session_state.shared_secret_enc, st.session_state.message)
            st.session_state.encrypted_message = base64.b64encode(ciphertext).decode('utf-8')
            st.session_state.nonce = nonce
            st.session_state.tag = tag
            st.session_state.step = 7
            st.rerun()
    if st.session_state.encrypted_message:
        st.success("Message encrypted successfully and sent to Receiver.")

if st.session_state.step >= 7:
    st.subheader("Step 7: Decrypt the Message")
    st.markdown("""The receiver uses the shared secret to decrypt the message from the sender.
    """)
    if st.session_state.encrypted_message:
        st.code(f"Encrypted Message (base64): {st.session_state.encrypted_message}", language='python')
        if st.session_state.step == 7 and st.button("Decrypt Message"):
            st.session_state.decrypted_message = decrypt_message(st.session_state.shared_secret_dec, st.session_state.nonce, base64.b64decode(st.session_state.encrypted_message), st.session_state.tag)
            st.session_state.step = 8
            st.rerun()

if st.session_state.step == 8:
    st.success(f"Decrypted Message: {st.session_state.decrypted_message}")
    if st.button("Start Again"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

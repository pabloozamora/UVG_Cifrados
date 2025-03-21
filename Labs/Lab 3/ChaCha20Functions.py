from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes

def chacha20_encrypt(plaintext, key: bytes, nonce: bytes, decrypt=False):
    """Cifra o descifra un mensaje con ChaCha20"""
    cipher = ChaCha20.new(key=key, nonce=nonce)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def chacha20_decrypt(ciphertext, key: bytes, nonce: bytes):
    """Descifra un mensaje con ChaCha20"""
    cipher = ChaCha20.new(key=key, nonce=nonce)
    message = cipher.decrypt(ciphertext)
    return message.decode()

# Generar clave
def chacha20_generate_random_key():
    return get_random_bytes(32)  # ChaCha20 usa una clave de 256 bits

# Generar nonce
def chacha20_generate_random_nonce():
    return get_random_bytes(12)  # ChaCha20 usa un nonce de 96 bits
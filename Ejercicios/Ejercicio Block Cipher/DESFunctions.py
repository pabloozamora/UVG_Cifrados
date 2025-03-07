from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# Función para aplicar padding
def pad(data):
    padding_len = 8 - (len(data) % 8) # El bloque de DES es de 8 bytes
    return data + bytes([padding_len] * padding_len)

# Función para remover padding
def unpad(data):
    padding_len = data[-1]
    return data[:-padding_len]

# Función para cifrar con DES en modo ECB
def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext.encode())
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

# Función para descifrar con DES en modo ECB
def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_padded_text = cipher.decrypt(ciphertext)
    return unpad(decrypted_padded_text).decode()

# Función para generar una llave aleatoria para DES (8 bytes)
def generate_random_key():
    return get_random_bytes(8)
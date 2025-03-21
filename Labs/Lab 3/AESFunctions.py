from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import numpy as np
import os

# Función para cifrar con AES en modo ECB
def aes_encrypt(image_bytes, key, mode, iv = None):
    cipher = AES.new(key, AES.MODE_ECB) if mode == 'ECB' else AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(image_bytes, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data

# Función para descifrar con AES en modo ECB
def aes_decrypt_ecb(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_padded_data = cipher.decrypt(ciphertext)
    return unpad(decrypted_padded_data, AES.block_size)

# Función para cifrar con AES en modo CBC
def aes_encrypt_cbc(data, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(data, AES.block_size)
    return cipher.encrypt(padded_data)

# Función para descifrar con AES en modo CBC
def aes_decrypt_cbc(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded_data = cipher.decrypt(ciphertext)
    return unpad(decrypted_padded_data, AES.block_size)

# Función para cifrar un archivo con AES en modo CBC
def aes_encrypt_file(input_file, output_file, key, iv):
    with open(input_file, 'rb') as file:
        data = file.read()
        encrypted_data = aes_encrypt_cbc(data, key, iv)
        with open(output_file, 'wb') as output:
            output.write(encrypted_data)

    os.remove(input_file)

# Función para descifrar un archivo con AES en modo CBC
def aes_decrypt_file(input_file, output_file, key, iv):
    with open(input_file, 'rb') as file:
        data = file.read()
        decrypted_data = aes_decrypt_cbc(data, key, iv)
        with open(output_file, 'w') as output:
            decrypted_data = decrypted_data.decode('utf-8')
            output.write(decrypted_data)

    os.remove(input_file)

# Generar una llave aleatoria de 32 bytes
def aes_generate_random_key():
    return get_random_bytes(32)

# Generar un vector de inicialización aleatorio de 16 bytes
def aes_generate_random_iv():
    return get_random_bytes(16)
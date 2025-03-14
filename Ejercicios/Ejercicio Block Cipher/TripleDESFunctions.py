from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Función para cifrar con 3DES en modo CBC
def triple_des_encrypt(plaintext, key, iv):
    cipher = DES3.new(key, DES3.MODE_CBC, iv) 
    padded_text = pad(plaintext.encode(), DES3.block_size)  # Agrega el padding
    ciphertext = cipher.encrypt(padded_text)  # Cifra el texto
    return ciphertext

# Función para descifrar con 3DES en modo CBC
def triple_des_decrypt(ciphertext, key, iv):
    cipher = DES3.new(key, DES3.MODE_CBC, iv) 
    decrypted_padded_text = cipher.decrypt(ciphertext)  # Descifra el texto
    return unpad(decrypted_padded_text, DES3.block_size).decode()  # Elimina el padding

# Generar una llave aleatoria de 24 bytes
def triple_des_generate_random_key():
    return get_random_bytes(24)

# Generar un vector de inicialización aleatorio de 8 bytes
def triple_des_generate_random_iv():
    return get_random_bytes(8)

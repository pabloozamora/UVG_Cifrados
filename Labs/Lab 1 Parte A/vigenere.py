from clean_text import clean_text

alphabet = "abcdefghijklmnñopqrstuvwxyz"

def vigenere_encrypt(text, key):
    encrypted_text = ""
    plain_text = clean_text(text)
    m = len(alphabet)

    key = clean_text(key)
    for i, char in enumerate(plain_text):
        if char in alphabet:
            key_char = key[i % len(key)] # Repetir la clave si es más corta que el texto
            key_index = alphabet.index(key_char)
            encrypted_text += alphabet[(alphabet.index(char) + key_index) % m]
        else:
            encrypted_text += char
    return encrypted_text

def vigenere_decrypt(text, key):
    decrypted_text = ""
    cipher_text = clean_text(text)
    m = len(alphabet)

    key = clean_text(key)
    for i, char in enumerate(cipher_text):
        if char in alphabet:
            key_char = key[i % len(key)] # Repetir la clave si es más corta que el texto
            key_index = alphabet.index(key_char)
            decrypted_text += alphabet[(alphabet.index(char) - key_index) % m]
        else:
            decrypted_text += char
    return decrypted_text
from clean_text import clean_text

alphabet = "abcdefghijklmnñopqrstuvwxyz"

def ceasar_encrypt(text, key):
    encrypted_text = ""
    plain_text = clean_text(text)
    for char in plain_text:
        if char in alphabet:
            encrypted_text += alphabet[(alphabet.index(char) + key) % 26]
        else:
            encrypted_text += char
    return encrypted_text

def ceasar_decrypt(text, key):
    plain_text = ""
    for char in text:
        if char in alphabet:
            plain_text += alphabet[(alphabet.index(char) - key) % 26]
        else:
            plain_text += char
    return plain_text



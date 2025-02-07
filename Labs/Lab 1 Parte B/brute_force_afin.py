from utils import *

alphabet = 'abcdefghijklmnñopqrstuvwxyz'

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def afin_decrypt(text, a, b):
    # Verificar si a y m son coprimos
    if gcd(a, len(alphabet)) != 1:
        raise ValueError("a y m no son coprimos.")
    
    decrypted_text = ""
    cipher_text = clean_text(text)
    m = len(alphabet)
    for char in cipher_text:
        if char in alphabet:
            a_inv = pow(a, -1, m)  # Inversa modular de a
            decrypted_text += alphabet[(a_inv * (alphabet.index(char) - b)) % m]
        else:
            decrypted_text += char
    return decrypted_text

# Prompt realizado a GPT-4o: ¿Cómo puedo hacer un algoritmo en Python que, mediante fuerza bruta, descifre un mensaje cifrado en afines?
def brute_force_afines(text):
    possible_keys = []

    alphabet = 'abcdefghijklmnñopqrstuvwxyz'
    m = len(alphabet)

    for a in range(1, 16):

        if gcd(a, m) != 1: # Si a y m no son coprimos, continuar
            continue

        for b in range(1, 16):
            decyphered_text = ''
            decyphered_text = afin_decrypt(text, a, b)
            score = chi_squared_score(decyphered_text)
            possible_keys.append((a, b, score, decyphered_text))

    # Ordenar por menor Chi-cuadrado
    possible_keys.sort(key=lambda x: x[2])
    return possible_keys

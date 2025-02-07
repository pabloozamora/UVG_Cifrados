from utils import *
import itertools

alphabet = 'abcdefghijklmnñopqrstuvwxyz'

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

# Prompt realizado a GPT-4o: ¿Cómo podría realizar una función de Python que utilice fuerza bruta para descifrar un texto Vigenere?
# Asegúrate de utilizar chi cuadrado para evaluar la calidad de las posibles claves.
def brute_force_vigenere(text, max_key_length=6, prefix=""):
    """ Prueba todas las posibles claves de longitud 1 a max_key_length en Vigenère """
    possible_keys = []

    remaining_length = max_key_length - len(prefix)  # Número de caracteres a generar
    if remaining_length < 0:
        raise ValueError("El prefijo es más largo que la clave esperada")

    for key_tuple in itertools.product(alphabet, repeat=remaining_length):
        key = prefix + ''.join(key_tuple)  # Mantiene el prefijo fijo
        decrypted_text = vigenere_decrypt(text, key)
        score = chi_squared_score(decrypted_text)
        possible_keys.append((key, score, decrypted_text))

    # Ordenar por menor Chi-cuadrado
    possible_keys.sort(key=lambda x: x[1])
    return possible_keys
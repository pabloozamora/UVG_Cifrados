from utils import *

alphabet = 'abcdefghijklmnñopqrstuvwxyz'

def ceasar_decrypt(text, key, m):
    plain_text = ""
    for char in text:
        if char in alphabet:
            plain_text += alphabet[(alphabet.index(char) - key) % m]
        else:
            plain_text += char
    return plain_text

def brute_force_ceasar(text):
     
    m = len(alphabet)
    possible_keys = []

    for i in range(m):
        decyphered_text = ''
        decyphered_text = ceasar_decrypt(text, i, m)
        score = chi_squared_score(decyphered_text)
        possible_keys.append((i, score, decyphered_text))

    # Ordenar por menor Chi-cuadrado
    possible_keys.sort(key=lambda x: x[1])
    return possible_keys
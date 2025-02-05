from clean_text import clean_text

alphabet = "abcdefghijklmnñopqrstuvwxyz"

# Prompt realizado a GPT-4o: Realiza una función para obtener el máximo común divisor de dos números.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def afin_encrypt(text, a, b):
    # Limpiar el texto
    text = clean_text(text)

    # Verificar si a y m son coprimos
    if gcd(a, len(alphabet)) != 1:
        raise ValueError("a y m no son coprimos.")

    encrypted_text = ""
    plain_text = clean_text(text)
    m = len(alphabet)
    for char in plain_text:
        if char in alphabet:
            encrypted_text += alphabet[int((a * alphabet.index(char) + b) % m)]
        else:
            encrypted_text += char
    return encrypted_text

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


from asciiToBinary import ascii_to_binary
from binaryToAscii import binary_to_ascii
from xor import xor

def fixed_key_cypher(text, key):
    cypher_text = ''

    if len(text) > len(key):
        key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
        print(f"Llave extendida: {key}")

    elif len(text) < len(key):
        text = text + '_' * (len(key) - len(text))
        print(f"Texto extendido: {text}")

    binary_text = ascii_to_binary(text)
    binary_key = ascii_to_binary(key)
    xor_output = xor(binary_text, binary_key)
    return xor_output

text = 'hola'
key = '123'
cypher_text = fixed_key_cypher(text, key)
print(f"Texto cifrado (binario): {cypher_text}")
cypher_text = binary_to_ascii(cypher_text)
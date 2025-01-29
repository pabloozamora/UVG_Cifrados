from generateDynamicKey import generate_dynamic_key
from asciiToBinary import ascii_to_binary
from binaryToAscii import binary_to_ascii
from xor import xor

def dynamic_key_cypher(text, key_length):
    cypher_text = ''
    key = generate_dynamic_key(key_length)
    print(f"Llave dinámica: {key}")

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
key_length = 10
cypher_text = dynamic_key_cypher(text, key_length)
print(f"Texto cifrado (binario): {cypher_text}")
cypher_text = binary_to_ascii(cypher_text)

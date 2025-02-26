from xor import xor
from asciiToBinary import ascii_to_binary
from binaryToAscii import binary_to_ascii
from keystream import generate_keystream

def stream_cipher(text, key):
    """Cifra o descifra un texto usando un stream cipher."""
    keystream = generate_keystream(len(text), key)
    print('Keystream generado:', ''.join(keystream))
    binary_text = ascii_to_binary(text)
    binary_keystream = ascii_to_binary(''.join(keystream))
    result = xor(binary_text, binary_keystream)
    return binary_to_ascii(result)
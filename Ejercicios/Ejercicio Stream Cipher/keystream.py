import random

def generate_keystream(length, key):
    """Genera un keystream pseudoaleatorio de la longitud especificada en caracteres ASCII."""
    random.seed(key)
    return [chr(random.randint(0, 255)) for _ in range(length)]
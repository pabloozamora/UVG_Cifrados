import random

def generate_keystream(seed, length):
    random.seed(seed)
    return bytes([random.randint(0, 255) for _ in range(length)])

def decrypt(ciphertext_hex):
    cipherbytes = bytes.fromhex(ciphertext_hex)
    for seed in range(100000):  # Intentar semillas del 0 al 99999
        keystream = generate_keystream(seed, len(cipherbytes))        
        plaintext = bytes([c ^ k for c, k in zip(cipherbytes, keystream)])        
        if plaintext.startswith(b"FLAG_"):  # Condición para detectar la flag
            print(f"Semilla encontrada: {seed}")
            print(f"Texto descifrado: {plaintext.decode()}")
            return
    print('Semilla no encontrada, probar con otro rango de semillas.')

if __name__ == "__main__":
    ciphertext = "a77742694e1300814b396b3d88968e2f17695b659d1a40dc451922b243ac9587ea4c558b6c"
    decrypt(ciphertext)

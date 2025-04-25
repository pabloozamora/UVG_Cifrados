from Crypto.Cipher import ChaCha20

def generate_key_nonce(possible_key, possible_nonce):
    key = (possible_key.encode() * 32)[:32]
    nonce = (possible_nonce.encode() * 8)[:8]
    return key, nonce

def chacha20_decrypt(ciphertext_hex, possible_key, possible_nonce):
    key, nonce = generate_key_nonce(possible_key, possible_nonce)
    ciphertext = bytes.fromhex(ciphertext_hex)
    cipher = ChaCha20.new(key=key, nonce=nonce)
    try:
        plaintext = cipher.decrypt(ciphertext)
        decoded = plaintext.decode()
        if decoded.startswith("FLAG_"):
            print(f"Key correcto: {possible_key}")
            print(f"Nonce correcto: {possible_nonce}")
            print(f"Texto descifrado: {decoded}")
            return True
    except:
        pass
    return False

if __name__ == "__main__":
    ciphertext = "544a8e505d0ab33f35ca53c0dfb7c08c76256474ef478796f5849865098647d7683c2bb75c"
    keywords = ["nami", "21780"]

    for possible_key in keywords:
        for possible_nonce in keywords:
            if chacha20_decrypt(ciphertext, possible_key, possible_nonce):
                break

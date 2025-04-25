from Crypto.Cipher import ARC4
import binascii

# Mensaje cifrado en hexadecimal
ciphertext_hex = "1e7b939f94e066cfc21d5adadf390e1e179446f94148af12945da54560c6b03cc01d835348"

# Convertir a bytes
ciphertext = bytes.fromhex(ciphertext_hex)

# Clave
key = b"21780"

# Inicializar el descifrador RC4
cipher = ARC4.new(key)

# Descifrar
plaintext = cipher.decrypt(ciphertext)

print("Texto descifrado:", plaintext.decode(errors="replace"))

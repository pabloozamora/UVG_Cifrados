import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

key = b'0123456789abcdef'  # Clave de 16 bytes

def send_file_encrypted(filename):
    with open(filename, 'rb') as f:
        data = f.read()

    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))

    # Enviar tamaño del archivo cifrado (4 bytes), IV (16 bytes), y luego los datos
    total_len = len(encrypted_data)
    sock.sendall(total_len.to_bytes(4, byteorder='big') + iv + encrypted_data)
    print(f"Archivo '{filename}' encriptado y enviado exitosamente.")

def send_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()

    # Enviar tamaño del archivo (4 bytes) y luego los datos
    total_len = len(data)
    sock.sendall(total_len.to_bytes(4, byteorder='big') + data)
    print(f"Archivo '{filename}' enviado exitosamente.")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("172.20.10.3", 8080))

try:
    while True:
        filename = input("Ingrese el nombre del archivo a enviar (o 'exit'): ")
        if filename.lower() == 'exit':
            break
        if not os.path.isfile(filename):
            print("Archivo no encontrado.")
            continue
        send_file_encrypted(filename)
finally:
    sock.close()

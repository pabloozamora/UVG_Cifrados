import socket
import os

def receive_file_encrypted(conn):
    # Leer los primeros 4 bytes (tamaño del archivo cifrado)
    raw_size = conn.recv(4)
    if not raw_size:
        return False
    file_size = int.from_bytes(raw_size, byteorder='big')

    # Leer el IV (16 bytes)
    iv = conn.recv(16)

    # Leer los datos cifrados
    data = b''
    while len(data) < file_size:
        chunk = conn.recv(min(4096, file_size - len(data)))
        if not chunk:
            break
        data += chunk

    # Guardar archivo recibido
    with open('archivo_recibido.enc', 'wb') as f:
        f.write(iv + data)  # Guardamos también el IV por si queremos descifrar luego
    print("Archivo recibido y guardado como 'archivo_recibido.enc'")
    return True

def receive_file(conn):
    # Leer los primeros 4 bytes (tamaño del archivo)
    raw_size = conn.recv(4)
    if not raw_size:
        return False
    file_size = int.from_bytes(raw_size, byteorder='big')

    # Leer los datos
    data = b''
    while len(data) < file_size:
        chunk = conn.recv(min(4096, file_size - len(data)))
        if not chunk:
            break
        data += chunk

    # Guardar archivo recibido
    with open('archivo_recibido', 'wb') as f:
        f.write(data)
    print("Archivo recibido y guardado como 'archivo_recibido'")
    return True

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("172.20.10.3", 8080))
server.listen(1)
print("Esperando conexiones en el puerto 8080...")

while True:
    conn, addr = server.accept()
    print(f"Conexión establecida desde {addr}")
    while receive_file(conn):
        pass
    conn.close()

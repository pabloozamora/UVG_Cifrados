def xor_hex_with_key(hex_string, key):
    # Convertir el texto hexadecimal a bytes
    data = bytes.fromhex(hex_string)

    # Extender la clave si es necesario
    key_bytes = key.encode()
    repeated_key = (key_bytes * (len(data) // len(key_bytes) + 1))[:len(data)]

    # Hacer XOR byte por byte
    result = bytes([b ^ k for b, k in zip(data, repeated_key)])
    return result

if __name__ == "__main__":
    hex_string = input("Ingresa el string hexadecimal: ").strip()
    key = input("Ingresa la clave: ").strip()

    result = xor_hex_with_key(hex_string, key)
    print("Resultado del XOR (en texto):", result.decode(errors='replace'))
    print("Resultado del XOR (hex):", result.hex())

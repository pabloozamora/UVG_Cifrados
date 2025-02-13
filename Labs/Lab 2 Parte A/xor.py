def xor(binary_text, binary_key):
    if len(binary_key) > len(binary_text):
        raise ValueError("La llave no puede ser de mayor longitud que el texto.")
    
    elif len(binary_key) < len(binary_text):
        # Agregar padding a la llave
        padding = len(binary_text) - len(binary_key)
        binary_key = padding * '0' + binary_key

    result = ''
    for i in range(len(binary_text)):
        if binary_text[i] == binary_key[i]:
            result += '0'
        else:
            result += '1'

    return result

if __name__ == "__main__":
    binary_text1 = input("Ingresa el primer texto en binario: ")
    binary_text2 = input("Ingresa el segundo texto en binario: ")
    result = xor(binary_text1, binary_text2)
    print(f"Resultado del XOR: {result}")


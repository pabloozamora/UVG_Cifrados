def xor(binary_text1, binary_text2):
    num1 = int(binary_text1, 2)
    num2 = int(binary_text2, 2)
    # Realizar operación XOR y convertir resultado a binario
    result = num1 ^ num2
    return bin(result)[2:]  # [2:] elimina el prefijo '0b'

if __name__ == "__main__":
    binary_text1 = input("Ingresa el primer texto en binario: ")
    binary_text2 = input("Ingresa el segundo texto en binario: ")
    result = xor(binary_text1, binary_text2)
    print(f"Resultado del XOR: {result}")


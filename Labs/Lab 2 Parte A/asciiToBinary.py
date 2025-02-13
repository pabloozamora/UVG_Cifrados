def ascii_to_binary(text):
    """
    Convierte un texto en binario representando cada carácter en formato ASCII.

    Args:
        text (str): Texto de entrada que será convertido a binario.

    Returns:
        str: Texto convertido a binario, separado por espacios entre caracteres.
    """
    binary_result = ''
    for char in text:
        ascii_value = ord(char)  # Obtener el valor ASCII del carácter
        binary_value = ""
        while ascii_value > 0:
            binary_value = str(ascii_value % 2) + binary_value
            ascii_value //= 2
        # Asegurar que el binario tenga 8 bits
        binary_value = binary_value.zfill(8)
        binary_result += binary_value
    return binary_result

if __name__ == "__main__":
    print("Conversor de texto ASCII a binario")
    text = input("Ingresa el texto que deseas convertir: ")
    binary_output = ascii_to_binary(text)
    print(f"Texto en binario: {binary_output}")
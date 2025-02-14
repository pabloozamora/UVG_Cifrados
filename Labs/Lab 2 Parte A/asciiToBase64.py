def ascii_to_base64(text):

    base_64_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    """
    Convierte un texto en ASCII a su Base64.

    Args:
        text (str): Texto en formato ASCII que será convertido a Base64.

    Returns:
        str: Texto convertido a ASCII.
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

    base64_result = []

    # Rellenar el binario con ceros si su longitud no es múltiplo de 6
    padding_needed = (6 - len(binary_result) % 6) % 6
    if padding_needed > 0:
        binary_result += '0' * padding_needed

    # Dividir el texto binario en grupos de 6 bits
    for i in range(0, len(binary_result), 6):
        binary_chunk = binary_result[i:i + 6]
        # Convertir cada grupo de 6 bits a su valor decimal
        decimal_value = int(binary_chunk, 2)
        # Mapear el valor decimal al alfabeto Base64
        base64_result.append(base_64_alphabet[decimal_value])

    # Agregar padding de Base64 si es necesario
    base64_result = ''.join(base64_result) + '=' * ((4 - len(base64_result) % 4) % 4)
    return base64_result

if __name__ == "__main__":
    print("Conversor de texto ASCII a Base64")
    text = input("Ingresa el texto que deseas convertir: ")
    base64_output = ascii_to_base64(text)
    print(f"Texto en Base64: {base64_output}")
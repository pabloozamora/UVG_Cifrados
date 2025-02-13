def base64_to_ascii(text):

    base_64_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    """
    Convierte un texto en Base64 a su representación binaria.

    Args:
        text (str): Texto en formato Base64 que será convertido a binario.

    Returns:
        str: Texto convertido a binario, separado por espacios entre caracteres.
    """
    
    binary_result = []

    for char in text:
        if char in base_64_alphabet:
            # Obtener el índice del carácter en el alfabeto Base64
            index = base_64_alphabet.index(char)
            # Convertir el índice a binario manualmente
            binary_value = ""
            while index > 0:
                binary_value = str(index % 2) + binary_value
                index //= 2
            # Asegurarse de que el binario sea de 8 bits
            binary_value = binary_value.zfill(6)
            binary_result.append(binary_value)
        elif char == '=':
            # Padding de Base64
            continue
        else:
            raise ValueError(f"Carácter inválido en Base64: {char}")
        
    binary_text = ''.join(binary_result)

    ascii_result = ''
        
    # Si el texto tiene padding, se elimina la cantidad de ceros que corresponden al padding
    padding_count = text.count('=')
    if padding_count > 0:
        binary_text = binary_text[:-padding_count * 2]

    # Dividir el texto binario en grupos de 8 bits
    for i in range(0, len(binary_text), 8):
        binary_chunk = binary_text[i:i + 8]
        # Convertir cada grupo de 8 bits a su valor decimal
        decimal_value = int(binary_chunk, 2)
        # Convertir el valor decimal a su carácter ASCII
        ascii_result += chr(decimal_value)

    return ascii_result

if __name__ == "__main__":
    base64_text = input("Ingresa el texto en Base64 que deseas convertir: ")
    try:
        ascii_output = base64_to_ascii(base64_text)
        print(f"Texto en ASCII: {ascii_output}")
    except Exception as e:
        print(f"Error: {e}")
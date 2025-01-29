# Prompt realizado a GPT-4o: Escribe un programa en Python que manualmente convierta un texto en Base64 a binario.
def base64_to_binary(text):

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
            # Asegurarse de que el binario sea de 6 bits
            binary_value = binary_value.zfill(6)
            binary_result.append(binary_value)
        elif char == '=':
            # Padding de Base64
            continue
        else:
            raise ValueError(f"Carácter inválido en Base64: {char}")

    return ''.join(binary_result)

if __name__ == "__main__":
    base64_text = input("Ingresa el texto en Base64 que deseas convertir: ")
    try:
        binary_output = base64_to_binary(base64_text)
        print(f"Texto en binario: {binary_output}")
    except Exception as e:
        print(f"Error: {e}")
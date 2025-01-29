# Prompt realizado a GPT-4o: Escribe un programa en Python que manualmente convierta un texto en binario a Base64.
def binary_to_base64(binary_text):
    """
    Convierte un texto en binario a su representación en Base64.

    Args:
        binary_text (str): Texto en binario que será convertido a Base64.

    Returns:
        str: Texto convertido a Base64.
    """
    base_64_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    base64_result = []

    # Rellenar el binario con ceros si su longitud no es múltiplo de 6
    padding_needed = (6 - len(binary_text) % 6) % 6
    if padding_needed > 0:
        binary_text += '0' * padding_needed

    # Dividir el texto binario en grupos de 6 bits
    for i in range(0, len(binary_text), 6):
        binary_chunk = binary_text[i:i + 6]
        # Convertir cada grupo de 6 bits a su valor decimal
        decimal_value = int(binary_chunk, 2)
        # Mapear el valor decimal al alfabeto Base64
        base64_result.append(base_64_alphabet[decimal_value])

    base64_result = ''.join(base64_result) + '=' * int(padding_needed / 2)
    return base64_result

if __name__ == "__main__":
    binary_text = input("Ingresa el texto en binario que deseas convertir (múltiplo de 6 bits): ")
    try:
        base64_output = binary_to_base64(binary_text)
        print(f"Texto en Base64: {base64_output}")
    except Exception as e:
        print(f"Error: {e}")
def clean_text(text):
    cleaned_text = text.lower()
    cleaned_text = cleaned_text.replace(" ", "")
    cleaned_text = cleaned_text.replace('á', 'a')
    cleaned_text = cleaned_text.replace('é', 'e')
    cleaned_text = cleaned_text.replace('í', 'i')
    cleaned_text = cleaned_text.replace('ó', 'o')
    cleaned_text = cleaned_text.replace('ú', 'u')
    cleaned_text = cleaned_text.replace("'", "")
    cleaned_text = cleaned_text.replace(".", "")
    cleaned_text = cleaned_text.replace(",", "")
    cleaned_text = cleaned_text.replace(";", "")
    cleaned_text = cleaned_text.replace(":", "")
    cleaned_text = cleaned_text.replace("!", "")
    cleaned_text = cleaned_text.replace("?", "")
    cleaned_text = cleaned_text.replace("¿", "")
    cleaned_text = cleaned_text.replace("¡", "")
    cleaned_text = cleaned_text.replace("(", "")
    cleaned_text = cleaned_text.replace(")", "")
    cleaned_text = cleaned_text.replace("[", "")
    cleaned_text = cleaned_text.replace("]", "")
    cleaned_text = cleaned_text.replace("{", "")
    cleaned_text = cleaned_text.replace("}", "")
    cleaned_text = cleaned_text.replace("\\", "")
    cleaned_text = cleaned_text.replace("/", "")
    cleaned_text = cleaned_text.replace("*", "")
    cleaned_text = cleaned_text.replace("^", "")
    cleaned_text = cleaned_text.replace("+", "")
    cleaned_text = cleaned_text.replace("-", "")
    cleaned_text = cleaned_text.replace("_", "")
    cleaned_text = cleaned_text.replace("=", "")
    cleaned_text = cleaned_text.replace("|", "")
    cleaned_text = cleaned_text.replace(":", "")
    cleaned_text = cleaned_text.replace(";", "")
    cleaned_text = cleaned_text.replace("'", "")
    cleaned_text = cleaned_text.replace('\n', "")
    return cleaned_text

def frequency_analysis(text):
    # Limpiar el texto
    text = clean_text(text)

    # Crear un diccionario para almacenar la frecuencia de cada caracter
    frequency = {}
    # Iterar sobre cada caracter en el texto
    for char in text:
        # si el caracter ya está en el diccionario, incrementar su frecuencia
        if char in frequency:
            frequency[char] += 1
        # Si el caracter no está en el diccionario, inicializar su frecuencia en 1
        else:
            frequency[char] = 1

    # Dividir la frecuencia de cada caracter por el total de caracteres en el texto
    total_chars = len(text)
    for char in frequency:
        frequency[char] /= total_chars

    # Ordenar el diccionario en orden alfabético
    frequency = dict(sorted(frequency.items()))

    return frequency

# Prompt realizado a GPT-4o: ¿Cuál es la mejor métrica que podría usar para comparar dos distribuciones de frecuencias?
def chi_squared_score(decrypted_text):
    '''Calcula el puntaje Chi-cuadrado de un texto en comparación a las frecuencias teóricas del español.'''

    # Obtener las frecuencias del texto
    frequencies = frequency_analysis(decrypted_text)

    # Frecuencias teóricas del español
    theoretical_frequencies = {
        "a": 0.11525,
        "b": 0.02215,
        "c": 0.04019,
        "d": 0.05010,
        "e": 0.12181,
        "f": 0.00692,
        "g": 0.01768,
        "h": 0.00703,
        "i": 0.06247,
        "j": 0.00493,
        "k": 0.00011,
        "l": 0.04967,
        "m": 0.03157,
        "n": 0.06712,
        "o": 0.08683,
        "p": 0.02510,
        "q": 0.00877,
        "r": 0.06871,
        "s": 0.07977,
        "t": 0.04632,
        "u": 0.02927,
        "v": 0.01138,
        "w": 0.00017,
        "x": 0.00215,
        "y": 0.01008,
        "z": 0.00467,
        "á": 0.00502,
        "é": 0.00433,
        "í": 0.00725,
        "ñ": 0.00311,
        "ó": 0.00827,
        "ú": 0.00168,
        "ü": 0.00012
    }

    chi_square = 0
    for char in theoretical_frequencies:
        observed = frequencies.get(char, 0)
        expected = theoretical_frequencies[char]
        if expected > 0:
            chi_square += ((observed - expected) ** 2) / expected
    return chi_square


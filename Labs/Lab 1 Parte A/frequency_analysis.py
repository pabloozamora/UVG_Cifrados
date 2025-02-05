import matplotlib.pyplot as plt
from clean_text import clean_text
import numpy as np

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

# Prompt realizado a GPT-4o: Realiza una función que permita graficar las frecuencias de los
# caracteres en un texto en comparación a estas frecuencias teóricas.
def plot_frequencies(frequency):
    theoretical_frequencies = {
        "a": 12.53, "b": 1.42, "c": 4.68, "d": 5.86, "e": 13.68, "f": 0.69, "g": 1.01, "h": 0.70, "i": 6.25,
        "j": 0.44, "k": 0.02, "l": 4.97, "m": 3.15, "n": 6.71, "ñ": 0.31, "o": 8.68, "p": 2.51, "q": 0.88,
        "r": 6.87, "s": 7.98, "t": 4.63, "u": 3.93, "v": 0.90, "w": 0.01, "x": 0.22, "y": 0.90, "z": 0.52, "ñ": 0
    }

    # Asegurar que ambas distribuciones tengan las mismas claves en el mismo orden
    all_letters = sorted(theoretical_frequencies.keys())  # Orden alfabético

    # Obtener valores en el orden correcto (si una letra no está en frequency, se asume 0)
    theoretical_values = [theoretical_frequencies[letter]/100 for letter in all_letters]
    empirical_values = [frequency.get(letter, 0) for letter in all_letters]

    # Crear un gráfico de barras con separación
    x = np.arange(len(all_letters))  # Posiciones en el eje X

    plt.figure(figsize=(12, 6))
    plt.bar(x - 0.2, theoretical_values, width=0.4, alpha=0.6, label='Frecuencias teóricas', color='blue')
    plt.bar(x + 0.2, empirical_values, width=0.4, alpha=0.6, label='Frecuencias reales', color='orange')

    plt.xticks(x, all_letters) 
    plt.xlabel('Caracteres')
    plt.ylabel('Frecuencia')
    plt.title('Frecuencia de caracteres en el texto')
    plt.legend()
    plt.show()
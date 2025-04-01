# Laboratorio 3
Universidad del Valle de Guatemala
Cifrado de Información<br>
Pablo Andrés Zamora Vásquez<br>
Carné 21780<br>

## 📜 Descripción
En este laboratorio se realizó lo siguiente:
- Comparación entre los modos EBC y CBC de AES mediante el cifrado de imágenes.
- Captura del envío de mensajes y archivos sin cifrar y cifrados con AES-CBC entre dos máquinas.
- Implementación de un cifrado de flujo con ChaCha20 y comparación de su rendimiento respecto a AES.
- Simulación de un ransomware mediante el encriptado AES de los archivos que se encuentran en un directorio y sus subdirectorios.

## 📦 Dependencias
- pycriptodome
- matplotlib
- Pillow
- numpy

## 🔐 Uso
Se utilizan las funciones que se encuentran en los módulos *AESFunctions.py* y *ChaCha20Functions.py* para el cifrado de información. Es importante mencionar que cada función AES utiliza un modo distinto.
Por otro lado, a las funciones AES se les debe proporcionar un parámetro para el vector de inicialización (IV), mientras que a las funciones ChaCha20 se les debe proporcionar un parámetro para el nonce.




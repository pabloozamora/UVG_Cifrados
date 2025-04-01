# Ejercicio Block Cipher
Universidad del Valle de Guatemala
Cifrado de Información<br>
Pablo Andrés Zamora Vásquez<br>
Carné 21780<br>

## 📜 Descripción
En este ejercicio se implementan funciones de cifrado y descifrado DES, 3DES y AES (en modo ECB Y CBC). Las funciones DES y 3DES se utilizan para cifrar y descifrar texto plano, mientras que las funciones AES se utilizan sobre la misma imagen para comparar el funcionamiento
de los distintos modos.

## 📦 Dependencias
- pycryptodome
- matplotlib
- Pillow
- numpy

## 🔐 Uso
Se utilizan las funciones *encrypt* y *decrypt* del módulo respondiente a cada algoritmo para cifrar y descifrar texto plano (tomando en cuenta que, para AES, dichas funciones dependen también del modo). Cabe mencionar que a las funciones AES se les debe proporcionar un parámetro para
el vector de inicialización (IV).





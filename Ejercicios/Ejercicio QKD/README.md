# Ejercicio QKD - Protocolo BB84  
Universidad del Valle de Guatemala  
Cifrado de Información  
Pablo Andrés Zamora Vásquez
Carné 21780  

## 📜 Descripción  
Este ejercicio simula una ronda del protocolo de distribución cuántica de claves (QKD) BB84, en la cual Alice y Bob intentan compartir una clave secreta utilizando fotones con polarización y bases aleatorias.  
El objetivo es observar cómo se forma una clave segura únicamente cuando las bases de medición coinciden, y analizar cómo la intervención de un espía (Eve) puede introducir errores detectables.

## 📊 Funcionamiento  
- Alice genera una secuencia de bits y bases de manera aleatoria.
- Cada bit se codifica como un fotón con una polarización correspondiente.
- Bob, sin conocer las bases de Alice, mide cada fotón usando sus propias bases aleatorias.
- Luego, se comparan públicamente las bases que utilizaron, y se quedan únicamente los bits donde coincidieron.
- Finalmente, se analizan los resultados para obtener la clave segura y discutir la seguridad del canal.

## 📦 Dependencias  
No se requieren dependencias externas.  
La simulación fue implementada en Python y utiliza únicamente la librería estándar `random` y `pandas` para visualización.

## 🔐 Uso  
El script genera automáticamente una tabla con 15 rondas de transmisión entre Alice y Bob, indicando:
- Bit de Alice
- Base de Alice
- Fotón enviado
- Base de Bob
- Bit recibido
- Si las bases coinciden
- Si el bit se incluye en la clave

También se incluyen preguntas de análisis al final para reforzar la comprensión del protocolo.

## 📌 Observaciones  
- La asignación de bits a polarizaciones sigue la convención de los artículos de referencia, donde 0 = horizontal (0°) y 1 = vertical (90°) en la base recta.


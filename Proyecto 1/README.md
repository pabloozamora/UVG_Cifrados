# 🔐 Proyecto 1 - CTF Stream Cipher
Pablo Andrés Zamora Vásquez<br>
Carné 21780<br>
Curso: Cifrado de Información<br>
Sección: 10<br>

Este repositorio contiene los scripts utilizados para resolver una serie de retos prácticos sobre **cifrados de flujo**, presentados en el curso *Cifrado de Información* (CC3078). Cada reto explora vulnerabilidades reales en implementaciones comunes de cifrados como XOR, RC4, PRNG personalizados y ChaCha20.

---

## ⚔️ Retos

### 1. **Luffy Challenge - XOR básico**
Cifra basado en la operación XOR entre texto plano y una clave de texto.

- 🔑 Vulnerabilidad: clave predecible y sin protección adicional.
- 📄 Script: `xor_luffy.py`
- 🧪 Solución: se hace XOR del ciphertext con `"21780"`.

### 2. **Zoro Challenge - RC4**
RC4 sin vector de inicialización ni nonce.

- 🔑 Vulnerabilidad: RC4 reutiliza keystream si se repite la clave.
- 📄 Script: `rc4_zoro.py`
- 🧪 Solución: descifrado directo con `key = b"21780"`.

### 3. **Usopp Challenge - PRNG débil**
Cifrado personalizado usando `random.seed()` para generar keystream.

- 🔑 Vulnerabilidad: PRNG no criptográfico y semilla numérica predecible.
- 📄 Script: `stream_cipher_custom_usopp.py`
- 🧪 Solución: fuerza bruta sobre semillas `0–99999` buscando `FLAG_`.

### 4. **Nami Challenge - ChaCha20 mal implementado**
ChaCha20 con clave y nonce derivados del mismo valor (`user_id`).

- 🔑 Vulnerabilidad: uso determinístico del nonce → keystreams repetibles.
- 📄 Script: `chacha20_nami.py`
- 🧪 Solución: prueba de posibles claves/IDs (`"21780"`, `"nami"`, etc).

---

## ⚙ Requisitos
- Python 3
- pycryptodome

```bash
pip install pycryptodome
```

## ▶️ Ejecución

Puedes ejecutar cada script individualmente.

## 🏁 Flags obtenidas
El archivo flags.txt contiene las banderas descifradas y el archivo poneglyph.txt contiene los fragmentos de texto encontrados en las imágenes correspondientes de los retos.

## 📚 Referencias

Sumartono, I., Siahaan, A. P. U., & Mayasari, N. (2016). An overview of the RC4 algorithm. DOI:10.9790/0661-1806046773
Rana, M., Mamun, Q., & Islam, R. (2021). Lightweight cryptography in IoT networks: A survey. DOI:10.1016/j.future.2021.05.011


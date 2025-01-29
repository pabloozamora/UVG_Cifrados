import random

def generate_dynamic_key(quantity):
    key = ''
    for i in range(quantity):
        key += chr(random.randint(0, 255))
    return key

quantity = 10
key = generate_dynamic_key(quantity)
print(f"Llave dinámica: {key}")
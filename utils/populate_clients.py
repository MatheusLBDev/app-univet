import requests
import random

API_URL = "https://app-univet.onrender.com/clients"

first_names = [
    "Ana", "Carlos", "Mariana", "João", "Fernanda", "Ricardo", "Beatriz",
    "Paulo", "Larissa", "Gabriel", "Renata", "Thiago", "Letícia", "Eduardo"
]

last_names = [
    "Silva", "Souza", "Oliveira", "Pereira", "Almeida", "Costa", "Lima",
    "Gomes", "Ribeiro", "Martins", "Barros", "Teixeira", "Moreira", "Melo"
]

streets = [
    "Rua das Flores", "Avenida Brasil", "Rua Primavera", "Rua das Acácias",
    "Alameda dos Pinheiros", "Rua São João", "Avenida Paulista",
    "Travessa Azul", "Rua Central", "Rua do Comércio"
]

domains = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com"]

def generate_phone():
    return f"(11) 9{random.randint(1000,9999)}-{random.randint(1000,9999)}"

def generate_email(name):
    return f"{name.lower().replace(' ','.')}{random.randint(1,99)}@{random.choice(domains)}"

def generate_address():
    street = random.choice(streets)
    number = random.randint(10,500)
    return f"{street}, {number}"

def create_client():
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    return {
        "name": name,
        "phone": generate_phone(),
        "email": generate_email(name),
        "address": generate_address()
    }

# Total de clientes para gerar
for _ in range(30):
    client = create_client()
    response = requests.post(API_URL, json=client)
    
    if response.status_code in (200, 201):
        print(f"[OK] Cliente criado: {client['name']}")
    else:
        print(f"[ERRO] {response.status_code} — {response.text}")
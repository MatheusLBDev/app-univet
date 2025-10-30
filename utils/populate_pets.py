import requests
import random
from datetime import datetime, timedelta

# URL da API para criar pets
API_URL = "https://app-univet.onrender.com/pets"

# Lista de clientes (com ID)
clients = [
    {"id": 1, "name": "Beatriz Almeida"},
    {"id": 2, "name": "Fernanda Almeida"},
    {"id": 3, "name": "Thiago Martins"},
    {"id": 4, "name": "Thiago Oliveira"},
    {"id": 5, "name": "Beatriz Melo"},
    {"id": 6, "name": "Fernanda Teixeira"},
    {"id": 7, "name": "Ricardo Melo"},
    {"id": 8, "name": "Renata Ribeiro"},
    {"id": 9, "name": "Letícia Barros"},
    {"id": 10, "name": "Beatriz Pereira"},
    {"id": 11, "name": "Paulo Costa"},
    {"id": 12, "name": "Fernanda Lima"},
    {"id": 13, "name": "Ricardo Gomes"},
    {"id": 14, "name": "Eduardo Melo"},
    {"id": 15, "name": "Carlos Ribeiro"},
    {"id": 16, "name": "Mariana Moreira"},
    {"id": 17, "name": "Gabriel Almeida"},
    {"id": 18, "name": "Ana Teixeira"},
    {"id": 19, "name": "Beatriz Lima"},
    {"id": 20, "name": "Gabriel Teixeira"},
    {"id": 21, "name": "Gabriel Pereira"},
    {"id": 22, "name": "Mariana Moreira"},
    {"id": 23, "name": "Ana Oliveira"},
    {"id": 24, "name": "Fernanda Almeida"},
    {"id": 25, "name": "Thiago Oliveira"},
    {"id": 26, "name": "Larissa Costa"},
    {"id": 27, "name": "Renata Melo"},
    {"id": 28, "name": "Letícia Teixeira"},
    {"id": 29, "name": "Letícia Pereira"},
    {"id": 30, "name": "Mariana Martins"},
]

species_breeds = {
    "cachorro": ["Labrador", "Poodle", "Bulldog", "Golden Retriever", "Shih Tzu", "Lulu da Pomerânea", "Beagle"],
    "gato": ["Siamês", "Persa", "Maine Coon", "Sphynx", "Balinês", "Angorá"],
    "roedor": ["Hamster", "Porquinho-da-índia", "Gerbil", "Rato"],
    "pássaro": ["Calopsita", "Canário", "Periquito", "Papagaio"],
    "outro": ["Coelho", "Tartaruga", "Iguana", "Peixe"]
}

pet_names = [
    "Luna", "Thor", "Bella", "Simba", "Nina", "Max", "Milo", "Loki", "Chico", "Cacau",
    "Mel", "Bidu", "Toby", "Zeca", "Pipoca", "Fiona", "Bob", "Tina", "Spike", "Lucky"
]

def random_birthdate(min_age=1, max_age=15):
    """Gera uma data de nascimento aleatória"""
    today = datetime.today()
    age = random.randint(min_age, max_age)
    birth_date = today - timedelta(days=age*365 + random.randint(0, 364))
    return birth_date.strftime("%Y-%m-%d")

def generate_pet(owner_id):
    """Gera um pet aleatório consistente"""
    species = random.choice(list(species_breeds.keys()))
    breed = random.choice(species_breeds[species])
    name = random.choice(pet_names)
    birthDate = random_birthdate()
    return {
        "name": name,
        "species": species,
        "breed": breed,
        "birthDate": birthDate,
        "ownerId": owner_id
    }

# Criar pets para cada cliente (máx 2 por cliente)
for client in clients:
    num_pets = random.randint(1, 2)
    for _ in range(num_pets):
        pet = generate_pet(client["id"])
        response = requests.post(API_URL, json=pet)
        if response.status_code in (200, 201):
            print(f"[OK] Pet criado para {client['name']}: {pet['name']} ({pet['species']} - {pet['breed']})")
        else:
            print(f"[ERRO] {response.status_code} - {response.text}")
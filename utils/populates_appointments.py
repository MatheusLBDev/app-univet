import requests
import random
from datetime import datetime, timedelta

# URL da API para criar agendamentos
API_URL = "https://app-univet.onrender.com/appointments"

# Lista completa de pets
pets = [
    {"id": 1, "ownerId": 1, "name": "Simba", "species": "gato"},
    {"id": 2, "ownerId": 2, "name": "Fiona", "species": "pássaro"},
    {"id": 3, "ownerId": 2, "name": "Max", "species": "outro"},
    {"id": 4, "ownerId": 3, "name": "Zeca", "species": "gato"},
    {"id": 5, "ownerId": 4, "name": "Chico", "species": "roedor"},
    {"id": 6, "ownerId": 4, "name": "Bella", "species": "cachorro"},
    {"id": 7, "ownerId": 5, "name": "Luna", "species": "outro"},
    {"id": 8, "ownerId": 5, "name": "Zeca", "species": "roedor"},
    {"id": 9, "ownerId": 6, "name": "Nina", "species": "gato"},
    {"id": 10, "ownerId": 7, "name": "Pipoca", "species": "cachorro"},
    {"id": 11, "ownerId": 7, "name": "Bob", "species": "outro"},
    {"id": 12, "ownerId": 8, "name": "Tina", "species": "gato"},
    {"id": 13, "ownerId": 8, "name": "Bob", "species": "cachorro"},
    {"id": 14, "ownerId": 9, "name": "Max", "species": "pássaro"},
    {"id": 15, "ownerId": 9, "name": "Nina", "species": "pássaro"},
    {"id": 16, "ownerId": 10, "name": "Bidu", "species": "outro"},
    {"id": 17, "ownerId": 10, "name": "Nina", "species": "outro"},
    {"id": 18, "ownerId": 11, "name": "Bidu", "species": "outro"},
    {"id": 19, "ownerId": 12, "name": "Mel", "species": "gato"},
    {"id": 20, "ownerId": 12, "name": "Chico", "species": "roedor"},
    {"id": 21, "ownerId": 13, "name": "Cacau", "species": "outro"},
    {"id": 22, "ownerId": 14, "name": "Bella", "species": "gato"},
    {"id": 23, "ownerId": 15, "name": "Tina", "species": "outro"},
    {"id": 24, "ownerId": 15, "name": "Max", "species": "outro"},
    {"id": 25, "ownerId": 16, "name": "Max", "species": "cachorro"},
    {"id": 26, "ownerId": 17, "name": "Toby", "species": "roedor"},
    {"id": 27, "ownerId": 18, "name": "Simba", "species": "pássaro"},
    {"id": 28, "ownerId": 19, "name": "Bidu", "species": "roedor"},
    {"id": 29, "ownerId": 19, "name": "Zeca", "species": "cachorro"},
    {"id": 30, "ownerId": 20, "name": "Milo", "species": "cachorro"},
    {"id": 31, "ownerId": 20, "name": "Cacau", "species": "pássaro"},
    {"id": 32, "ownerId": 21, "name": "Simba", "species": "gato"},
    {"id": 33, "ownerId": 22, "name": "Fiona", "species": "cachorro"},
    {"id": 34, "ownerId": 22, "name": "Nina", "species": "cachorro"},
    {"id": 35, "ownerId": 23, "name": "Loki", "species": "gato"},
    {"id": 36, "ownerId": 24, "name": "Luna", "species": "outro"},
    {"id": 37, "ownerId": 24, "name": "Milo", "species": "roedor"},
    {"id": 38, "ownerId": 25, "name": "Chico", "species": "gato"},
    {"id": 39, "ownerId": 26, "name": "Luna", "species": "gato"},
    {"id": 40, "ownerId": 26, "name": "Mel", "species": "outro"},
    {"id": 41, "ownerId": 27, "name": "Toby", "species": "pássaro"},
    {"id": 42, "ownerId": 28, "name": "Lucky", "species": "pássaro"},
    {"id": 43, "ownerId": 28, "name": "Lucky", "species": "cachorro"},
    {"id": 44, "ownerId": 29, "name": "Fiona", "species": "cachorro"},
    {"id": 45, "ownerId": 30, "name": "Pipoca", "species": "gato"},
]

reasons = [
    "Consulta de rotina", "Vacinação", "Emergência", "Retorno", "Exame", "Tosa", "Banho", "Check-up completo"
]

notes = [
    "Cliente solicitou atendimento urgente",
    "Pet apresenta sintomas de tosse",
    "Verificar vacinação anual",
    "Necessário exame de sangue",
    "Consulta agendada para avaliação de peso",
    "Solicitado banho e tosa"
]

def random_date(start_days_ago=180, end_days_future=30):
    """Gera uma data aleatória nos últimos 6 meses até 30 dias no futuro"""
    today = datetime.today()
    start_date = today - timedelta(days=start_days_ago)
    end_date = today + timedelta(days=end_days_future)
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date

# Criar agendamentos para cada pet
for pet in pets:
    num_appointments = random.randint(1, 3)  # até 3 agendamentos por pet
    for _ in range(num_appointments):
        date = random_date()
        status = "Agendado" if date >= datetime.now() else random.choice(["Concluído", "Cancelado"])
        appointment = {
            "clientId": pet["ownerId"],
            "petId": pet["id"],
            "date": date.strftime("%Y-%m-%d %H:%M:%S"),
            "reason": random.choice(reasons),
            "notes": random.choice(notes),
            "status": status
        }
        response = requests.post(API_URL, json=appointment)
        if response.status_code in (200, 201):
            print(f"[OK] Agendamento criado para {pet['name']} ({pet['species']}), Status: {status}")
        else:
            print(f"[ERRO] {response.status_code} - {response.text}")
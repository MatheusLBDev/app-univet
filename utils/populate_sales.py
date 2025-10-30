import requests
import random
from datetime import datetime, timedelta

API_URL = "https://app-univet.onrender.com/inventory/sales"  # Altere se for local
NUM_SALES = 120  # Número de vendas para simular (média 20/mês)

# Lista de produtos e serviços com IDs e preços
products = [
    {"id": 1, "price": 169.90},
    {"id": 2, "price": 119.50},
    {"id": 3, "price": 22.90},
    {"id": 4, "price": 89.99},
    {"id": 5, "price": 34.90},
    {"id": 6, "price": 25.00},
    {"id": 7, "price": 27.80},
    {"id": 8, "price": 55.00},
    {"id": 9, "price": 45.00},
    {"id": 10, "price": 75.00},
]

services = [
    {"id": 1, "price": 120},
    {"id": 2, "price": 200},
    {"id": 3, "price": 90},
    {"id": 4, "price": 70},
    {"id": 5, "price": 85},
    {"id": 6, "price": 50},
    {"id": 7, "price": 140},
    {"id": 8, "price": 75},
    {"id": 9, "price": 250},
    {"id": 10, "price": 100},
]

def random_item():
    """Escolhe aleatoriamente um produto ou serviço"""
    if random.choice([True, False]):
        item = random.choice(products)
        return {"product_id": item["id"], "service_id": None, "quantity": random.randint(1, 3), "price": item["price"]}
    else:
        item = random.choice(services)
        return {"product_id": None, "service_id": item["id"], "quantity": 1, "price": item["price"]}

def generate_sale(date):
    """Gera uma venda com itens e data"""
    items = [random_item() for _ in range(random.randint(1, 3))]
    total = sum(i["price"] * i["quantity"] for i in items)
    return {
        "total": total,
        "date": date.strftime("%Y-%m-%d"),
        "items": items
    }

# Criar vendas distribuídas pelos últimos 6 meses (180 dias)
for i in range(NUM_SALES):
    date = datetime.now() - timedelta(days=random.randint(1, 180))
    sale_data = generate_sale(date)
    response = requests.post(API_URL, json=sale_data)

    if response.status_code in (200, 201):
        print(f"[OK] Venda criada — {sale_data['date']} — Total: R${sale_data['total']:.2f}")
    else:
        print(f"[ERRO] {response.status_code} — {response.text}")
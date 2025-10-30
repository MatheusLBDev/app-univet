import requests
import random

API_URL = "https://app-univet.onrender.com/inventory/products"  # altere se necessário

# Lista de produtos fictícios
products = [
    {"name": "Ração Premium para Cães 10kg", "description": "Ração de alta qualidade para cães adultos", "price": 169.90, "stock": 40},
    {"name": "Ração para Gatos 7kg", "description": "Ração completa para gatos castrados", "price": 119.50, "stock": 50},
    {"name": "Petiscos para Cães", "description": "Biscoitos saudáveis para cães filhotes e adultos", "price": 22.90, "stock": 120},
    {"name": "Coleira Antipulgas", "description": "Coleira contra pulgas e carrapatos para cães", "price": 89.99, "stock": 15},
    {"name": "Shampoo Pet Neutro", "description": "Shampoo dermatológico neutro para pets", "price": 34.90, "stock": 30},
    {"name": "Brinquedo Mordedor", "description": "Brinquedo resistente para cães de porte médio", "price": 25.00, "stock": 60},
    {"name": "Areia Higiênica 4kg", "description": "Areia granulada para gatos", "price": 27.80, "stock": 75},
    {"name": "Antiparasitário Oral", "description": "Tratamento oral para vermes e parasitas", "price": 55.00, "stock": 25},
    {"name": "Comedouro Duplo Pet", "description": "Comedouro e bebedouro duplo antiderrapante", "price": 45.00, "stock": 40},
    {"name": "Suplemento Vitamínico", "description": "Vitaminas essenciais para cães idosos", "price": 75.00, "stock": 20},
]

for product in products:
    response = requests.post(API_URL, json=product)

    if response.status_code == 200 or response.status_code == 201:
        print(f"✅ Produto criado: {product['name']}")
    else:
        print(f"❌ Erro ao criar {product['name']} - Status: {response.status_code} | {response.text}")
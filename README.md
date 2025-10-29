# Gestão de Clínica Veterinária - Univet

Este projeto é um sistema de gestão para clínicas veterinárias, permitindo o gerenciamento de consultas, clientes, pets e inventário, incluindo previsão de estoque e vendas utilizando um modelo estatístico baseado na biblioteca **Statsmodels**.

---

## 🧰 Pré-requisitos

Antes de começar, você precisará ter as seguintes ferramentas instaladas em sua máquina:

- [Python](https://www.python.org/downloads/) (versão 3.8 ou superior)  
- [Pip](https://pip.pypa.io/en/stable/installation/) (gerenciador de pacotes do Python)  

---

## 🗂️ Estrutura do Projeto

```
.
backend-univet/                  # Pasta raiz do backend
├── routers/                     # Rotas da API
│   ├── __init__.py
│   ├── appointments.py
│   ├── clients_pets.py
│   ├── dashboard.py
│   ├── forecast.py
│   └── inventory.py
├── __init__.py                  # Inicialização do pacote backend
├── crud.py                      # Operações CRUD
├── database.py                  # Configuração do banco de dados e engine SQLAlchemy
├── main.py                      # Inicialização do servidor FastAPI
├── models.py                    # Modelos de banco de dados
├── requirements.txt             # Dependências Python (FastAPI, SQLAlchemy, Pandas, Statsmodels, etc.)
├── schemas.py                   # Schemas de dados
├── Pipfile                      # Gerenciador de dependências Python
└── Pipfile.lock                 # Lock das dependências
.gitignore                       # Arquivos e pastas ignoradas pelo Git
```

---

## 🚀 Como Executar o Projeto

### 1. Backend (API)

O backend é responsável por toda a lógica de negócio, comunicação com o banco de dados e previsão de estoque/vendas.

```bash
# Navegue até o diretório do backend
cd backend

# Crie e ative um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate

# Instale as dependências do Python
pip install -r requirements.txt

# Inicie o servidor da API
uvicorn main:app --reload
```

O servidor estará em execução em:  
👉 `http://127.0.0.1:8000`

---

## 🧠 Previsão de Estoque e Vendas (IA)

O sistema utiliza **Statsmodels** para gerar previsões de demanda e sugerir reposição de estoque de forma automática.

- O modelo analisa o histórico de vendas armazenado no banco de dados.  
- Gera previsões de vendas futuras com base em séries temporais.  
- Sugere níveis ideais de reposição de produtos.  

O endpoint de previsão está implementado em `backend/routers/forecast.py`

## 🧩 Tecnologias Utilizadas

### Backend
- fastapi
- uvicorn
- sqlalchemy
- pydantic
- python-multipart
- pandas
- statsmodels
- psycopg2-binary
- python-dotenv

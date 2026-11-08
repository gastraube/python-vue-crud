# Produtos CRUD — FastAPI + Vue

CRUD simples de produtos (nome, preço e quantidade), com uma API em Python/FastAPI e um front-end em Vue 3 + Vuetify.

- **api/** — FastAPI organizada em camadas (routers → services → repositories). Os dados ficam em memória, então são resetados a cada reinício.
- **front/** — Vue 3 + TypeScript + Vite, com Vuetify (UI), Pinia (estado), Vue Router e axios.

## Pré-requisitos

- Python 3.10+
- Node.js 22.18+ ou 24.12+

## Rodando a API

```bash
cd api
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/macOS
pip install -r requirements.txt
fastapi dev app/main.py
```

A API sobe em http://127.0.0.1:8000 e a documentação interativa (Swagger) fica em http://127.0.0.1:8000/docs.

### Endpoints

| Método | Rota             | Descrição          |
|--------|------------------|--------------------|
| GET    | `/produtos`      | Lista os produtos  |
| GET    | `/produtos/{id}` | Busca um produto   |
| POST   | `/produtos`      | Cria um produto    |
| PUT    | `/produtos/{id}` | Atualiza um produto|
| DELETE | `/produtos/{id}` | Remove um produto  |

## Rodando o front

Em outro terminal:

```bash
cd front
npm install
npm run dev
```

O front abre em http://localhost:5173. A URL da API é configurada em `front/.env` (`VITE_API_URL`).

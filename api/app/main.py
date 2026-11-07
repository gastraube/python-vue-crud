from fastapi import FastAPI

from app.routers import produtos

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Produtos API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(produtos.router)
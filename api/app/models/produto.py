from dataclasses import dataclass


@dataclass
class Produto:
    id: int
    nome: str
    preco: float
    quantidade: int
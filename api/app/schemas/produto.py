from pydantic import BaseModel, Field


class ProdutoRequest(BaseModel):
    nome: str = Field(min_length=3, max_length=100)
    preco: float = Field(gt=0)
    quantidade: int = Field(ge=0)


class ProdutoResponse(ProdutoRequest):
    id: int
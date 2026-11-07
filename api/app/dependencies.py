from typing import Annotated

from fastapi import Depends

from app.repositories.produto_repository import ProdutoRepository
from app.services.produto_service import ProdutoService

_produto_repository = ProdutoRepository()


def get_produto_repository() -> ProdutoRepository:
    return _produto_repository


def get_produto_service(
    repository: Annotated[ProdutoRepository, Depends(get_produto_repository)],
) -> ProdutoService:
    return ProdutoService(repository)


ProdutoServiceDep = Annotated[ProdutoService, Depends(get_produto_service)]
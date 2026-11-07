from dataclasses import asdict

from app.models.produto import Produto
from app.repositories.produto_repository import ProdutoRepository
from app.schemas.produto import ProdutoRequest, ProdutoResponse


class ProdutoService:
    def __init__(self, repository: ProdutoRepository) -> None:
        self._repository = repository

    def listar(self) -> list[ProdutoResponse]:
        return [self._para_response(p) for p in self._repository.listar()]

    def obter_por_id(self, produto_id: int) -> ProdutoResponse | None:
        produto = self._repository.obter_por_id(produto_id)
        return self._para_response(produto) if produto is not None else None

    def criar(self, dados: ProdutoRequest) -> ProdutoResponse:
        produto = Produto(id=0, **dados.model_dump())
        return self._para_response(self._repository.criar(produto))

    def atualizar(self, produto_id: int, dados: ProdutoRequest) -> ProdutoResponse | None:
        if self._repository.obter_por_id(produto_id) is None:
            return None
        produto = Produto(id=produto_id, **dados.model_dump())
        self._repository.atualizar(produto)
        return self._para_response(produto)

    def remover(self, produto_id: int) -> bool:
        if self._repository.obter_por_id(produto_id) is None:
            return False
        self._repository.remover(produto_id)
        return True

    @staticmethod
    def _para_response(produto: Produto) -> ProdutoResponse:
        return ProdutoResponse(**asdict(produto))
from fastapi import APIRouter, HTTPException, status

from app.dependencies import ProdutoServiceDep
from app.schemas.produto import ProdutoRequest, ProdutoResponse

router = APIRouter(prefix="/produtos", tags=["Produtos"])


@router.get("")
def listar(service: ProdutoServiceDep) -> list[ProdutoResponse]:
    return service.listar()


@router.get("/{produto_id}")
def obter_por_id(produto_id: int, service: ProdutoServiceDep) -> ProdutoResponse:
    produto = service.obter_por_id(produto_id)
    if produto is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    return produto


@router.post("", status_code=status.HTTP_201_CREATED)
def criar(dados: ProdutoRequest, service: ProdutoServiceDep) -> ProdutoResponse:
    return service.criar(dados)


@router.put("/{produto_id}")
def atualizar(produto_id: int, dados: ProdutoRequest, service: ProdutoServiceDep) -> ProdutoResponse:
    produto = service.atualizar(produto_id, dados)
    if produto is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    return produto


@router.delete("/{produto_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover(produto_id: int, service: ProdutoServiceDep) -> None:
    if not service.remover(produto_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
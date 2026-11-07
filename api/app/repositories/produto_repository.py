from app.models.produto import Produto


class ProdutoRepository:
    def __init__(self) -> None:
        self._produtos: list[Produto] = [
            Produto(id=1, nome="Teclado", preco=250.0, quantidade=10),
            Produto(id=2, nome="Mouse", preco=120.0, quantidade=25),
            Produto(id=3, nome="Monitor", preco=1500.0, quantidade=5),
        ]
        self._proximo_id = 4

    def listar(self) -> list[Produto]:
        return list(self._produtos)

    def obter_por_id(self, produto_id: int) -> Produto | None:
        return next((p for p in self._produtos if p.id == produto_id), None)

    def criar(self, produto: Produto) -> Produto:
        produto.id = self._proximo_id
        self._proximo_id += 1
        self._produtos.append(produto)
        return produto

    def atualizar(self, produto: Produto) -> None:
        for indice, atual in enumerate(self._produtos):
            if atual.id == produto.id:
                self._produtos[indice] = produto
                return

    def remover(self, produto_id: int) -> None:
        self._produtos = [p for p in self._produtos if p.id != produto_id]
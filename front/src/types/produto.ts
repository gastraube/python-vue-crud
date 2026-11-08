export interface Produto {
  id: number
  nome: string
  preco: number
  quantidade: number
}

export type ProdutoRequest = Omit<Produto, 'id'>
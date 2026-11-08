import type { Produto, ProdutoRequest } from '@/types/produto'
import { http } from './http'

export const produtoService = {
  async listar(): Promise<Produto[]> {
    const { data } = await http.get<Produto[]>('/produtos')
    return data
  },

  async obterPorId(id: number): Promise<Produto> {
    const { data } = await http.get<Produto>(`/produtos/${id}`)
    return data
  },

  async criar(produto: ProdutoRequest): Promise<Produto> {
    const { data } = await http.post<Produto>('/produtos', produto)
    return data
  },

  async atualizar(id: number, produto: ProdutoRequest): Promise<Produto> {
    const { data } = await http.put<Produto>(`/produtos/${id}`, produto)
    return data
  },

  async remover(id: number): Promise<void> {
    await http.delete(`/produtos/${id}`)
  },
}
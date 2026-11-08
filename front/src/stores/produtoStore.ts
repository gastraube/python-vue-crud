import { computed, ref } from 'vue'
import { defineStore } from 'pinia'
import type { Produto, ProdutoRequest } from '@/types/produto'
import { produtoService } from '@/services/produtoService'

export const useProdutoStore = defineStore('produto', () => {
  const produtos = ref<Produto[]>([])
  const carregando = ref(false)

  const total = computed(() => produtos.value.length)

  async function carregar() {
    carregando.value = true
    try {
      produtos.value = await produtoService.listar()
    } finally {
      carregando.value = false
    }
  }

  async function criar(dados: ProdutoRequest) {
    const novo = await produtoService.criar(dados)
    produtos.value.push(novo)
  }

  async function atualizar(id: number, dados: ProdutoRequest) {
    const atualizado = await produtoService.atualizar(id, dados)
    const indice = produtos.value.findIndex((p) => p.id === id)
    if (indice !== -1) produtos.value[indice] = atualizado
  }

  async function remover(id: number) {
    await produtoService.remover(id)
    produtos.value = produtos.value.filter((p) => p.id !== id)
  }

  return { produtos, carregando, total, carregar, criar, atualizar, remover }
})
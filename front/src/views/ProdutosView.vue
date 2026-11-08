<script setup lang="ts">
import { onMounted } from 'vue'
import { useProdutoStore } from '@/stores/produtoStore'
import type { Produto } from '@/types/produto'

const store = useProdutoStore()

const headers = [
  { title: 'Id', key: 'id' },
  { title: 'Nome', key: 'nome' },
  { title: 'Preço', key: 'preco', align: 'end' as const },
  { title: 'Quantidade', key: 'quantidade', align: 'end' as const },
  { title: 'Ações', key: 'acoes', sortable: false, align: 'end' as const },
]

function formatarPreco(valor: number) {
  return valor.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })
}

async function excluir(produto: Produto) {
  if (!confirm(`Excluir o produto "${produto.nome}"?`)) return
  await store.remover(produto.id)
}

onMounted(() => {
  store.carregar()
})
</script>

<template>
  <div class="d-flex align-center justify-space-between mb-4">
    <h2 class="text-h5">Lista de produtos ({{ store.total }})</h2>
    <v-btn color="primary" prepend-icon="mdi-plus" :to="{ name: 'produto-novo' }">
      Novo produto
    </v-btn>
  </div>

  <v-card>
    <v-data-table
      :headers="headers"
      :items="store.produtos"
      :loading="store.carregando"
      item-value="id"
    >
      <template #item.preco="{ item }">
        {{ formatarPreco(item.preco) }}
      </template>

      <template #item.acoes="{ item }">
        <v-btn
          icon="mdi-pencil"
          variant="text"
          size="small"
          :to="{ name: 'produto-editar', params: { id: item.id } }"
        />
        <v-btn
          icon="mdi-delete"
          variant="text"
          size="small"
          color="error"
          @click="excluir(item)"
        />
      </template>
    </v-data-table>
  </v-card>
</template>
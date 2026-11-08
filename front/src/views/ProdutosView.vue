<script setup lang="ts">
import { onMounted } from 'vue'
import { useProdutoStore } from '@/stores/produtoStore'

const store = useProdutoStore()

function formatarPreco(valor: number) {
  return valor.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })
}

onMounted(() => {
  store.carregar()
})
</script>

<template>
  <section>
    <h2>Lista de produtos ({{ store.total }})</h2>

    <p v-if="store.carregando">Carregando...</p>

    <table v-else>
      <thead>
        <tr>
          <th>Id</th>
          <th>Nome</th>
          <th>Preço</th>
          <th>Quantidade</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="produto in store.produtos" :key="produto.id">
          <td>{{ produto.id }}</td>
          <td>{{ produto.nome }}</td>
          <td>{{ formatarPreco(produto.preco) }}</td>
          <td>{{ produto.quantidade }}</td>
        </tr>
      </tbody>
    </table>
  </section>
</template>
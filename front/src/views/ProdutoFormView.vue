<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import ProdutoForm from '@/components/ProdutoForm.vue'
import { produtoService } from '@/services/produtoService'
import { useProdutoStore } from '@/stores/produtoStore'
import type { ProdutoRequest } from '@/types/produto'

const route = useRoute()
const router = useRouter()
const store = useProdutoStore()

const id = route.params.id ? Number(route.params.id) : null
const produtoInicial = ref<ProdutoRequest>()
const carregando = ref(id !== null)

onMounted(async () => {
  if (id === null) return
  produtoInicial.value = await produtoService.obterPorId(id)
  carregando.value = false
})

async function salvar(dados: ProdutoRequest) {
  if (id === null) {
    await store.criar(dados)
  } else {
    await store.atualizar(id, dados)
  }
  router.push({ name: 'produtos' })
}

function cancelar() {
  router.push({ name: 'produtos' })
}
</script>

<template>
  <v-card max-width="480" class="mx-auto">
    <v-card-title>{{ id === null ? 'Novo produto' : 'Editar produto' }}</v-card-title>

    <v-card-text>
      <div v-if="carregando" class="d-flex justify-center pa-6">
        <v-progress-circular indeterminate color="primary" />
      </div>

      <ProdutoForm
        v-else
        :produto-inicial="produtoInicial"
        @salvar="salvar"
        @cancelar="cancelar"
      />
    </v-card-text>
  </v-card>
</template>
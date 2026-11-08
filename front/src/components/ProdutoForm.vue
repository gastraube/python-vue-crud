<script setup lang="ts">
import { reactive } from 'vue'
import type { SubmitEventPromise } from 'vuetify'
import type { ProdutoRequest } from '@/types/produto'

const props = defineProps<{
  produtoInicial?: ProdutoRequest
}>()

const emit = defineEmits<{
  salvar: [dados: ProdutoRequest]
  cancelar: []
}>()

const form = reactive<ProdutoRequest>({
  nome: props.produtoInicial?.nome ?? '',
  preco: props.produtoInicial?.preco ?? 0,
  quantidade: props.produtoInicial?.quantidade ?? 0,
})

const regras = {
  nome: [
    (v: string) => !!v || 'Informe o nome',
    (v: string) => (v.length >= 3 && v.length <= 100) || 'O nome deve ter entre 3 e 100 caracteres',
  ],
  preco: [(v: number) => v > 0 || 'O preço deve ser maior que zero'],
  quantidade: [(v: number) => v >= 0 || 'A quantidade não pode ser negativa'],
}

async function enviar(evento: SubmitEventPromise) {
  const { valid } = await evento
  if (!valid) return
  emit('salvar', { ...form })
}
</script>

<template>
  <v-form @submit.prevent="enviar">
    <v-text-field v-model="form.nome" label="Nome" :rules="regras.nome" />

    <v-text-field
      v-model.number="form.preco"
      label="Preço"
      type="number"
      step="0.01"
      prefix="R$"
      :rules="regras.preco"
    />

    <v-text-field
      v-model.number="form.quantidade"
      label="Quantidade"
      type="number"
      :rules="regras.quantidade"
    />

    <div class="d-flex justify-end ga-2">
      <v-btn variant="text" @click="emit('cancelar')">Cancelar</v-btn>
      <v-btn type="submit" color="primary">Salvar</v-btn>
    </div>
  </v-form>
</template>
import { createRouter, createWebHistory } from 'vue-router'
import ProdutosView from '@/views/ProdutosView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
   routes: [
    { path: '/', redirect: '/produtos' },
    { path: '/produtos', name: 'produtos', component: ProdutosView },
    {
      path: '/produtos/novo',
      name: 'produto-novo',
      component: () => import('@/views/ProdutoFormView.vue'),
    },
    {
      path: '/produtos/:id/editar',
      name: 'produto-editar',
      component: () => import('@/views/ProdutoFormView.vue'),
    },
  ],
})

export default router
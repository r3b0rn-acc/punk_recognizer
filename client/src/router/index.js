import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/UploadingView.vue'),
    },
    {
      path: '/processing/',
      name: 'processing',
      component: () => import('@/views/ProcessingView.vue')
    },
    {
      path: '/results/',
      name: 'results',
      component: () => import('@/views/ResultsView.vue')
    }
  ],
})

export default router

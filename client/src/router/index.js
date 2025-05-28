import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/RecognizerView.vue'),
    },
    {
      path: '/processing/',
      name: 'processing',
      component: () => import('@/views/ProcessingView.vue')
    }
  ],
})

export default router

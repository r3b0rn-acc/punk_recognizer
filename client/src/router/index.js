import { createRouter, createWebHistory } from 'vue-router'
import {useTaskStore} from "@/stores/taskStore.js";
import {storeToRefs} from "pinia";

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

router.beforeEach((to) => {
  const taskStore = useTaskStore()

  const { taskID, taskResult } = storeToRefs(taskStore)

  if (to.name === 'processing') {
    if (!taskID?.value) {
      taskStore.clearStore()  // на всякий случай
      return { name: 'home' }
    }
  }
  if (to.name === 'results') {
    if (!taskID?.value || !taskResult?.value) {
      taskStore.clearStore()  // на всякий случай
      return { name: 'home' }
    }
  }
})

export default router

<template>
  <div class="flex flex-col py-8 gap-12">
    <div class="flex flex-row flex-wrap gap-8 items-center justify-center">
      <div
        v-for="(result, indx) in results"
        :key="indx"
        class="cursor-pointer"
        @click="open(result.image_url)"
      >
        <image-block :src="result.image_url" />
      </div>
    </div>
    <div class="flex justify-center items-center">
      <button
        class="px-6 py-2 rounded-full bg-white transition-colors hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-black/70 cursor-pointer"
        @click="router.push({ name: 'home' })"
      >
        <span class="text-black text-lg font-medium">
          Загрузить еще
        </span>
      </button>
    </div>
  </div>

  <image-modal v-model="modalOpen" :src="openedSrc" alt="Просмотр изображения" width="50rem" height="50rem" />
</template>

<script setup>
import { ref, computed, onUnmounted } from 'vue'
import { useTaskStore } from '@/stores/taskStore.js'
import ImageBlock from '@/components/ImageBlock.vue'
import ImageModal from '@/components/ImageModal.vue'
import router from '@/router/index.js'

const taskStore = useTaskStore()
const taskResult = taskStore.taskResult

const results = computed(() =>
  taskResult.map(item => ({
    ...item,
    image_url: '/' + item.image_path.replace(/\\/g, '/')
  }))
)

const modalOpen = ref(false)
const openedSrc = ref('')

const open = src => {
  openedSrc.value = src
  modalOpen.value = true
}

onUnmounted(() => {
  taskStore.clearStore()
})
</script>
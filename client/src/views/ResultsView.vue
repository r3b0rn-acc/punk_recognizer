<template>
  <div class="flex flex-col py-8 gap-12">
    <div class="flex flex-row flex-wrap gap-8 items-center justify-center">
      <div
        v-for="(result, indx) in results"
        :key="indx"
      >
        <image-block :src="result.image_url" />
      </div>
    </div>
    <div class="flex justify-center items-center">
      <button
        class="px-6 py-2 rounded-full bg-white transition-colors hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-black/70"
        @click="router.push({name: 'home'})"
      >
        <span class="text-black text-lg font-medium">
          Загрузить еще
        </span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { useTaskStore } from "@/stores/taskStore.js";
import {computed, onUnmounted} from "vue";
import ImageBlock from "@/components/ImageBlock.vue";
import router from "@/router/index.js";

const taskStore = useTaskStore()
const taskResult = taskStore.taskResult

const results = computed(() => {
  return taskResult.map(item => ({
    ...item,
    image_url: '/' + item.image_path.replace(/\\/g, '/')
  }))
})

onUnmounted(() => {
  taskStore.clearStore()
})

</script>

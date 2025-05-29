<template>
  <div class="flex flex-col gap-8 items-center justify-center">
    <p class="font-bold text-lg break-normal">Ваша позиция в очереди:</p>
    <preloader size="13rem" v-model="queuePosition" />
  </div>
</template>

<script setup>
import Preloader from "@/components/Preloader.vue"
import { onMounted, onUnmounted, ref } from "vue"
import {useTaskStore} from "@/stores/taskStore.js";
import router from "@/router/index.js";

const taskStore = useTaskStore()

const queuePosition = ref(null)
const intervalId = ref(null)

const fetchStatus = async () => {
  try {
    const res = await taskStore.checkTaskStatus()
    queuePosition.value = res?.position

    if (res.status === 'SUCCESS') {
      clearInterval(intervalId.value)
      router.push({ name: 'results' })
    }
  } catch (e) {
    // pass
  }
}

onMounted(() => {
  fetchStatus()
  intervalId.value = setInterval(fetchStatus, 1000)
})

onUnmounted(() => {
  if (intervalId.value) clearInterval(intervalId.value)
})
</script>
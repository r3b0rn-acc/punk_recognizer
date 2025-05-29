<template>
  <div class="flex w-full h-auto items-center justify-center">
    <div class="flex flex-1 justify-center items-center p-8">
      <drag-and-drop-zone v-model="imageFile" />
    </div>
  </div>
</template>

<script setup>
import DragAndDropZone from "@/components/DragAndDropZone.vue"
import {ref, watch} from "vue"
import router from "@/router/index.js"
import {useTaskStore} from "@/stores/taskStore.js";


const taskStore = useTaskStore()

const imageFile = ref(null)

watch(imageFile, () => {
  taskStore.createTask(imageFile?.value)
  router.push({name: 'processing'})
})

</script>
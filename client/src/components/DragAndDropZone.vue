<template>
  <div
    class="flex flex-col items-center justify-center gap-8 p-8 rounded-3xl bg-primary w-full max-w-[50rem]"
  >
    <div
      ref="dropZone"
      class="flex flex-1 flex-col items-center border-2 border-dashed border-[#c5c5c5] rounded-3xl w-full max-w-[46rem] aspect-[184/75]"
      :class="{'cursor-pointer border-[#c5c5c5]/70': isOverDropZone}"
    >
      <p class="flex items-center text-xl text-center text-[#c5c5c5] h-full">
        <span v-if="!isOverDropZone">Перетащите своё изображение</span>
        <span v-else>Отпустите изображение</span>
      </p>
    </div>
    <button
      class="px-6 py-2 rounded-full bg-white text-black text-lg font-medium transition-colors hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-black/70 cursor-pointer"
      @click.stop="triggerInput"
    >
      <span>Загрузить фото</span>
    </button>
    <input
      ref="fileInput"
      type="file"
      class="hidden"
      accept="image/*"
      @change="onChange"
    />
  </div>
</template>

<script setup>
import {ref} from 'vue'
import { useDropZone } from '@vueuse/core'

const props = defineProps({
  modelValue: {
    type: File,
    required: false,
    default: null,
  }
})

const emit = defineEmits(['update:modelValue'])

const dropZone = ref(null)
const fileInput = ref(null)

const handleFile = (file) => {
  const allowedTypes = ['image/jpeg', 'image/png']
  const allowedExtensions = ['.jpg', '.jpeg', '.png']
  const fileType = file.type
  const fileName = file.name.toLowerCase()

  const hasValidType = allowedTypes.includes(fileType)
  const hasValidExtension = allowedExtensions.some(ext => fileName.endsWith(ext))

  if (!hasValidType || !hasValidExtension) {
    alert('Допустимы только изображения в формате JPG, JPEG или PNG')
    return
  }

  emit('update:modelValue', file)
}


const onDrop = (files) => {
  if (files && files.length === 1) {
    handleFile(files[0])
  }
}

const { isOverDropZone } = useDropZone(dropZone, {
  onDrop,
  multiple: false,
  preventDefaultForUnhandled: true,
})

const triggerInput = () => {
  fileInput.value?.click()
}

const onChange = (e) => {
  const file = e.target.files?.[0]
  if (file) {
    handleFile(file)
  }
  e.target.value = ''
}
</script>

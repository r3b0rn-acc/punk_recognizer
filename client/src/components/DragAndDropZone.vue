<template>
  <div
    ref="dropZone"
    :class="[
      'flex flex-col items-center justify-center gap-6 p-8 m-4 rounded-2xl border-2 border-dashed transition-shadow backdrop-blur-sm',
      isOverDropZone
        ? 'border-blue-400 bg-blue-50/70'
        : 'border-gray-300 bg-gray-50/70 hover:shadow-lg cursor-pointer'
    ]"
    @click="triggerInput"
  >
    <div>
      <attached-file-icon
        v-if="!previewUrl"
        class="w-32 h-32 text-gray-400"
      />
      <div v-else class="w-32 h-32">
        <img :src="previewUrl" alt="Preview" class="w-full h-full object-cover rounded-lg" />
      </div>
    </div>

    <p class="text-xl text-center text-gray-600">
      Перетащите изображение сюда<br />или нажмите для загрузки
    </p>
    <button
      class="px-6 py-2 rounded-full bg-blue-500 text-white text-lg font-medium transition-colors hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-300"
      @click.stop="triggerInput"
    >
      <span v-if="!previewUrl">Загрузить фото</span>
      <span v-else>Изменить фото</span>
    </button>
    <input
      ref="fileInput"
      type="file"
      class="hidden"
      accept="image/*"
      @change="onFileChange"
    />
  </div>
</template>

<script setup>
import { ref, onUnmounted } from 'vue'
import { useDropZone } from '@vueuse/core'
import AttachedFileIcon from '@/components/icons/AttachedFileIcon.vue'

const dropZone = ref(null)
const fileInput = ref(null)

const file = ref(null)
const previewUrl = ref('')

const onDrop = (files) => {
  if (files && files.length === 1) {
    const f = files[0]
    if (!f.type.startsWith('image')) {
      alert('Файл должен быть изображением')
      return
    }

    if (previewUrl.value) {
      URL.revokeObjectURL(previewUrl.value)
      previewUrl.value = ''
    }

    file.value = {
      name: f.name,
      size: f.size,
      type: f.type,
    }
    previewUrl.value = URL.createObjectURL(f)
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


const onFileChange = (e) => {
  const files = e.target.files
  if (files && files.length === 1) {
    onDrop(Array.from(files))
  }
}

onUnmounted(() => {
  if (previewUrl.value) {
    URL.revokeObjectURL(previewUrl.value)
  }
})
</script>

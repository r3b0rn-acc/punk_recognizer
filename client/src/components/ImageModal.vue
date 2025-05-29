<template>
  <teleport to="body">
    <transition name="fade">
      <div
        v-if="modelValue"
        class="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm"
      >
        <div
          ref="modalRef"
          tabindex="-1"
          @keydown.esc="close"
          class="relative max-h-[90vh] max-w-[90vw] shadow-xl outline-none"
        >
          <button
            @click="close"
            class="absolute top-2 right-2 z-10 text-white bg-black/50 hover:bg-black/70 rounded-full p-1 transition-colors"
          >
            <close-icon />
          </button>
          <div class="overflow-auto max-h-[90vh] max-w-[90vw]">
            <img
              :src="src"
              :alt="alt"
              class="block max-h-full max-w-full object-contain"
              :style="sizeStyle"
            />
          </div>
        </div>
      </div>
    </transition>
  </teleport>
</template>


<script setup>
import { ref } from 'vue'
import { onClickOutside } from '@vueuse/core'
import CloseIcon from "@/components/icons/CloseIcon.vue";

const props = defineProps({
  src: {
    type: String,
    required: true
  },
  alt: {
    type: String,
    default: ''
  },
  modelValue: {
    type: Boolean,
    default: false
  },
  height: {
    type: String,
    default: '10rem',
  },
  width: {
    type: String,
    default: '10rem'
  },
})
const emit = defineEmits(['update:modelValue', 'close'])

const modalRef = ref(null)

function close () {
  emit('update:modelValue', false)
  emit('close')
}

onClickOutside(modalRef, close)


const sizeStyle = {
  'max-width': props.width,
  'max-height': props.height
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.15s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
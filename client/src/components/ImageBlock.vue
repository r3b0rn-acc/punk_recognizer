<template>
  <div class="bg-primary rounded-3xl p-4 w-full max-w-[15rem]">
    <img :src="props.src" alt="Preview" />
  </div>
</template>

<script setup>
const props = defineProps({
  src: {
    type: String,
    required: true,
  },
})
</script>

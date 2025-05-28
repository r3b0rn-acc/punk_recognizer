<template>
  <div class="flex flex-1 items-center justify-between">
    <div class="flex justify-center items-center h-[23.5rem]">
      <drag-and-drop-zone />
      <div class="text-center text-white text-[10rem]">ТУ БИ КОНТИНУЕД...</div>
    </div>
  </div>
</template>

<script setup>
import DragAndDropZone from "@/components/DragAndDropZone.vue";
</script>
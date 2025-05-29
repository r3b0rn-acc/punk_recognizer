<template>
  <header class="flex flex-row justify-start items-center bg-primary h-16 p-8">
    <span
      class="font-bold text-base text-white cursor-pointer"
      @click="router.push({name: 'home'})"
    >
      ПУНК РЕКОГНАЙЗЕР
    </span>
  </header>
</template>
<script setup lang="ts">
import router from "@/router/index.js";
</script>
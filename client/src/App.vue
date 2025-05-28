<template>
  <div class="app-background flex flex-col min-h-screen align-center">
    <h1 class="text-center font-bold text-[5rem]">
      ПУНК РЕКОГНАЙЗЕР
    </h1>
    <router-view v-slot="{ Component }">
      <keep-alive>
        <component :is="Component" />
      </keep-alive>
    </router-view>
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router'
</script>

<style scoped>
  .app-background {
    @apply bg-cover bg-center bg-no-repeat;
    background-image: url('/src/assets/puck_background.jpg');
  }
</style>
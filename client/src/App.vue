<template>
  <div class="app justify-between align-center">
    <nav class="flex flex-row justify-start items-center sticky top-0 bg-primary h-16 p-8">
      <span class="font-bold text-base text-white">
        ПУНК РЕКОГНАЙЗЕР
      </span>
    </nav>
    <router-view v-slot="{ Component }">
      <keep-alive>
        <component :is="Component" />
      </keep-alive>
    </router-view>
    <nav class="flex flex-row justify-between items-center sticky bottom-0 bg-primary h-16 p-8">
      <span class="text-base text-white">
        © 2025 ПМ-ПУ. Все права защищены.
      </span>
      <div>
        <a href="https://github.com/r3b0rn-acc/punk_recognizer">
          GitHub
        </a>
      </div>
    </nav>
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router'
</script>

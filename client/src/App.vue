<template>
  <header-main class="sticky top-0" />
  <div class="app justify-center align-center">
    <router-view />
  </div>
  <footer-main class="bottom-0" />
</template>

<script setup>
import { RouterView } from 'vue-router'
import FooterMain from "@/components/FooterMain.vue";
import HeaderMain from "@/components/HeaderMain.vue";
</script>

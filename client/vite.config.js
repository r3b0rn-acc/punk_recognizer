import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'

import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite';


export default defineConfig({
  plugins: [
    vue(),
    tailwindcss(),
  ],
  server: {
    origin: 'http://localhost:5173'
  },
  base: '/static/punk_recognizer/',
  build: {
    manifest: 'manifest.json',
    emptyOutDir: true,
    outDir: '../static/punk_recognizer/',
    rollupOptions: {
      input: './src/main.js',
    }
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
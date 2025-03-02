import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],

  server: {
    proxy: {
      '/analyse-pdf': {
        target: 'http://127.0.0.1:80', // statt 192.168.49.2
        headers: { Host: 'backend.pdf-extract.com' },
        changeOrigin: true,
        rewrite: (path) => path, // falls du den Pfad nicht ändern möchtest
      },
    },

    allowedHosts: ['pdf-extract.com']
  },
})

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import 'bootstrap/dist/css/bootstrap.min.css'
import './assets/styles.css' // Eigene globale Styles (optional)

createApp(App).use(router).mount('#app')

import { createRouter, createWebHistory } from 'vue-router'
import DragAndDropView from '@/views/DragAndDropView.vue'
import DisplayCardView from '@/views/DisplayCardView.vue'

const routes = [
  { path: '/', redirect: '/upload' },
  { path: '/upload', name: 'UploadView', component: DragAndDropView },
  { path: '/flashcards', name: 'DisplayCardView', component: DisplayCardView }
]

export default createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

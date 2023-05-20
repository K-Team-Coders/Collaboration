import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    
    component: () => import('../views/MainPage.vue')
  },

]


const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router

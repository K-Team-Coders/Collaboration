import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    
    component: () => import('../views/MainPage.vue')
  },
  {
    path: '/datamarking',
    name: 'datamarking',
    
    component: () => import('../components/DataMark.vue')
  },

]


const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router

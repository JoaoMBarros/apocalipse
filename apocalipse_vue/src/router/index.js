import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/sobrevivencia/:id',
    name: 'sobrevivencia',
    component: () => import(/* webpackChunkName: "sobrevivencia" */ '../views/SobrevivenciaView.vue')
  },
  {
    path: '/sobrevivencia/:id/iniciar',
    name: 'inicio',
    component: () => import(/* webpackChunkName: "sobrevivencia" */ '../views/InicioSobrevivencia.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

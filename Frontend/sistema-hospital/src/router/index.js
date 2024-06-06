import { createRouter, createWebHistory } from 'vue-router'
import loginView from '@/components/login.vue'
import registerUser from '@/components/registerUser.vue'
import dashboard from '@/components/dashboard.vue'
import registrarUsuarios from '@/components/registrarUsuarios.'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: loginView
    },  
    {
      path: '/register',
      name: 'register',
      component: registerUser
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: dashboard
    },

    {
      path: '/registro',
      name: 'registrarUsuarios',
      component: registrarUsuarios
    }



  ]
})

export default router

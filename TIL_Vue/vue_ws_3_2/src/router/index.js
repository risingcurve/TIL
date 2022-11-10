import Vue from 'vue'
import VueRouter from 'vue-router'
import TheLunch from '@/views/TheLunch'
import TheLotto from '@/views/TheLotto'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'lunch',
    component: TheLunch
  },
  {
    path: '/',
    name: 'lotto',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: TheLotto
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

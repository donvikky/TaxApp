import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'

// Bootstrap js
import $ from 'jquery'
import 'bootstrap'

// LightBootstrap plugin
import LightBootstrap from './plugins'

// router setup
import routes from './routes/routes'
// plugin setup
Vue.use(VueRouter)
Vue.use(LightBootstrap)

// configure router
const router = new VueRouter({
  routes, // short for routes: routes
  linkActiveClass: 'nav-item active'
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  render: h => h(App),
  router
})

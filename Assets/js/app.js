import Vue from 'vue'
import App from './App.vue'
import components from './components'
import Plugins from './plugins'
/* eslint-disable no-unused-vars */
import $ from 'jquery'
import 'bootstrap'

Vue.use(Plugins)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components,
  render: h => h(App)
})

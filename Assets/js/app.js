import Vue from 'vue'
import components from './components'
import CompositePlugin from './plugins'

Vue.use(CompositePlugin)

const app = new Vue({
  el: '#app',
  components
})

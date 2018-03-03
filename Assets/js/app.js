import Vue from 'vue'
import components from './components'
import Plugins from './plugins'
require('bootstrap')

Vue.use(Plugins)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components
})

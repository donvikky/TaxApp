import Vue from 'vue'
import components from './components'
import Plugins from './plugins'
/* eslint-disable no-unused-vars */
import $ from 'jquery'
import 'bootstrap'
import Raphael from 'raphael/raphael'

window.jQuery = window.jquery = $
window.Raphael = Raphael

Vue.use(Plugins)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components
})

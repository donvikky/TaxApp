import VTooltip from 'v-tooltip'
import Notifications from 'vue-notifyjs'
import AxiosPlugin from './axios'
import SideBar from './sidebar'
import DebugMode from './debug-mode'
import Directives from './directives'
import GlobalComponents from './global-components'
// library auto imports
import 'es6-promise/auto'

export default {
  install (Vue) {
    Vue.use(AxiosPlugin)
    Vue.use(DebugMode)
    Vue.use(Directives)
    Vue.use(GlobalComponents)
    Vue.use(Notifications)
    Vue.use(SideBar)
    Vue.use(VTooltip)
  }
}

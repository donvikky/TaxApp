import axios from 'axios'


const installAxios = Vue => {
  document.addEventListener('DOMContentLoaded', event => {
    const instance = axios.create({
      headers: {
        'X-Requested-With': 'XMLHttpRequest',
        'Accept': 'application/json',
        'Authorization': 'Bearer token', // @todo: fetch token
        'X-CSRF-Token': document.querySelector('meta[name="csrftoken"]').content
      }
    })

    Object.defineProperty(Vue.prototype, '$axios', {value: instance})
  })
}


const debugMode = Vue => {
  if (process.env.NODE_ENV !== 'production') {
    Vue.config.debug = true
    Vue.config.devtools = true
  }
}


export default {
  install (Vue) {
    installAxios(Vue)
    debugMode(Vue)
  }
}

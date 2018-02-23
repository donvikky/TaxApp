import axios from 'axios'

const AxiosPlugin = {
  install (Vue) {
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
}

export default AxiosPlugin

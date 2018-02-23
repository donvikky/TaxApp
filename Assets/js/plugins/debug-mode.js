const DebugMode = {
  install (Vue) {
    if (process.env.NODE_ENV !== 'production') {
      Vue.config.debug = true
      Vue.config.devtools = true
    }
  }
}

export default DebugMode

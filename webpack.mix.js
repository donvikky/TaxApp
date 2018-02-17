let mix = require('laravel-mix')
let webpack = require('webpack')
let process = require('process')

let assetPublishPath = 'Assets/dist'

mix.setPublicPath(assetPublishPath)

mix.webpackConfig({
  plugins: [
    new webpack.DefinePlugin({
      'process.env.NODE_ENV': `"${process.env.NODE_ENV}"`
    })
  ]
})

mix.js('Assets/js/app.js', 'app.js')
  .sass('Assets/sass/app.scss', 'app.css')
  .copyDirectory('Assets/images', assetPublishPath + '/images')
  .autoload({
    jquery: ['$', 'window.jQuery', 'window.jquery']
  })
  .extract([
    'vue', 'vuex', 'vue-router', 'axios', 'jquery', 'bootstrap', 'chartist',
    'es6-promise', 'google-maps', 'v-tooltip', 'vue-clickaway',
    'vue-notifyjs', 'vue2-google-maps'
  ])

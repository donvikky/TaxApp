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

mix
  .js('Assets/js/app.js', 'app.js')
  .sass('Assets/sass/app.scss', 'app.css')
  .copyDirectory('Assets/images', assetPublishPath + '/images')
  .autoload({
    chartist: ['Chartist'],
    jquery: ['$', 'window.jQuery', 'window.jquery'],
    'popper.js': ['Popper']
  })
  .extract([
    'vue', 'axios', 'jquery', 'bootstrap', 'es6-promise', 'popper.js',
    'chartist', 'vue-clickaway', 'vue-notifyjs'
  ])

<template>
  <component :is="tag"
             @click.native="hideSidebar"
             v-bind="$attrs"
             tag="li">
    <a class="nav-link">
      <slot>
        <i v-if="link.icon" :class="link.icon"></i>
        <p>{{link.name}}</p>
      </slot>
    </a>
  </component>
</template>
<script>
/** delete later */
import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter)
/** delete later end */
  export default {
    inheritAttrs: false,
    inject: {
      autoClose: {
        default: true
      }
    },
    props: {
      link: {
        type: [String, Object],
        default: () => {
          return {
            name: '',
            path: '',
            icon: ''
          }
        }
      },
      tag: {
        type: String,
        default: 'router-link'
      }
    },
    methods: {
      hideSidebar () {
        if (this.autoClose && this.$sidebar && this.$sidebar.showSidebar === true) {
          this.$sidebar.displaySidebar(false)
        }
      }
    }
  }
</script>
<style>
</style>

<template>
  <div :class="{'nav-open': $sidebar.showSidebar}">
    <notifications></notifications>

    <div class="wrapper">
      <side-bar>
        <mobile-menu slot="content"></mobile-menu>
        <sidebar-link to="/dashboard/overview">
          <i class="nc-icon nc-chart-pie-35"></i>
          <p>Dashboard</p>
        </sidebar-link>
        <sidebar-link to="/dashboard/enrollment">
          <i class="nc-icon nc-paper-2"></i>
          <p>TIN Enrollment</p>
        </sidebar-link>
        <sidebar-link to="/dashboard/user">
          <i class="nc-icon nc-circle-09"></i>
          <p>User Profile</p>
        </sidebar-link>
      </side-bar>
      <div class="main-panel">
        <top-navbar></top-navbar>

        <dashboard-content @click="toggleSidebar">
          <slot>
            <h1>No Content</h1>
          </slot>
        </dashboard-content>

        <content-footer></content-footer>
      </div>
    </div>
  </div>
</template>
<style lang="scss">

</style>
<script>
  import TopNavbar from './TopNavbar.vue'
  import ContentFooter from './ContentFooter.vue'
  import DashboardContent from './Content.vue'
  import MobileMenu from './MobileMenu.vue'
  export default {
    name: 'dashboard',
    components: {
      TopNavbar,
      ContentFooter,
      DashboardContent,
      MobileMenu
    },
    methods: {
      toggleSidebar () {
        if (this.$sidebar.showSidebar) {
          this.$sidebar.displaySidebar(false)
        }
      }
    }
  }
</script>

<style lang="scss">
.vue-notifyjs.notifications{
  .list-move {
    transition: transform 0.3s, opacity 0.4s;
  }
  .list-item {
    display: inline-block;
    margin-right: 10px;
  }
  .list-enter-active {
    transition: transform 0.2s ease-in, opacity 0.4s ease-in;
  }
  .list-leave-active {
    transition: transform 1s ease-out, opacity 0.4s ease-out;
  }
  .list-enter {
    opacity: 0;
    transform: scale(1.1);
  }
  .list-leave-to {
    opacity: 0;
    transform: scale(1.2, 0.7);
  }
}
</style>

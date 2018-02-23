<template>
  <div class="content">
    <div class="container-fluid">
      <div class="row">
        <div class="col-12">
          <card>
            <template slot="header">
              <h4 class="card-title">Enrollment</h4>
              <p class="card-category">Enroll New Tax Payer</p>
            </template>
            
            <!-- content goes here -->
            <slot></slot>

          </card>
        </div>

      </div>
    </div>
  </div>
</template>
<script>
  import Card from '../../UIComponents/Cards/Card.vue'
  import Individual from './Enrollment/Individual.vue'

  export default {
    components: {
      Card,
      Individual
    }
  }

</script>
<style>

</style>

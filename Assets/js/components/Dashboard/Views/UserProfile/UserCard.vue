<template>
  <card class="card-user">
    <img slot="image" src="https://ununsplash.imgix.net/photo-1431578500526-4d9613015464?fit=crop&fm=jpg&h=300&q=75&w=400" alt="..."/>
    <div class="author">
      <a href="#">
        <img class="avatar border-gray" src="/static/images/default-avatar.png" alt="..."/>

        <h4 class="title">{{ fullName }}<br />
          <small>{{ username }}</small>
        </h4>
      </a>
    </div>
  </card>
</template>
<script>
import Card from "../../../UIComponents/Cards/Card.vue";
export default {
  components: {
    Card
  },
  props: {
    username: {
      type: String,
      required: true
    },
    fullName: {
      type: String,
      required: true
    }
  }
}
</script>
<style>

</style>

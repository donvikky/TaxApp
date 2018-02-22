<template>
  <card class="card-user">
    <img slot="image" src="https://ununsplash.imgix.net/photo-1431578500526-4d9613015464?fit=crop&fm=jpg&h=300&q=75&w=400" alt="..."/>
    <div class="author">
      <a href="#">
        <img class="avatar border-gray" src="/static/images/default-avatar.png" alt="..."/>

        <h4 class="title">Jack Bauer<br />
          <small>admin</small>
        </h4>
      </a>
    </div>
    <!--div slot="footer" class="text-center">
    </div-->
  </card>
</template>
<script>
import Card from "../../../UIComponents/Cards/Card.vue";
export default {
  components: {
    Card
  },
  data() {
    return {
      details: [
        {
          title: "12",
          subTitle: "Files"
        },
        {
          title: "2GB",
          subTitle: "Used"
        },
        {
          title: "24,6$",
          subTitle: "Spent"
        }
      ]
    };
  },
  methods: {
    getClasses(index) {
      var remainder = index % 3;
      if (remainder === 0) {
        return "col-md-3 col-md-offset-1";
      } else if (remainder === 2) {
        return "col-md-4";
      } else {
        return "col-md-3";
      }
    }
  }
};
</script>
<style>

</style>

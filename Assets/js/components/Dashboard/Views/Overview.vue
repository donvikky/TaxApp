<template>
  <div class="content">
    <div class="container-fluid">
      <div class="row">
        <div class="col-xl-4 col-md-6">
          <stats-card>
            <div slot="header" class="icon-success">
              <i class="fa fa-users text-success"></i>
            </div>
            <div slot="content">
              <p class="card-category">Individuals</p>
              <h4 class="card-title">{{ individualEnrollments }}</h4>
            </div>
            <div slot="footer">
              <i class="fa fa-refresh"></i>Updated <span class="timeago" :datetime="now"></span>
            </div>
          </stats-card>
        </div>

        <div class="col-xl-4 col-md-6">
          <stats-card>
            <div slot="header" class="icon-danger">
              <i class="fa fa-building text-danger"></i>
            </div>
            <div slot="content">
              <p class="card-category">Corporates</p>
              <h4 class="card-title">{{ corporateEnrollments }}</h4>
            </div>
            <div slot="footer">
              <i class="fa fa-refresh"></i>Updated <span class="timeago" :datetime="now"></span>
            </div>
          </stats-card>
        </div>

        <div class="col-xl-4 col-md-6">
          <stats-card>
            <div slot="header" class="icon-info">
              <i class="fa fa-cubes text-primary"></i>
            </div>
            <div slot="content">
              <p class="card-category">Total Enrollments</p>
              <h4 class="card-title">{{ totalEnrollments }}</h4>
            </div>
            <div slot="footer">
              <i class="fa fa-refresh"></i>Updated <span class="timeago" :datetime="now"></span>
            </div>
          </stats-card>
        </div>

      </div>

      <div class="row">
        <div class="col">
          <chart-card
            :chart-data="pieChart.data"
            chart-type="Pie">
            <template slot="header">
              <h4 class="card-title">Enrollments</h4>
              <p class="card-category">All enrollments to date</p>
            </template>
            <template slot="footer">
              <div class="legend">
                <i class="fa fa-circle text-info"></i> Individual
                <i class="fa fa-circle text-danger"></i> Corporate
              </div>
            </template>
          </chart-card>
        </div>
      </div>

    </div>
  </div>
</template>
<script>
import timeago from "timeago.js";
import ChartCard from "../../UIComponents/Cards/ChartCard.vue";
import StatsCard from "../../UIComponents/Cards/StatsCard.vue";
import Card from "../../UIComponents/Cards/Card.vue";
import LTable from "../../UIComponents/Table.vue";
import Checkbox from "../../UIComponents/Inputs/Checkbox.vue";

export default {
  mounted() {
    timeago().render(document.querySelectorAll(".timeago"));
    console.log("context: ", this.context);
  },
  components: {
    Checkbox,
    Card,
    LTable,
    ChartCard,
    StatsCard
  },
  props: ["context"],
  data() {
    return {
      now: new Date()
    };
  },
  computed: {
    chartData() {
      months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec"
      ];
    },
    individualEnrollments() {
      return this.context.counts.individual;
    },
    corporateEnrollments() {
      return this.context.counts.corporate;
    },
    totalEnrollments() {
      return this.individualEnrollments + this.corporateEnrollments;
    }
  }
};
</script>
<style>

</style>

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
              <i class="fa fa-refresh"></i>Updated
              <span class="timeago" :datetime="now"></span>
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
              <i class="fa fa-refresh"></i>Updated
              <span class="timeago" :datetime="now"></span>
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
              <i class="fa fa-refresh"></i>Updated
              <span class="timeago" :datetime="now"></span>
            </div>
          </stats-card>
        </div>

      </div>

      <div class="row">
        <div class="col">
          <div class="card">
            <div class="card-header">
              <h4 class="card-title">Enrollments</h4>
              <p class="card-category">Monthly enrollments for last 12 months</p>
            </div>
            <div class="card-body">
              <bar-chart id="bar-chart" data="chartData" xkey="month" ykeys="['individual', 'corporate']" bar-colors="['#17a2b8', '#dc3545']" grid="true" grid-text-weight="bold" resize="true">
              </bar-chart>
            </div>
            <div class="card-footer">
              <div class="legend">
                <i class="fa fa-circle text-info"></i> Individual
                <i class="fa fa-circle text-danger"></i> Corporate
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>
<script>
import timeago from "timeago.js";
import BarChart from 'vue-morris/src/components/bar-chart.vue'
import StatsCard from "../../UIComponents/Cards/StatsCard.vue";
import Card from "../../UIComponents/Cards/Card.vue";
import LTable from "../../UIComponents/Table.vue";
import Checkbox from "../../UIComponents/Inputs/Checkbox.vue";


export default {
  mounted() {
    timeago().render(document.querySelectorAll(".timeago"));
    console.log(this.chartData)
  },
  components: {
    BarChart,
    Card,
    Checkbox,
    LTable,
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
      let months = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
        "Aug", "Sep", "Oct", "Nov", "Dec"
      ];
      let data = []
      months.map((month, index) => {
        let monthCode = ++index
        data.push({
          month: this.getMonth(monthCode),
          individual: this.getCount(monthCode, true),
          corporate: this.getCount(monthCode)
        })
      })
      // sort data such that current year items are last
      let isCurrentYear = i => {
        return (i.month.split(' ')[1].trim() == `${(new Date).getFullYear()}`)
      }

      let isPreviousYear = m => !isCurrentYear(m)
      return data.filter(isPreviousYear).concat(data.filter(isCurrentYear))
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
  },
  methods: {
    getCount(monthCode, individual=false) {
      let months = individual ? this.context.months.individual : this.context.months.corporate
      let count = months.filter(m => m.month === monthCode)
                    .reduce((acc, m) => acc + m.count, 0)
      return count
    },
    getMonth(monthCode){
      let label
      switch(monthCode) {
        case 1:
          label = 'Jan'
          break
        case 2:
          label = 'Feb'
          break
        case 3:
          label = 'Mar'
          break
        case 4:
          label = 'Apr'
          break
        case 5:
          label = 'May'
          break
        case 6:
          label = 'Jun'
          break
        case 7:
          label = 'Jul'
          break
        case 8:
          label = 'Aug'
          break
        case 9:
          label = 'Sep'
          break
        case 10:
          label = 'Oct'
          break
        case 11:
          label = 'Nov'
          break
        case 12:
          label = 'Dec'
          break
        default:
         throw new Error('Invalid Month Code')
      }

      let now = new Date()
      return (monthCode <= now.getMonth()) ?
                `${label} ${now.getFullYear()}` :
                `${label} ${now.getFullYear() - 1}`
    }
  }
};
</script>
<style>

</style>

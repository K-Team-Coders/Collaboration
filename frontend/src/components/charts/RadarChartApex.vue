<template>
  <div class="flex">
    <apexchart
      height="400"
      width="570"
      :options="chartOptions"
      :series="items"
      type="radar"
    ></apexchart>
  </div>
</template>

<script>
import VueApexCharts from "vue3-apexcharts";
export default {
  components: {
    apexchart: VueApexCharts,
  },
  
  computed: {
        items(){
          let series = {}
          let series_radar = []
          this.radardata.forEach(element => {
            series.name = element.market, 
            series.data = Array(element.good, element.article, element.delivery, element.post, element.times) });
            
            console.log(series)
            return series
        }
        
      },
      props:{
    radardata: Array
  },
  data() {
    return {
      chartOptions: {
        title: {
          text: "Проблемы по партнерам",
        },
        stroke: {
          width: -70,
        },
        fill: {
          opacity: 0.2,
        },
        markers: {
          size: 0,
        },
        xaxis: {
          categories: [
            "Все хорошо",
            "Проблема с товаром",
            "Проблема с доставкой",
            "Проблема с постаматом",
            "Проблема со сроками",
          ],
        },
      },
      
    };
  },
};
</script>

<style>
</style>

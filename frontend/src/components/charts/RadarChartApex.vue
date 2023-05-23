<template>
  <div class="">
    <apexchart
      height="580"
      width="770"
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
            series = {}
            series.name = element.market, 
            series.data = Array(element.good, element.article, element.delivery, element.post, element.times),
            series_radar.push(series) });
            
            console.log(series_radar)
            return series_radar
        }
        
      },
      props:{
    radardata: Array
  },
  data() {
    return {
      chartOptions: {
        title: {
          text: "Проблема партнеров по отзывам",
        },
        stroke: {
          width: -70,
        },
        fill: {
          opacity: 0.4,
        },
        markers: {
          size: 4,
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

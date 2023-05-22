<template>
  <div class="flex">
    <apexchart
      height="250"
      width="600"
      :options="chartOptions"
      :series="series"
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
      series: [
        {
          name: "Я.Маркет",
          data: [678, 345, 100, 150, 30],
        },
        {
          name: "OZON",
          data: [778, 445, 600, 250, 50],
        },
        {
          name: "Undefind",
          data: [378, 145, 200, 750, 10],
        },
      ],
    };
  },
};
</script>

<style></style>

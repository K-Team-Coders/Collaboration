<template>
    <apexchart type="area" height="350" :options="chartOptions" :series="series"></apexchart>
</template>

<script>
export default {
    data: {
          
          series: [{
            name: "STOCK ABC",
            data: series.monthDataSeries1.prices
          }],
          chartOptions: {
            chart: {
              type: 'area',
              height: 350,
              zoom: {
                enabled: false
              }
            },
            dataLabels: {
              enabled: false
            },
            stroke: {
              curve: 'straight'
            },
            
            title: {
              text: 'Fundamental Analysis of Stocks',
              align: 'left'
            },
            subtitle: {
              text: 'Price Movements',
              align: 'left'
            },
            labels: series.monthDataSeries1.dates,
            xaxis: {
              type: 'datetime',
            },
            yaxis: {
              opposite: true
            },
            legend: {
              horizontalAlign: 'left'
            }
          },
          
          
        },
        }
</script>

<style></style>
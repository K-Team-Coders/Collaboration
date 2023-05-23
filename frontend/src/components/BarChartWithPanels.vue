<template>
  <div
    class="flex items-center justify-center border-idealRed border-4 rounded-lg shadow-cards"
  >
    <BarChart />
  </div>
</template>
<script>
import BarChart from '@/components/charts/BarChart.vue'
export default {
  components: {
    BarChart
  }
}
</script>

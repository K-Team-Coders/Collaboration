<template>
  <div class="border-idealRed border-4 rounded-lg shadow-cards">
    <BarChart :bardata="bardata"/>
    <PanelGroup />
  </div>
</template>
<script>
import Panel from "./Panel.vue";
import BarChart from "@/components/charts/BarChart.vue";
import PanelGroup from "./PanelGroup.vue";
export default {
  props:{
    bardata: Object,
  },
  components: {
    Panel,
    PanelGroup,
    BarChart,
  },
};
</script>

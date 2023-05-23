<template>
  <div class="h-full w-full">
    <div class="border-idealRed border-4 h-full rounded-lg shadow-cards">
      <RadarChartApex :radardata="radardata"/>
      <PanelGroup />
    </div>
  </div>
</template>
<script>
import PanelGroup from "./PanelGroup.vue";
import RadarChartApex from "@/components/charts/RadarChartApex.vue";

export default {
  components: {
    PanelGroup,
    RadarChartApex,
  },
  props:{
    radardata: Array,
  }
};
</script>

<template>
  <div>
    <div class="border-idealRed border-4 rounded-lg mt-4 shadow-cards">
      <RadarChartApex />
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
};
</script>

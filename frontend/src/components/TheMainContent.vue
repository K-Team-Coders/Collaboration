<template>
  <div class="ml-64 pt-20">
    <div class="px-5 py-4 h-full bg-white">
      <div class="grid grid-cols-3 gap-3 mb-4">
        <Panel  label="Всего постаматов" icon="box" :views="allpostamats.totalStats.postamats" />
        <Panel label="Всего отзывов" icon="chat" :views="allpostamats.totalStats.reviews" />
        <Panel label="Всего партнеров" icon="parther" :views="allpostamats.totalStats.partners" />
      </div>
      <Map :postamat_list="allpostamats.data"> </Map>
    </div>
    <div class="px-5 py-3 shadow-innerMax h-full">
      <div class="grid grid-cols-2 gap-3">
        <RadarChartWithPanels :radardata="allpostamats.marketStats"/>
        <BarChartWithPanels :bardata="allpostamats.classStats"/>
      </div>
    </div>
    <div class="p-5 bg-white">
      <Table :postamats_list="allpostamats.adressStats" />
      <div class="flex justify-start">
        <DownloadButton label="Импорт в .xls" icon="document" />
      </div>
    </div>
  </div>
</template>
<script>
import Panel from "@/components/Panel.vue";

import Map from "@/components/Map.vue";
import Table from "@/components/Table.vue";
import DownloadButton from "@/components/DownloadButton.vue";
import Filter from "@/components/Filter.vue";
import Button from "@/components/Button.vue";
import BarChart from "@/components/charts/BarChart.vue";
import RadarChartWithPanels from "./RadarChartWithPanels.vue";
import BarChartWithPanels from "./BarChartWithPanels.vue";
import ProgressBar from "./ProgressBar.vue";
export default {
  components: {
    BarChart,
    Button,
    BarChartWithPanels,
    Panel,
    Filter,
    Map,
    DownloadButton,
    RadarChartWithPanels,
    Table,
    ProgressBar,
  },
  data() {
    return {};
  },
  computed: {
    postamat_count() {
      let adress_list = [];
      this.allpostamats.data.forEach((element) => adress_list.push(element.adress));
      let unique_postamat_list = Array.from(new Set(adress_list));
      return unique_postamat_list.length;
    },
  },
  props: {
    allpostamats: Object,
  },
  
};
</script>

<template>
  <div class="ml-64 pt-20">
    <div class="px-5 py-4 h-full bg-white">
      <div class="grid grid-cols-3 gap-3 mb-4">
        <Panel label="Всего постаматов" icon="box" :views="postamat_count" />
        <Panel label="Всего отзывов" icon="chat" :views="allpostamats.length" />
        <Panel label="Всего партнеров" icon="parther" views="100" />
      </div>
      <Map :postamat_list="allpostamats"> </Map>
    </div>
    <div class="px-5 py-3 shadow-innerMax">
      <div class="grid grid-cols-2 gap-3">
        <RadarChartWithPanels />
        <BarChartWithPanels />
      </div>
    </div>
    <div class="p-5 bg-white">
      <Table :postamats_list="allpostamats" />
      <div class="flex justify-start">
        <DownloadButton label="Импорт в .xls" icon="document" />
      </div>
    </div>
  </div>
</template>
<script>
import Panel from "@/components/Panel.vue";
import { mapActions, mapGetters } from "vuex";
import Map from "@/components/Map.vue";
import Table from "@/components/Table.vue";
import DownloadButton from "@/components/DownloadButton.vue";
import Filter from "@/components/Filter.vue";
import Button from "@/components/Button.vue";
import BarChart from "@/components/charts/BarChart.vue";
import RadarChartWithPanels from "./RadarChartWithPanels.vue";
import BarChartWithPanels from "./BarChartWithPanels.vue";
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
  },
  data() {
    return {};
  },
  computed: {
    ...mapGetters(["allpostamats"]),
    postamat_count() {
      let adress_list = [];
      this.allpostamats.forEach((element) => adress_list.push(element.adress));
      let unique_postamat_list = Array.from(new Set(adress_list));
      return unique_postamat_list.length;
    },
  },
  methods: {
    ...mapActions(["GET_ALLPOSTAMATS"]),
  },
  async created() {
    this.GET_ALLPOSTAMATS();
  },
};
</script>

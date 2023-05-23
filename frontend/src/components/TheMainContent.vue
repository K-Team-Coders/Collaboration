<template>
  <div class="ml-64 pt-20">
    <div class="p-5 h-full bg-white">
      <Map :postamat_list="allpostamats"> </Map>
    </div>
    <div class="p-5">
      <div class="grid grid-cols-3 gap-3">
        <Panel label="Всего постаматов" icon="box" :views="postamat_count" />
        <Panel label="Всего отзывов" icon="chat" :views="allpostamats.length" />
        <Panel label="Всего партнеров" icon="parther" views="100" />
      </div>
      <div class="grid grid-cols-2 gap-3">
        <RadarChartWithPanels />
        <div class="border-idealRed border-4 rounded-lg mt-4 shadow-cards">
          <BarChart />
          <div class="grid grid-cols-3 px-3 pb-2 ml-4 justify-center">
            <Panel
              label="Яндекс.Маркет"
              classesCard="bg-[#FFFFFF] border-[#333333] w-[170px] border-3 rounded-xl shadow-innerMax"
              classesHat="bg-[#FC3C18] rounded-t-lg h-[37px] border-b-2 border-black text-center"
              classesHatText="text-white text-xl p-1 font-semibold"
              icon=""
              classesBaseIcons="h-0"
              classesMainDiv="h-[75px] flex justify-center mt-3"
              classesIcon=""
              classesMainText="text-6xl text-black font-semibold"
              views="100"
            />
            <Panel
              label="Ozon"
              style="
                background: linear-gradient(
                  to bottom right,
                  #005cff 75%,
                  #f91155 75%
                );
              "
              classesCard="border-[#333333] w-[170px] border-2 shadow-innerMax rounded-xl"
              classesHat=" rounded-t-lg h-[37px] border-b-2 border-black text-center"
              classesHatText="text-white text-3xl -p-1   font-semibold"
              icon=""
              classesBaseIcons="h-0"
              classesMainDiv="h-[75px] flex justify-center mt-3"
              classesIcon=""
              classesMainText="text-6xl font-semibold text-white"
              views="100"
            />
            <Panel
              label="Undefinded"
              classesCard="bg-[#E5102A] border-[#333333] w-[170px] border-3 rounded-xl shadow-innerMax"
              classesHat="rounded-t-lg h-[37px] border-b-2 border-black text-center"
              classesHatText="text-[#FFFFFF] text-xl p-1 font-semibold"
              icon=""
              classesBaseIcons="h-0"
              classesMainDiv="h-[75px] flex justify-center mt-3"
              classesIcon=""
              classesMainText="text-6xl text-white font-semibold"
              views="100"
            />
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="flex flex-col xl:flex-row ml-64 pt-20">
    <div class="w-full">
      <div class="w-auto p-[15px]"></div>
    </div>

    <div class="w-full">
      <div class="xl:p-1 p-2">
        <Table :postamats_list="allpostamats"> </Table>
      </div>
      <div class="flex justify-center w-auto mt-2 mb-4">
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
export default {
  components: {
    BarChart,
    Button,
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

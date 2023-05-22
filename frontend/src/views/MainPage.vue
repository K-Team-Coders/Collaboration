<template>
  <div>
    <div class="ml-1">
      <TheHeader />
    </div>
    <div class="flex flex-col xl:flex-row">
      <div class="xl:mt-4 xl:ml-4">
        <Filter />
        <div class="mt-2.5">
          <Button label="Применить" />
        </div>
      </div>
      <div class="w-full">
        <div class="ml-4">
          <div
            class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-3 gap-2 mt-3"
          >
            <Panel
              label="Всего постаматов"
              icon="box"
              :views="postamat_count"
            />
            <Panel
              label="Всего отзывов"
              icon="chat"
              :views="allpostamats.length"
            />
            <Panel label="Всего партнеров" icon="parther" views="3" />
          </div>
        </div>
        <div class="w-auto p-[15px]">
          <div class="flex shadow-cards border-idealRed border-5 rounded-lg">
            <Map :postamat_list="allpostamats"> </Map>
          </div>
          <div class="border-idealRed border-4 rounded-lg mt-4 shadow-cards">
            <RadarChartApex />
            <div class="grid grid-cols-3 px-3 pb-2 ml-4 justify-center">
              <Panel
                label="Яндекс.Маркет"
                classesCard="bg-[#FFFFFF] border-[#333333] w-[170px] border-3 rounded-xl shadow-cards"
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
                classesCard="border-[#333333] w-[170px] border-2 shadow-cards rounded-xl"
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
                classesCard="bg-[#E5102A] border-[#333333] w-[170px] border-3 rounded-xl shadow-xl"
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
          <div class="border-idealRed border-4 rounded-lg mt-4 shadow-cards">
            <BarChart />
            <div class="grid grid-cols-3 px-3 pb-2 ml-4 justify-center">
              <Panel
                label="Яндекс.Маркет"
                classesCard="bg-[#FFFFFF] border-[#333333] w-[170px] border-3 rounded-xl shadow-cards"
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
                classesCard="border-[#333333] w-[170px] border-2 shadow-cards rounded-xl"
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
                classesCard="bg-[#E5102A] border-[#333333] w-[170px] border-3 rounded-xl shadow-xl"
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

      <div class="w-full">
        <div class="xl:p-1 p-2">
          <Table :postamats_list="allpostamats"> </Table>
        </div>
        <div class="flex justify-center w-auto mt-2 mb-4">
          <DownloadButton label="Импорт в .xls" icon="document" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TheHeader from "@/components/TheHeader.vue";
import Panel from "@/components/Panel.vue";
import RadarChartApex from "@/components/charts/RadarChartApex.vue";
import { mapActions, mapGetters } from "vuex";
import Map from "@/components/Map.vue";
import Table from "@/components/Table.vue";
import DownloadButton from "@/components/DownloadButton.vue";
import Filter from "@/components/Filter.vue";
import Button from "@/components/Button.vue";
import BarChart from "@/components/charts/BarChart.vue";
export default {
  components: {
    RadarChartApex,
    BarChart,
    TheHeader,
    Button,
    Panel,
    Filter,
    Map,
    DownloadButton,
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

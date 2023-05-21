<template>
  <div>
    <div class="ml-1">
      <TheHeader />
    </div>
    <div class="flex flex-col xl:flex-row">
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
          <div class="flex border-idealRed border-5 rounded-lg">
            <Map :postamat_list="allpostamats"> </Map>
          </div>
        </div>
      </div>
      <div class="w-auto">
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
import TheFooter from "@/components/TheFooter.vue";
import Panel from "@/components/Panel.vue";
import { mapActions, mapGetters } from "vuex";
import Map from "@/components/Map.vue";
import Table from "@/components/Table.vue";
import DownloadButton from "@/components/DownloadButton.vue";
import Filter from "@/components/Filter.vue";
export default {
  components: {
    TheFooter,
    TheHeader,
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

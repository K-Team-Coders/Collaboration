<template>
  <div>
    <TheHeader />
    <div class="flex ml-3">
      <div class="">
        <div class="flex justify-start mt-3 gap-2">
          <Panel label="Всего постаматов" icon="box" :views="postamat_count" />
          <Panel
            label="Всего отзывов"
            icon="chat"
            :views="allpostamats.length"
          />
          <Panel label="Всего партнеров" icon="parther" views="3" />
        </div>
        <div class="w-full mt-1 mr-4">
          <div class="flex">
            <Table />
          </div>
          <div class="flex justify-start mr-2">
            <DownloadButton label="Импорт в .xls" icon="document" />
          </div>
        </div>
      </div>
      <div class="w-1/2">
        <div class="pl-2 mt-3">
          <Map :postamat_list="allpostamats" />
        </div>
      </div>
    </div>
    <div>
      <Filter />
    </div>
  </div>
</template>

<script>
import TheHeader from "@/components/TheHeader.vue";
import TheFooter from "@/components/TheFooter.vue";
import Panel from "@/components/Panel.vue";
import Map from "@/components/Map.vue";
import Table from "@/components/Table.vue";
import DownloadButton from "@/components/DownloadButton.vue";
import Filter from "@/components/Filter.vue";
import { mapActions, mapGetters } from "vuex";

export default {
  components: {
    TheFooter,
    TheHeader,
    Panel,
    Map,
    DownloadButton,
    Table,
    Filter,
  },
  data() {
    return {};
  },
  computed: {
    ...mapGetters(["allpostamats"]),
    postamat_count() {
      let adress_list = [];
      this.allpostamats.forEach((element) => adress_list.push(element.adress));
      console.log(adress_list);
      let unique_postamat_list = Array.from(new Set(adress_list));
      console.log(unique_postamat_list.length);
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

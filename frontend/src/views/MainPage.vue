<template>
  <div>
    <TheHeader />
    <div class="flex justify-center mt-5 gap-5">
      <Panel label="Всего постаматов" icon="box" views="222" />
      <Panel label="Всего отзывов" icon="chat" views="10000+" />
      <Panel label="Всего партнеров" icon="parther" views="25" />
    </div>
    <div class="flex justify-end mr-5">
      <DownloadButton label="Импорт в .xls" icon="document" />
    </div>
    <!-- <Table2 /> //Это мой, он красивее вроде :0 как -->
    <div class="flex justify-between items-start">
      <div class="w-[800px] pl-3 mt-3">
        <Map :postamat_list="allpostamats" />
      </div>
      <div class="w-[700px] mt-2 mr-3">
        <Table />
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
import Table2 from "@/components/Table2.vue";
import DownloadButton from "@/components/DownloadButton.vue";
export default {
  components: {
    TheFooter,
    TheHeader,
    Panel,
    Map,
    DownloadButton,
    Table2,
    Table,
  },
  data() {
    return {
      id: 2,
      usertext: "Все классно",
      grade: 5,
      adress: "",
      reviewdate: "2023-05-20T11:07:15.590Z",
      clusername: 1,
      article: "Пиво",
      seller: "БТК-Групп",
      latitude: 0,
      longtitude: 0,
    };
  },
  computed: {
    ...mapGetters(["allpostamats"]),
  },
  methods: {
    ...mapActions(["GET_ALLPOSTAMATS"]),
  },
  async created() {
    this.GET_ALLPOSTAMATS();
  },
};
</script>

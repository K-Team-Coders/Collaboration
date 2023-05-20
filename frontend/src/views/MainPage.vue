<template>
  <div>
    <TheHeader />
    <div class="flex">
      <Panel label="Всего постаматов" icon="box" views="222" />
      <Panel label="Всего отзывов" icon="chat" views="10000+" />
      <Panel label="Всего партнеров" icon="parther" views="25" />
    </div>
    <DownloadButton label="Импорт в .xls" icon="document"/>
    <div class="flex justify-center p-10">
      <Map :postamat_list="allpostamats"/>
    </div>
  </div>
</template>

<script>
import TheHeader from "@/components/TheHeader.vue";
import TheFooter from "@/components/TheFooter.vue";
import Panel from "@/components/Panel.vue";
import { mapActions, mapGetters } from "vuex";
import Map from "@/components/Map.vue";
import DownloadButton from "@/components/DownloadButton.vue";
export default {
  components: {
    TheFooter,
    TheHeader,
    Panel,
    Map,
    DownloadButton
  },
  data () {
    return{
      id: 2,
        usertext: 'Все классно',
        grade: 5,
        adress: '',
        reviewdate: '2023-05-20T11:07:15.590Z',
        clusername: 1,
        article: 'Пиво',
        seller: 'БТК-Групп',
        latitude: 0,
        longtitude: 0,
    }
  },
  computed: {
    ...mapGetters(["allpostamats"]),
  },
  methods: {
    ...mapActions([
      "GET_ALLPOSTAMATS",
    ])

  },
  async created(){
    this.GET_ALLPOSTAMATS()

  }
};
</script>

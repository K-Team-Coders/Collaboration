<template>
  <div>
    <TheHeader />
    <Panel />
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
export default {
  components: {
    TheFooter,
    TheHeader,
    Panel,
    Map,
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

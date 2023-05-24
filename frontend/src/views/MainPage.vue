<template>
  <div class="bg-[#E2E7EE]">
    <div class="fixed w-full z-30 shadow-cards">
      <TheHeader />
    </div>
    <TheSidebar/>
    <TheMainContent v-if="allpostamats != null" :allpostamats="allpostamats"/>
  </div>
</template>

<script>
import TheHeader from "@/components/TheHeader.vue";
import { mapActions, mapGetters } from "vuex";
import TheSidebar from "@/components/TheSidebar.vue";
import LoadingScreen from "@/components/LoadingScreen.vue"
import TheMainContent from '@/components/TheMainContent.vue';
export default {
  components: {
    TheHeader,
    TheSidebar,
    TheMainContent,
    LoadingScreen
  },
  computed:{
    ...mapGetters(["allpostamats"])
  },
  data(){
    return {
      isLoading: true
    }
  },
  methods: {
    ...mapActions(["GET_ALLPOSTAMATS"]),
  },
  async created() {
    this.GET_ALLPOSTAMATS();
  }}
</script>
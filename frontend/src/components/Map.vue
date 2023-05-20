<template>
  <yandex-map :coords="coords" :settings="settings" :zoom="5" >
    <ymap-marker v-for="item in postamat_list" :key="item.id"
      :coords="[item.longitude, item.latitude]" :markerId="item.id" :cluster-name="1"
    />
  </yandex-map>
</template>

<script>
import { yandexMap, ymapMarker } from "vue-yandex-maps";

const settings = {
  apiKey: "afad2baa-cde2-44e1-8d21-0e93b892a275",
  lang: "ru_RU",
  coordorder: "latlong",
  enterprise: false,
  version: "2.1",
};

export default {
  components: { yandexMap, ymapMarker },
  computed: {
    
  },
  data() {
    return {
      coords: [55.753215, 36.622504],
      settings: settings,
    }},
  props: {
    postamat_list: Array,
  }
 
}
</script>

<style>
.ymap-container {
  width: 100%;
  height: 100vh;
}
</style>

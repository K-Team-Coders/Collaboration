<template>
  <yandex-map :coords="coords" :settings="settings" :zoom="5">
    <ymap-marker
      v-for="item in postamat_list"
      :key="item.id"
      :coords="[item.longitude, item.latitude]"
      :markerId="item.id"
      :cluster-name="1"
      :balloon-template="balloonTemplate(item)"
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
  computed: {},
  data() {
    return {
      coords: [55.753215, 36.622504],
      settings: settings,
    };
  },
  props: {
    postamat_list: Array,
  },
  methods: {
    balloonTemplate(item) {
      return `
      <table class="w-full text-sm text-center text-black">
          <thead class="text-xs text-white bg-idealRed">
            <tr class="">
              <th class="px-2 py-2 border-black border-r-[0.5px]  hover:bg-[#E5102A]"">
                Адрес постамата
              </th>
              <th
                class="px-6 py-2 border-black border-r-[0.5px] hover:bg-[#E5102A]"
              >
                Отзыв
              </th>
              <th
                class="px-1 py-2  hover:bg-[#E5102A]"
              >
                Рейтинг
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              class="bg-slate-50 p-1 border-l-2 border-black hover:bg-gray-200"
            > 
              <td class=" text-xs p-2 border-1 text-gray-900 text-center">
                 ${item.adress}
              </td>
              <td class=" text-xs border-1  p-1 text-gray-900 text-center">
                 ${item.usertext}
              </td>
              <td class="text-xs p-1 border-1 text-gray-900 text-center">
                 ${item.mark}
              </td>
            </tr>
          </tbody>
        </table>
      `;
    },
  },
};
</script>

<style>
.ymap-container {
  width: 100%;
  height: 87vh;
}
</style>

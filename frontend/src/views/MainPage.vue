<template>
  <div>
    <TheHeader />
    <div class="flex">
      <Panel label="Всего постаматов" icon="box" views="222" />
      <Panel label="Всего отзывов" icon="chat" views="10000+" />
      <Panel label="Всего партнеров" icon="parther" views="25" />
    </div>
    <div class="flex justify-center p-10">
      <Map />
    </div>
  </div>
</template>

<script>
import TheHeader from "@/components/TheHeader.vue";
import TheFooter from "@/components/TheFooter.vue";
import Panel from "@/components/Panel.vue";
import Map from "@/components/Map.vue";
export default {
  components: {
    TheFooter,
    TheHeader,
    Panel,
    Map,
  },
};
</script>

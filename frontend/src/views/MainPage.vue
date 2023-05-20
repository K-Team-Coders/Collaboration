<template>
  <div>
    <TheHeader />
    <Panel />
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

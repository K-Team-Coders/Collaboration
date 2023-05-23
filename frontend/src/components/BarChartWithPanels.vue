<template>
  <div class="border-idealRed border-4 rounded-lg mt-4 shadow-cards">
    <BarChart />
    <div class="grid grid-cols-3 px-3 pb-2 ml-4 justify-center">
      <Panel
        label="Яндекс.Маркет"
        classesCard="bg-[#FFFFFF] border-[#333333] w-[170px] border-3 rounded-xl shadow-innerMax"
        classesHat="bg-[#FC3C18] rounded-t-lg h-[37px] border-b-2 border-black text-center"
        classesHatText="text-white text-xl p-1 font-semibold"
        icon=""
        classesBaseIcons="h-0"
        classesMainDiv="h-[75px] flex justify-center mt-3"
        classesIcon=""
        classesMainText="text-6xl text-black font-semibold"
        views="100"
      />
      <Panel
        label="Ozon"
        style="
          background: linear-gradient(
            to bottom right,
            #005cff 75%,
            #f91155 75%
          );
        "
        classesCard="border-[#333333] w-[170px] border-2 shadow-innerMax rounded-xl"
        classesHat=" rounded-t-lg h-[37px] border-b-2 border-black text-center"
        classesHatText="text-white text-3xl -p-1   font-semibold"
        icon=""
        classesBaseIcons="h-0"
        classesMainDiv="h-[75px] flex justify-center mt-3"
        classesIcon=""
        classesMainText="text-6xl font-semibold text-white"
        views="100"
      />
      <Panel
        label="Undefinded"
        classesCard="bg-[#E5102A] border-[#333333] w-[170px] border-3 rounded-xl shadow-innerMax"
        classesHat="rounded-t-lg h-[37px] border-b-2 border-black text-center"
        classesHatText="text-[#FFFFFF] text-xl p-1 font-semibold"
        icon=""
        classesBaseIcons="h-0"
        classesMainDiv="h-[75px] flex justify-center mt-3"
        classesIcon=""
        classesMainText="text-6xl text-white font-semibold"
        views="100"
      />
    </div>
  </div>
</template>
<script>
import Panel from "./Panel.vue";
import BarChart from "@/components/charts/BarChart.vue";
export default {
  components: {
    Panel,
    BarChart,
  },
};
</script>

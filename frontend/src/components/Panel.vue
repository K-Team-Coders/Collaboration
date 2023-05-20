<template>
  <div class="bg-idealRed w-[189px] h-[140px] mt-5 ml-2 shadow-3xl ">
    <div class="bg-[#E5102A] h-[33px] text-center">
      <p class="text-white text-base font-semibold tracking-wider pt-1">
        Всего постаматов
      </p>
    </div>
    <div class="w-full flex-row items-center text-center justify-center">
      <div class="h-8 flex justify-center">
        <BaseIcon name="x" class="w-22" />
      </div>
      <div class="h-12 flex justify-center ">
        <p class="text-white text-4xl">120</p>
      </div>
    </div>
  </div>
</template>

<script>
import BaseIcon from "./BaseIcon.vue";
export default {
  components: {
    BaseIcon,
  },
};
</script>

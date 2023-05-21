<template>
  <div class="bg-idealRed w-auto mr-3 xl:h-[140px] shadow-3xl rounded-lg">
    <div class="bg-[#E5102A] h-[37px] text-center rounded-t-lg">
      <p class="text-white text-lg font-semibold tracking-wider pt-1">
        {{ label }}
      </p>
    </div>
    <div class="w-full flex-row">
      <div class="h-8 flex justify-center pt-2">
        <BaseIcon :name="icon" class="text-white w-10 h-10"></BaseIcon>
      </div>
      <div class="h-12 flex justify-center mt-3">
        <p class="text-white font-semibold text-4xl">{{ views }}</p>
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
  props: {
    label: {
      type: String,
    },
    views: {
      type: Number,
    },
    icon: {
      type: String,
    },
  },
};
</script>

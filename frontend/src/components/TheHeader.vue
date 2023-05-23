<template>
  <header :class="classesHeader">
    <div class="">
    </div>
  </header>
</template>

<script>
import LogoMain from "./LogoMain.vue";
export default {
  components: {
    LogoMain,
  },
  data() {
    return {
      classesHeader: [
        "bg-[#2F3342]",
        "bg-opacity-100",
        "h-[70px]"
      ],
    };
  },
};
</script>

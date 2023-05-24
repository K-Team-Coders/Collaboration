<template>
  <header :class="classesHeader">
    <div>
      <HeaderTimeAndDate />
      <ButtonRoute />
    </div>
  </header>
</template>

<script>
import HeaderTimeAndDate from "./HeaderTimeAndDate.vue";
import ButtonRoute from "./ButtonRoute.vue";
export default {
  components: {
    HeaderTimeAndDate,
    ButtonRoute,
  },
  data() {
    return {
      classesHeader: ["bg-[#2F3342]", "bg-opacity-100", "h-[70px]"],
    };
  },
};
</script>

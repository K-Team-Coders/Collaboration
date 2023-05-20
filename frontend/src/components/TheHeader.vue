<template>
  <header class="flex w-full justify-between bg-white bg-opacity-95">
    <div class="w-1/4">
      <div class="flex w-64 bg-white mt-2 ml-2">
        <LogoMain />
        <p class="text-2xl ml-4 mt-[0.4rem] font-medium leading-5">
          Московский постамат
        </p>
      </div>
    </div>
  </header>
</template>

<script>
import LogoMain from "./LogoMain.vue";
export default {
  components: {
    LogoMain,
  },
  props:[]
};
</script>

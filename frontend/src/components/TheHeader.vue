<template>
  <header class="flex w-full justify-between bg-white bg-opacity-95">
    <div class="w-1/4">
      <div class="flex w-64 bg-white pl-4 items-center">
        <LogoMain />
        <p class="text-xl font-TT_Firs_Neue ml-4">Московский постамат</p>
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
};
</script>

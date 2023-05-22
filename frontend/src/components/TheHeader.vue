<template>
  <header :class="classesHeader">
    <div class="flex flex-col mt-2 xl:flex-row xl:w-1/4 2xl:items-end">
      <div class="xl:w-20 xl:mt-2 xl:ml-2">
        <LogoMain />
      </div>
      <div class="flex items-end">
        <p
          class="font-semibold tracking-widest xl:text-2xl xl:ml-3 xl:tracking-widest xl:font-normal xl:leading-5"
        >
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
  data() {
    return {
      classesHeader: [
        "flex",
        "justify-center",
        "xl:justify-start",
        "bg-white",
        "bg-opacity-95",
        "shadow-xl",
        "pb-[0.5rem]",
      ],
    };
  },
};
</script>

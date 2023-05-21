<template>
  <div
    class="w-auto items-center bg-idealRed mt-1 ml-2 shadow-3xl rounded-lg  hover:bg-[#E5102A]"
  >
    <div class="w-full h-full">
      <div class="flex w-full p-2 items-center">
        <p class="w-3/4 text-white text-xl font-semibold text-center">
          {{ label }}
        </p>
        <div class="flex justify-end mr-2 w-1/4">
          
        </div>
      </div>
    </div>
  </div>
</template>
<script>

export default {
  components: {
  },
  props: {
    label: {
      type: String,
    },
    icon: {
      type: String,
    },
  },
};
</script>

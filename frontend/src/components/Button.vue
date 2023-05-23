<template>
  <button class="bg-idealRed hover:bg-red-700 text-white font-bold w-64 h-10">
    <p class="mr-2">
      {{ label }}
    </p>
  </button>
</template>
<script>
export default {
  props: {
    label: {
      type: String,
    },
  },
};
</script>

<template>
  <button
    class="bg-idealRed hover:bg-red-700 text-white font-semibold py-1 px-4 rounded"
  >
    {{ label }}
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

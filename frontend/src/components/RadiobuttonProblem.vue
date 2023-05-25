<template>
  <div class="">
    <input
      id="problem-radio"
      type="radio"
      value=""
      name="problem-radio"
      class="w-4 h-4 text-idealRed bg-idealRed border-gray-300 focus:ring-red-500 focus:ring-2"
    />
    <label
      for="problem-radio"
      class="ml-1.5 font-medium text-gray-900 dark:text-gray-300"
      >{{ label }}</label
    >
  </div>
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

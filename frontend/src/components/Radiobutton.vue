<template>
  <div class="">
    <input
      id="red-radio"
      type="radio"
      value=""
      name="colored-radio"
      class="w-4 h-4 text-idealRed bg-idealRed border-gray-300 focus:ring-red-500 focus:ring-2"
    />
    <label
      for="red-radio"
      class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300"
      >{{ label }}</label
    >
  </div>
</template>
<script>
export default {
    props: {
        label: {
            type: String
        },
    },
}
</script>

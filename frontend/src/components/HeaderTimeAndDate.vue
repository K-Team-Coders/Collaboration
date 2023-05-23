<template>
  <div class="absolute right-10 top-5 text-white">
    {{ localeDate }} {{ localTime }}
  </div>
</template>

<script>
export default {
  data: () => ({
    date: 1580558031264,
  }),

  computed: {
    localeDate() {
      return new Date(this.date).toLocaleTimeString();
    },
  },

  created() {
    this.intervalId = setInterval(() => (this.date = Date.now()), 1000);
  },

  beforeDestroy() {
    if (this.intervalId) clearInterval(this.intervalId);
  },
};
</script>

<template>
  <div class="p-2">
    <div class="relative w-[700px] overflow-x-auto shadow-3xl rounded-lg">
      <div class="w-full text-sm text-left text-black">
        <table class="w-full text-sm text-left text-black">
          <thead class="text-xs text-white bg-idealRed uppercase">
            <tr>
              <th class="px-6 py-3 hover:bg-[#E5102A]" @click="sortBy('name')">
                Адрес постамата
              </th>
              <th
                class="px-6 py-3 hover:bg-[#E5102A]"
                @click="sortBy('review')"
              >
                Количество отзывов
              </th>
              <th
                class="px-6 py-3 hover:bg-[#E5102A]"
                @click="sortBy('rating')"
              >
                Рейтинг
              </th>
              <th
                class="px-6 py-3 hover:bg-[#E5102A]"
                @click="sortBy('problem')"
              >
                Категория проблемы
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              class="bg-slate-50 border-b border-gray-700 hover:bg-gray-200"
              v-for="item in sortedItems"
              :key="item.id"
            >
              <td class="px-6 py-4 font-medium text-gray-900 text-center">
                {{ item.adress }}
              </td>
              <td class="px-6 py-4 font-medium text-gray-900 text-center">
                {{ item.review }}
              </td>
              <td class="px-6 py-4 font-medium text-gray-900 text-center">
                {{ item.rating }}
              </td>
              <td class="px-6 py-4 font-medium text-gray-900 text-center">
                {{ item.problem }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          adress: "Проспект Королева 62",
          review: "10000",
          rating: "4",
          problem: "Лол",
        },
        {
          adress: "русновка",
          review: "10234",
          rating: "1020",
          problem: "Л123124",
        },
      ],
      sortKey: "",
      sortOrders: {
        name: 1,
        price: 1,
      },
    };
  },
  computed: {
    sortedItems() {
      const order = this.sortOrders[this.sortKey] || 1;
      return this.items.slice().sort((a, b) => {
        if (a[this.sortKey] < b[this.sortKey]) {
          return -1 * order;
        }
        if (a[this.sortKey] > b[this.sortKey]) {
          return 1 * order;
        }
        return 0;
      });
    },
  },
  methods: {
    sortBy(key) {
      this.sortKey = key;
      this.sortOrders[key] = this.sortOrders[key] * -1;
    },
  },
};
</script>

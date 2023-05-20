<template>
  <div class="p-2">
    <div class="relative w-[700px] overflow-x-auto shadow-3xl rounded-lg">
      <table class="w-full text-sm text-left text-black">
        <thead class="text-xs text-white bg-idealRed uppercase">
          <tr>
            <th scope="col" class="px-6 py-3 text-center">Адрес постамата</th>
            <th scope="col" class="px-6 py-3 text-center">
              Количество отзывов
            </th>
            <th scope="col" class="px-6 py-3 text-center">Рейтинг</th>
            <th scope="col" class="px-6 py-3 text-center">
              Категория проблемы
            </th>
          </tr>
        </thead>
        <tbody>
          <tr class="bg-slate-50 border-b border-gray-700 hover:bg-gray-200">
            <th
              scope="row"
              class="px-6 py-4 font-medium text-gray-900 text-center"
            >
              {{ adress }}
            </th>
            <td class="px-6 py-4 font-medium text-gray-900 text-center">
              {{ review }}
            </td>
            <td class="px-6 py-4 font-medium text-gray-900 text-center">
              {{ rating }}
            </td>
            <td class="px-6 py-4 font-medium text-gray-900 text-center">
              {{ problem }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
export default {
  props: ["adress", "review", "rating", "problem"],
};
</script>

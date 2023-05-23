<template>
  <div>
    <p class="text-lg font-bold tracking-wide ml-4 text-[#E2E7EE] mt-1">Проблема</p>
    <div id="v-model-multiple-checkboxes" class="ml-4 font-semibold text-[#E2E7EE] text-[14px]">
      <div class="">
        <input
          type="checkbox"
          id="no problem"
          class=""
          value="1"
          v-model="filter.checkedProblems"
        />
        <label class="ml-2" for="no problem">Проблем нет</label><br />
      </div>
      <div class="">
        <input
          type="checkbox"
          id="product"
          value="2"
          v-model="filter.checkedProblems"
        />
        <label class="ml-2" for="product">Проблема с товаром</label><br />
      </div>
      <div class="">
        <input
          type="checkbox"
          id="deliver"
          value="3"
          v-model="filter.checkedProblems"
        />
        <label class="ml-2" for="deliver">Проблема с доставкой</label><br />
      </div>
      <div class="">
        <input
          type="checkbox"
          id="postamat"
          value="4"
          v-model="filter.checkedProblems"
        />
        <label class="ml-2" for="postamat">Проблема с постаматом</label><br />
      </div>
      <div class="">
        <input
          type="checkbox"
          id="date"
          value="5"
          v-model="filter.checkedProblems"
        />
        <label class="ml-2" for="date">Проблема со сроками</label>
        <br />
      </div>

      <p class="text-lg font-bold tracking-wide text-[#E2E7EE] mt-1">Рейтинг</p>
      <div id="v-model-multiple-checkboxes" class="font-semibold">
        <div class="flex items-center">
          <input
            class=""
            type="checkbox"
            id="5"
            value="5"
            v-model="filter.checkedRating"
          />
          <label class="flex items-center ml-2" for="5"
            >5 <span class="text-[0.7rem] ml-0.5"></span> </label
          ><br />
        </div>
        <div class="flex items-center">
          <input
            type="checkbox"
            id="4"
            value="4"
            v-model="filter.checkedRating"
          />
          <label class="flex items-center ml-2" for="4"
            >4 <span class="text-[0.7rem] ml-0.5"></span></label
          ><br />
        </div>
        <div class="flex items-center">
          <input
            type="checkbox"
            id="3"
            value="3"
            v-model="filter.checkedRating"
          />
          <label class="flex items-center ml-2" for="3"
            >3 <span class="text-[0.7rem] ml-0.5"></span></label
          ><br />
        </div>
        <div class="flex items-center">
          <input
            type="checkbox"
            id="2"
            value="2"
            v-model="filter.checkedRating"
          />
          <label class="flex items-center ml-2" for="2"
            >2 <span class="text-[0.7rem] ml-0.5"></span></label
          ><br />
        </div>
        <div class="flex items-center">
          <input
            type="checkbox"
            id="1"
            value="1"
            v-model="filter.checkedRating"
          />
          <label class="flex items-center ml-2" for="1"
            >1 <span class="text-[0.7rem] ml-0.5"></span></label
          ><br />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      filter: {
        checkedProblems: [],
        checkedRating: [],
        selectedDate: [
          new Date(),
          new Date(new Date().getTime() + 9 * 24 * 60 * 60 * 1000),
        ],
      },
    };
  },
};
</script>

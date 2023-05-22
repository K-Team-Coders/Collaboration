<template>
  <div>
    <Datepicker
      range
      class="Datepicker"
      placeholder="Выберите период"
      show-clear-button
      v-model="filter.selectedDate"
      lang="ru"
    />
    <p class="text-lg font-semibold mt-2 mb-1">Фильтры</p>
    <p class="text-lg font-bold tracking-wide ml-2 mb-1">Проблема</p>
    <div id="v-model-multiple-checkboxes" class="">
      <div class="ml-2">
        <input
          type="checkbox"
          id="no problem"
          class=""
          value="1"
          v-model="filter.checkedProblems"
        />
        <label class="ml-2" for="no problem">Проблем нет</label><br />
      </div>
      <div class="ml-2">
        <input
          type="checkbox"
          id="product"
          value="2"
          v-model="filter.checkedProblems"
        />
        <label class="ml-2" for="product">Проблема с товаром</label><br />
      </div>
      <div class="ml-2">
        <input
          type="checkbox"
          id="deliver"
          value="3"
          v-model="filter.checkedProblems"
        />
        <label class="ml-2" for="deliver">Проблема с доставкой</label><br />
      </div>
      <div class="ml-2">
        <input
          type="checkbox"
          id="postamat"
          value="4"
          v-model="filter.checkedProblems"
        />
        <label class="ml-2" for="postamat">Проблема с постаматом</label><br />
      </div>
      <div class="ml-2">
        <input
          type="checkbox"
          id="date"
          value="5"
          v-model="filter.checkedProblems"
        />
        <label class="ml-2" for="date">Проблема со сроками</label>
        <br />
      </div>

      <p class="font-bold text-lg tracking-wide p-2">Рейтинг</p>
      <div id="v-model-multiple-checkboxes">
        <div class="flex items-center ml-2">
          <input
            class=""
            type="checkbox"
            id="5"
            value="5"
            v-model="filter.checkedRating"
          />
          <label class="flex items-center ml-2" for="5"
            >5 <span class="text-[0.7rem] ml-0.5">⭐⭐⭐⭐⭐</span> </label
          ><br />
        </div>
        <div class="flex items-center ml-2">
          <input
            type="checkbox"
            id="4"
            value="4"
            v-model="filter.checkedRating"
          />
          <label class="flex items-center ml-2" for="4"
            >4 <span class="text-[0.7rem] ml-0.5">⭐⭐⭐⭐</span></label
          ><br />
        </div>
        <div class="flex items-center ml-2">
          <input
            type="checkbox"
            id="3"
            value="3"
            v-model="filter.checkedRating"
          />
          <label class="flex items-center ml-2" for="3"
            >3 <span class="text-[0.7rem] ml-0.5">⭐⭐⭐</span></label
          ><br />
        </div>
        <div class="flex items-center ml-2">
          <input
            type="checkbox"
            id="2"
            value="2"
            v-model="filter.checkedRating"
          />
          <label class="flex items-center ml-2" for="2"
            >2 <span class="text-[0.7rem] ml-0.5">⭐⭐</span></label
          ><br />
        </div>
        <div class="flex items-center ml-2">
          <input
            type="checkbox"
            id="1"
            value="1"
            v-model="filter.checkedRating"
          />
          <label class="flex items-center ml-2" for="1"
            >1 <span class="text-[0.7rem] ml-0.5">⭐</span></label
          ><br />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import "vue-datepicker-ui/lib/vuedatepickerui.css";
import VueDatepickerUi from "vue-datepicker-ui";
export default {
  components: {
    Datepicker: VueDatepickerUi,
  },
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

<style>
.Datepicker {
  --v-calendar-picker-color: #2F3342;
  --v-calendar-input-bg-color: #FF1935;
  --v-calendar-select-bg-color: #FF1935;
  --v-calendar-border-color: #000000;
  --v-calendar-triangle-color: #000000;
  --v-calendar-shadow: 0 20px 30px 0 rgba(227, 227, 227, 0.2);
  --v-calendar-top-shadow: 3px -14px 30px 0px rgba(0, 0, 0, 0.2);
  --v-calendar-text-color: #ffffff;
  --v-calendar-action-color: #ffffff;
  --v-calendar-text-disabled-color: #7d7d7d9d;
  --v-calendar-view-button-color: #ffffff;
  --v-calendar-datepicker-icon-color: #ffffff;
  --v-calendar-datepicker-icon-size: 1.1rem;
  --v-calendar-active-bg-color: #ff193400;
  --v-calendar-active-text-color: #ffffff;
  --v-calendar-range-bg-color: #BFCADA;
  --v-calendar-view-button-font-weight: 00;
  --v-calendar-view-button-font-size: 1.1rem;
  --v-calendar-range-text-color: #ffffff;
  --v-calendar-range-radius: 100%;
  --v-calendar-day-hover-bg-color: #BFCADA;
  --v-calendar-day-width: 45px;
  --v-calendar-day-height: 45px;
  --v-calendar-day-font-size: 0.8rem;
  --v-calendar-day-font-weight: 500;
  --v-calendar-input-border: 1px solid #383e48;
  --v-calendar-input-text-color: #ffffff;
  --v-calendar-input-font-size: 0.9rem;
  --v-calendar-input-font-weight: 600;
  --v-calendar-content-radius: 6px;
  --v-calendar-day-name-font-size: 0.9rem;
  --v-calendar-day-name-font-weight: 600;
  --v-calendar-day-name-color: #ffffff;
  --v-calendar-year-font-size: 1.1rem;
  --v-calendar-year-color: #ffffff;
  --v-calendar-year-font-weight: 500;
  --v-calendar-input-bg-disable-color: rgb(0, 0, 0);
  --v-calendar-input-text-disable-color: #ffffff;
  --v-calendar-year-disabled-color: #ffffff;
  --v-calendar-year-disabled-bg-color: transparent;
  --v-calendar-year-padding: 10px;
  --v-calendar-year-border: none;
  --v-calendar-year-border-radius: none;
  --v-calendar-month-font-size: 1.1rem;
  --v-calendar-month-color: #b8b8b9;
  --v-calendar-month-font-weight: 500;
  --v-calendar-month-disabled-color: #b8b8b9;
  --v-calendar-month-disabled-bg-color: transparent;
  --v-calendar-month-padding: 8px;
  --v-calendar-month-border: none;
  --v-calendar-month-border-radius: none;
}
</style>

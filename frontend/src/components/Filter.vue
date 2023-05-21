<template>
<div>
    <h2>Фильтры</h2>
    <Datepicker range  show-clear-button v-model="filter.selectedDate" lang="ru"/>
    <span>Выбранная дата: {{ filter.selectedDate }}</span>
    <h3>Проблема</h3>
  <div id="v-model-multiple-checkboxes">
  <input type="checkbox" id="no problem" value="1" v-model="filter.checkedProblems" />
  <label for="no problem">Проблем нет</label>
  <input type="checkbox" id="product" value="2" v-model="filter.checkedProblems" />
  <label for="product">Проблема с товаром</label>
  <input type="checkbox" id="deliver" value="3" v-model="filter.checkedProblems" />
  <label for="deliver">Проблема с доставкой</label>
  <input type="checkbox" id="postamat" value="4" v-model="filter.checkedProblems" />
  <label for="postamat">Проблема с постаматом</label>
  <input type="checkbox" id="date" value="5" v-model="filter.checkedProblems" />
  <label for="date">Проблема со сроками</label>
  <br />
  <span>Выбранные проблемы: {{ filter.checkedProblems }}</span>
  <h3>Рейтинг</h3>
  <div id="v-model-multiple-checkboxes">
  <input type="checkbox" id="5" value="5" v-model="filter.checkedRating" />
  <label for="5">5</label>
  <input type="checkbox" id="4" value="4" v-model="filter.checkedRating" />
  <label for="4">4</label>
  <input type="checkbox" id="3" value="3" v-model="filter.checkedRating" />
  <label for="3">3</label>
  <input type="checkbox" id="2" value="2" v-model="filter.checkedRating" />
  <label for="2">2</label>
  <input type="checkbox" id="1" value="1" v-model="filter.checkedRating" />
  <label for="1">1</label>
  <br />
  <span>Выбранный рейтинг: {{ filter.checkedRating }}</span>
</div>
</div>
</div>
</template>

<script>
import 'vue-datepicker-ui/lib/vuedatepickerui.css';
  import VueDatepickerUi from 'vue-datepicker-ui';
export default {
    components: {
      Datepicker: VueDatepickerUi
    },
    data() {
    return {
        filter: {
            checkedProblems: [],
            checkedRating: [],
            selectedDate: [
        new Date(),
        new Date(new Date().getTime() + 9 * 24 * 60 * 60 * 1000)]
        }
      
      

    }
  }
}
</script>

<style>

</style>
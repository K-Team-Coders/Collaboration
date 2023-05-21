<template>
<div>
    <h2>Фильтры</h2>
    
    <h3>Проблема</h3>
  <div id="v-model-multiple-checkboxes">
  <input type="checkbox" id="no problem" value="Нет проблем" v-model="checkedProblems" />
  <label for="no problem">Проблем нет</label>
  <input type="checkbox" id="product" value="Проблема с товаром" v-model="checkedProblems" />
  <label for="product">Проблема с товаром</label>
  <input type="checkbox" id="deliver" value="Проблема с доставкой" v-model="checkedProblems" />
  <label for="deliver">Проблема с доставкой</label>
  <input type="checkbox" id="postamat" value="Проблема с постаматом" v-model="checkedProblems" />
  <label for="postamat">Проблема с постаматом</label>
  <input type="checkbox" id="date" value="Проблема со сроками" v-model="checkedProblems" />
  <label for="date">Проблема со сроками</label>
  <br />
  <span>Выбранные проблемы: {{ checkedProblems }}</span>
  <h3>Рейтинг</h3>
  <div id="v-model-multiple-checkboxes">
  <input type="checkbox" id="5" value="5" v-model="checkedRating" />
  <label for="5">5</label>
  <input type="checkbox" id="4" value="4" v-model="checkedRating" />
  <label for="4">4</label>
  <input type="checkbox" id="3" value="3" v-model="checkedRating" />
  <label for="3">3</label>
  <input type="checkbox" id="2" value="2" v-model="checkedRating" />
  <label for="2">2</label>
  <input type="checkbox" id="1" value="1" v-model="checkedRating" />
  <label for="1">1</label>
  <br />
  <span>Выбранный рейтинг: {{ checkedRating }}</span>
</div>
</div>
</div>
</template>

<script>

export default {
   
    data() {
    return {
      checkedProblems: [],
      checkedRating: [],

    }
  }
}
</script>

<style>

</style>
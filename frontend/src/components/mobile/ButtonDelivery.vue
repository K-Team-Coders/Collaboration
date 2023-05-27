<template>
  <div>
    <FrontEnd v-show="button_frontend"></FrontEnd>
    <div v-show="button_frontend == false">
      <header class="head">
        <img class="head_logo" src="../mobile/image/logo.svg" alt="логотип">
      </header>

      <RatingDelivery v-model="checkedRating" />
      <div class="checkbox_main">
        <ul>
          <li>
            <input class="inputcheck" id="checkbox4" type="checkbox" style="display: none;"
              value="Товар пришел не вовремя" v-model="checked" />
            <label class="checkbox" for="checkbox4">
              <span>
                <svg width="12px" height="10px" viewbox="0 0 12 10">
                  <polyline points="1.5 6 4.5 9 10.5 1"></polyline>
                </svg>
              </span>
              <span>Товар пришел не вовремя</span>
            </label>
          </li>
          <li>
            <input class="inputcheck" id="checkbox5" type="checkbox" style="display: none;"
              value="Товара не оказалось в ячейке" v-model="checked" />
            <label class="checkbox" for="checkbox5">
              <span>
                <svg width="12px" height="10px" viewbox="0 0 12 10">
                  <polyline points="1.5 6 4.5 9 10.5 1"></polyline>
                </svg>
              </span>
              <span>Товара не оказалось в ячейке</span>
            </label>
          </li>
        </ul>
      </div>
      <div class="input">
        <textarea class="input_comment" type="text" placeholder="Комментарий" v-model="checkedText"></textarea>
        <a>
          <button @click="button_frontend = true" class="button input_button" id="#">Отправить</button>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import RatingDelivery from '../RatingDelivery.vue';
import FrontEnd from './FrontEnd.vue';
export default {
  components: {
    RatingDelivery,
    FrontEnd
  },
  data() {
    return {
      checkedRating: null,
      checked: [],
      checkedText: ''
    }
  },
  methods: {
    async sendData() {
      const data = {
        checkedRating: this.checkedRating,
        checked: this.checked,
        checkedText: this.checkedText
      }
      await axios.post('http://localhost:8000/', data)
    }
  }
}
</script>

<template>
  <div>
    <FrontEnd v-show="button_frontend"></FrontEnd>
    <div v-show="button_frontend == false">
      <header class="head">
        <img class="head_logo" src="../mobile/image/logo.svg" alt="логотип">
      </header>


      <RatingMobile v-model="checkedRating" />
      <div class="input">
        <textarea class="input_comment" type="text" placeholder="Комментарий" v-model="checkedText"></textarea>
        <a>
          <button @click="button_frontend = true || sendData()" class="button input_button" id="11">Отправить</button>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import RatingMobile from '../RatingMobile.vue';
import FrontEnd from './FrontEnd.vue';
export default {
  components: {
    RatingMobile,
    FrontEnd
  },
  data() {
    return {
      checkedRating: null,
      checkedText: '',
      button_frontend: false,
    }
  },
  methods: {
    async sendData() {
      const data = {
        checkedRating: this.checkedRating,
        checkedText: this.checkedText
      }
      await axios.post('http://localhost:8000/', data)
    }
  }
}
</script>


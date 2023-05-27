<template>
    <div>
        <header class="head">
            <img class="head_logo" src="../mobile/image/logo.svg" alt="логотип">
        </header>

        <RatingArticle v-model="checkedRating" />
        <div class="input">
            <textarea class="input_comment" type="text" placeholder="Комментарий"></textarea>
            <a href="#">
                <button class="button input_button" id="#">Отправить</button>
            </a>
        </div>
    </div>
</template>

<script>
import RatingArticle from '../RatingArticle.vue'
export default {
  components: {
    RatingArticle
  },
  data () {
    return {
      checkedRating: null
    }
  },
  methods: {
    async sendData () {
      const data = {
        checkedRating: this.checkedRating
      }
      await axios.post('http://localhost:8000/', data)
    }
  }
}
</script>

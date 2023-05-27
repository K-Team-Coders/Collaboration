<template>
    <div>
        <FrontEnd v-show="button_frontend"></FrontEnd>
        <div v-show="button_frontend == false">
            <header class="head">
                <img class="head_logo" src="../mobile/image/logo.svg" alt="логотип">
            </header>

            <main class="main">
                <RatingPostamat v-model="checkedRating" />
                <div class="checkbox_main">
                    <ul>
                        <li>
                            <input class="inputcheck" id="checkbox1" type="checkbox" style="display: none;"
                                value="Постамат не открылся" v-model="checked" />
                            <label class="checkbox" for="checkbox1">
                                <span>
                                    <svg width="12px" height="10px" viewbox="0 0 12 10">
                                        <polyline points="1.5 6 4.5 9 10.5 1"></polyline>
                                    </svg>
                                </span>
                                <span>Постамат не открылся</span>
                            </label>
                        </li>
                        <li>
                            <input class="inputcheck" id="checkbox2" type="checkbox" style="display: none;"
                                value="Постамат не работает" v-model="checked" />
                            <label class="checkbox" for="checkbox2">
                                <span>
                                    <svg width="12px" height="10px" viewbox="0 0 12 10">
                                        <polyline points="1.5 6 4.5 9 10.5 1"></polyline>
                                    </svg>
                                </span>
                                <span>Постамат не работает</span>
                            </label>
                        </li>
                        <li>
                            <input class="inputcheck" id="checkbox3" type="checkbox" style="display: none;"
                                value="Постамат расположен неудобно" v-model="checked" />
                            <label class="checkbox" for="checkbox3">
                                <span>
                                    <svg width="12px" height="10px" viewbox="0 0 12 10">
                                        <polyline points="1.5 6 4.5 9 10.5 1"></polyline>
                                    </svg>
                                </span>
                                <span>Постамат расположен неудобно</span>
                            </label>
                        </li>
                    </ul>
                </div>
                <div class="input">
                    <textarea id="postarea" class="input_comment" type="text" placeholder="Комментарий"
                        v-model="checkedText"></textarea>
                    <a>
                        <button @click="button_frontend = true" class="button input_button" id="#">Отправить</button>
                    </a>
                </div>
            </main>
        </div>
    </div>
</template>

<script>
import RatingPostamat from '../RatingPostamat.vue';
import FrontEnd from './FrontEnd.vue';
export default {
    components: {
        RatingPostamat,
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

<style></style>
<template>
    <div>
        <header class="head">
            <img class="head_logo" src="../mobile/image/logo.svg" alt="логотип">
        </header>
        <main class="main">
            <div class="full-stars">
                <p>Как вам постамат?</p>
                <div class="rating-group">
                    <!-- по умолчанию 0 -->
                    <input name="rat" value="0" type="radio" disabled checked />

                    <!-- рейтинг 1 -->
                    <label for="rat-1">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
                            <path
                                d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z" />
                        </svg>
                    </label>
                    <input name="rat" id="rat-1" value="1" type="radio" />

                    <!-- рейтинг 2 -->
                    <label for="rat-2">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
                            <path
                                d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z" />
                        </svg>
                    </label>
                    <input name="rat" id="rat-2" value="2" type="radio" />

                    <!-- рейтинг 3 -->
                    <label for="rat-3">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
                            <path
                                d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z" />
                        </svg>
                    </label>
                    <input name="rat" id="rat-3" value="3" type="radio" />

                    <!-- рейтинг 4 -->
                    <label for="rat-4">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
                            <path
                                d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z" />
                        </svg>
                    </label>
                    <input name="rat" id="rat-4" value="4" type="radio" />

                    <!-- рейтинг 5 -->
                    <label for="rat-5">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
                            <path
                                d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z" />
                        </svg>
                    </label>
                    <input name="rat" id="rat-5" value="5" type="radio" />
                </div>
            </div>
            <div class="checkbox_main">
                <ul>
                    <li>
                        <input class="inputcheck" id="checkbox1" type="checkbox" style="display: none;" />
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
                        <input class="inputcheck" id="checkbox2" type="checkbox" style="display: none;" />
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
                        <input class="inputcheck" id="checkbox3" type="checkbox" style="display: none;" />
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
                <textarea class="input_comment" type="text" placeholder="Комментарий"></textarea>
                <a href="#">
                    <button class="button input_button" id="#">Отправить</button>
                </a>
            </div>
        </main>
    </div>
</template>

<script>
export default {

}
</script>

<style>

</style>
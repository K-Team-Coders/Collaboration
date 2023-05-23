<template>
    <div>
 <header class="head">
        <img class="head_logo" src="../mobile/image/logo.png" alt="логотип">
    </header>
    
    <div class="full-stars">
            <p>Как вам постамат?</p>
            <div class="rating-group">
                <!-- по умолчанию 0 -->
                <input name="fst" value="0" type="radio" disabled checked />

                <!-- рейтинг 1 -->
                <label for="fst-1">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
                        <path
                            d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z" />
                    </svg>
                </label>
                <input name="fst" id="fst-1" value="1" type="radio" />

                <!-- рейтинг 2 -->
                <label for="fst-2">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
                        <path
                            d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z" />
                    </svg>
                </label>
                <input name="fst" id="fst-2" value="2" type="radio" />

                <!-- рейтинг 3 -->
                <label for="fst-3">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
                        <path
                            d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z" />
                    </svg>
                </label>
                <input name="fst" id="fst-3" value="3" type="radio" />

                <!-- рейтинг 4 -->
                <label for="fst-4">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
                        <path
                            d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z" />
                    </svg>
                </label>
                <input name="fst" id="fst-4" value="4" type="radio" />

                <!-- рейтинг 5 -->
                <label for="fst-5">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
                        <path
                            d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z" />
                    </svg>
                </label>
                <input name="fst" id="fst-5" value="5" type="radio" />
            </div>
        </div>
        <div class="input">
            <textarea class="input_comment" type="text" placeholder="Комментарий"></textarea>
            <a href="#">
                <button class="button input_button" id="#">Отправить</button>
            </a>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style>
        p {
            font-family: TTFirsNeue-Regular;
        }

        .full-stars {
            box-sizing: border-box;
            width: 90%;
            max-width: 400px;
            margin: 0 auto;
            margin-bottom: 10px;
            text-align: start;
        }

        .full-stars .rating-group {
            display: inline-flex;
        }

        .full-stars input {
            position: absolute;
            left: -9999px;
        }

        .full-stars label {
            margin: 0;
            cursor: pointer;
        }

        .full-stars label svg {
            margin: 2px;
            height: 40px;
            width: 40px;
            fill: #ff1935;
            transition: fill 0.3s;
        }

        .full-stars input:checked~label svg {
            fill: #FFC5C5;
        }

        .full-stars .rating-group:hover label svg {
            fill: #ff1935;
        }

        .full-stars .rating-group input:hover~label svg {
            fill: #FFC5C5;
        }

        .input {
            width: 90%;
            max-width: 400px;
            margin: 0 auto;
            
        }

        .input_comment {
            box-sizing: border-box;
            display: block;
            min-width: 100%;
            max-width: 400px;
            height: calc(10rem + 2px);
            padding: 0.375rem 0.75rem;
            margin-bottom: 20px;
            font-family: inherit;
            font-size: 1rem;
            font-weight: 400;
            line-height: 1.5;
            color: #212529;
            background-color: #fff;
            background-clip: padding-box;
            border: 1px solid #bdbdbd;
            border-radius: 0.25rem;
            transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
        }

        .input_comment::placeholder {
            color: #212529;
            opacity: 0.4;
        }

        .input_comment:focus {
            color: #212529;
            background-color: #fff;
            border-color: #bdbdbd;
            outline: 0;
            box-shadow: 0 0 0 0.2rem rgba(158, 158, 158, 0.25);
        }

        .input_comment:disabled,
        .input_comment[readonly] {
            background-color: #f5f5f5;
            opacity: 1;
        }

        .input_button {
            box-sizing: border-box;
            width: 100%;
            max-width: 400px;
        }
</style>
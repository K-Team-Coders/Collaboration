<template>
<body>
    
    <PostamatMobileAllGood v-if="button_good == true" ></PostamatMobileAllGood>
    <header class="head">
        <img class="head_logo" src="../mobile/image/logo.png" alt="логотип">
    </header>
    <main class="main">
        <div class="main_box">
            <h1>Поделитесь своим<br> мнением и&nbsp;помогите нам<br> стать лучше!</h1>
            <img class="main_box--img" src="../mobile/image/1.svg" alt="иконка">
            <span>Возникали&nbsp;ли у&nbsp;вас проблемы<br> с&nbsp;получением заказа?</span>

            <a >
                <button  @click="button_good = true" class="button good-button" id="0">Все отлично!</button>
            </a>
            <a >
                <button  @click="v" class="button" id="1">С постаматом</button>
            </a>
            <a >
                <button  @click="" class="button" id="2">С доставкой</button>
            </a>
            <a >
                <button  @click="" class="button" id="3">С посылкой</button>
            </a>
        </div>
    </main>
</body>
</template>

<script>
import PostamatMobileAllGood from "../mobile/PostamatMobileAllGood.vue";
export default {
    components: {
    PostamatMobileAllGood,
  },
data(){
    return{
        button_good: false,

        mobile_data: {
            id: 0,
            date: 0,
            adress: 'Синявинская д.11, г. Москва.',
            classnumber: 0,
            clusternumber: 0,
            logitude: 55,
            latitude: 36,
            usertext: '',

        },
        visible: false,
    }
},
methods:{
    
}
}
</script>

<style>
@font-face {
    font-family: "TTFirsNeue-Regular";
    src: url("../mobile/fonts/TTFirsNeue-Regular.ttf");
}

@font-face {
    font-family: "../mobile/fonts/TTFirsNeue-Bold.ttf";
    src: url("");
}

body {
    margin: 0 auto;
    font-family: TTFirsNeue-Bold;
    text-align: center;
}

h1 {
    font-size: 22px;
}

span {
    color: #BFCADA;
    margin-bottom: 20px;
}

.head {
    display: flex;
    justify-content: center;
    margin: 20px 0;
}

.main_box {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.main_box--img {
    margin-bottom: 20px;
}

.button {
    width: 365px;
    height: 66px;
    padding: 10px;
    margin-bottom: 4px;

    font-family: TTFirsNeue-bold;
    font-size: 22px;

    background: #FF1935;
    color: #f1f1f1;
    border-radius: 8px;
    border: none;
    box-shadow: inset 0px 4px 6px -2px rgba(0, 0, 0, 0.4);
    cursor: pointer;
}


.good-button {
    margin-bottom: 16px;
    background: #E2E7EE;
    color: #ff1935;
}
</style>
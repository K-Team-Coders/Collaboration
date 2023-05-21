<template>
    <div>
        <div class="w-full h-full">
            <div class="flex w-full p-2 items-center">
                <p class="w-3/4 text-black text-xl font-semibold text-center">
                    Отзыв: {{ get_review }}
                </p>
                <div class="flex justify-end mr-2 ">
                </div>
            </div>
        </div>
        <div class="demo">
            <Button label="1 - все ок" />
            <Button label="2 - проблема с товаром" />
            <Button label="3 - проблема с доставкой" />
            <Button label="4 - проблема с постаматом" />
            <Button label="5 - проблема со сроками" />
        </div>
    </div>
</template>

<script>
import Button from "@/components/Button.vue";
import axios from "axios";
export default {
    components: { Button },
    data() {
        return {
            choosed_class: 0,
            get_review: '',
        }
    },
    methods:{
        clicked(){
            
        }
    },
    mounted(){
        ax
    }
}
</script>

<style>
.demo {
    font-family: sans-serif;
    border: 1px solid #eee;
    border-radius: 2px;
    padding: 20px 30px;
    margin-top: 1em;
    margin-bottom: 40px;
    user-select: none;
    overflow-x: auto;
}
</style>
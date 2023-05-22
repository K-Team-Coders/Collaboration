<template>
  <div>
    <div class="flex w-full h-full">
      <div class="flex flex-col  w-full justify-center items-center">
        <p class="font-bold text-3xl p-4">Отзыв</p>
        <p class="text-black text-2xl w-3/5 font-base text-center">
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Odio id ea
          nobis maxime. Minima alias ratione tenetur perferendis nihil sapiente
          voluptates eos dolorem, aut nobis aperiam natus nam quaerat optio?
          {{ get_review }}
        </p>
      </div>
    </div>
    <div class="demo">
      <div class="flex gap-2 justify-center">
        <Button label="1 - все ок" />
        <Button label="2 - проблема с товаром" />
        <Button label="3 - проблема с доставкой" />
        <Button label="4 - проблема с постаматом" />
        <Button label="5 - проблема со сроками" />
      </div>
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
      get_review: "",
    };
  },
  methods: {
    clicked() {},
  },
  mounted() {
    ax;
  },
};
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

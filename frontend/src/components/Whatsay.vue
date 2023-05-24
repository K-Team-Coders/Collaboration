<template>
  <div class="external-svg">
    <div class="min-h-screen bg-no-repeat font-TT_Firs_Neue_Regular">
      <section class="pt-60 ml-20 text-[#E2E7EE]">
        <div class="flex justify-start">
          <div class="w-2/5">
            <div class="flex flex-col gap-2">
              <p class="text-5xl font-TT_Firs_Neue_Bold uppercase">
                Вот что я скажу!
              </p>
              <p class="font-medium text-lg">
                Нам важно услышать Ваше мнение о нас.
              </p>
              <div class="border-b-[3px] border-[#E2E7EE]"></div>
            </div>
            <div class="flex flex-col pt-3 w-full">
              <input
                type="text"
                v-model="isActive"
                placeholder="Пожалуйста, введите уникальный код"
                useautocomplete="off"
                class="border-[#E2E7EE] border-[1.5px] w-full px-4 text-xl overflow-x-hidden text-left py-1 rounded-lg focus:outline-none focus:border-idealRed focus:border-[1.5px] focus:shadow-innerMax text-black"
              />
              <p class="py-2.5 tracking-tighter font-medium">
                Где я могу найти номер заказа?
              </p>
              <transition
                enter-active-class="duration-300"
                enter-from-class="opacity-0"
                enter-to-class="opacity-100"
                leave-active-class="duration-300"
                leave-from-class="opacity-100"
                leave-to-class="opacity-0"
              >
                <input
                  v-show="isActive.length > 0"
                  v-model="usertext"
                  type="text"
                  placeholder="Оставьте отзыв"
                  useautocomplete="off"
                  class="border-[#E2E7EE] border-[1.5px] mb-2.5 w-full px-4 text-xl overflow-x-hidden text-left py-1 rounded-lg focus:outline-none focus:border-idealRed focus:border-[1.5px] focus:shadow-innerMax text-black"
                />
              </transition>

              <div>
                <Radiobutton
                  v-for="label in items"
                  :key="label"
                  :label="label.massage"
                />
              </div>
            </div>
            <button
              class="bg-idealRed w-full rounded-lg py-3 text-xl font-TT_Firs_Neue_Bold text-uppercase mt-3"
            >
              Отправить отзыв
            </button>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import Radiobutton from "./Radiobutton.vue";
export default {
  components: {
    Radiobutton,
  },
  data() {
    return {
      isActive: "",
      usertext: "",
      items: [
        { massage: "Проблем нет" },
        { massage: "Проблем с товаром" },
        { massage: "Проблем с доставкой" },
        { massage: "Проблем нет" },
        { massage: "Проблем нет" },
      ],
    };
  },
};
</script>
<style>
.external-svg {
  background: url(../image/yandexqq.svg) no-repeat center center fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}
</style>

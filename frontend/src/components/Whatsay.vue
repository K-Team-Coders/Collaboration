<template>
  <div class="external-svg">
    <div class="min-h-screen bg-no-repeat font-TT_Firs_Neue_Regular">
      <section class="pt-60 ml-20 text-[#E2E7EE]">
        <div class="flex justify-start">
          <div class="w-2/5">
            <div class="flex flex-col gap-4">
              <p class="text-5xl font-TT_Firs_Neue_Bold uppercase">
                Вот что я скажу!
              </p>
              <p class="font-medium text-lg">
                Нам важно услышать Ваше мнение о нас.
              </p>
              <div class="border-b-[3px] border-[#E2E7EE]"></div>
            </div>
            <div class="pt-4 w-full">
              <input
                type="text"
                placeholder="Пожалуйста, введите уникальный код, указанный на Вашем чеке"
                useautocomplete="off"
                class="border-[#E2E7EE] border-[1.5px] w-full max-w-[500px] px-4 text-[14px] overflow-x-hidden text-center py-3 rounded-l-lg focus:outline-none"
              />
              <p class="py-2.5 tracking-tighter font-medium">
                Где я могу найти код?
              </p>
              <div class="flex items-center">
                <input type="checkbox" class="w-3 h-3" />
                <label class="text-sm ml-3 w-[700px] font-medium leading-5"
                  >Настоящим Вы подтверждаете, что Вам исполнилось 18 лет и Вы
                  являетесь полностью дееспособным лицом.
                </label>
              </div>
              <div class="flex items-center mt-1">
                <input type="checkbox" class="w-3 h-3 mt-[2px]" />
                <label class="text-sm ml-3 w-[700px] font-medium leading-5"
                  >Я согласен на обработку моих персональных данных</label
                >
              </div>
            </div>
            <button
              class="bg-[#696969] w-full rounded-lg py-3 text-xl tracking-tighter text-uppercase mt-3"
            >
              Начать опрос
            </button>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>
<style>
.external-svg {
  background: url(../img/yandexqq.svg) no-repeat center center fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}
</style>

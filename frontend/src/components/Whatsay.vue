<template>
  <div class="">
    <section class="pt-[200px] -ml-[380px]">
      <div class="flex justify-center">
        <div class="w-2/5">
          <div class="flex flex-col gap-4">
            <p class="font-semibold text-5xl uppercase">Вот что я скажу!</p>
            <p class="font-medium text-lg">
              Нам важно услышать Ваше мнение о нас.
            </p>
            <div class="border-b-[3px] border-black"></div>
          </div>
          <div class="pt-4 w-full">
            <input
              type="text"
              placeholder="Пожалуйста, введите уникальный код, указанный на Вашем чеке"
              useautocomplete="off"
              class="border-[#232323] border-[1.5px] w-full max-w-[500px] px-4 text-[14px] overflow-x-hidden text-center py-3 rounded-l-lg"
            />
            <p class="py-1 tracking-tighter font-medium">Где я могу найти код?</p>
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
          <button class="bg-[#696969] w-full rounded-lg py-3 text-xl tracking-tighter text-uppercase mt-3">
            Начать опрос
          </button>
        </div>
      </div>
    </section>
  </div>
</template>

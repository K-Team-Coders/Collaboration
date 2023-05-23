<template>
  <aside :class="classes">
    <div class="">
      <LogoMain />
      <div class="mt-4">
        <SidebarNavItem label="Карта" icon="dashboard" />
        <SidebarNavItem label="Статистика" icon="x" is-active />
        <SidebarNavItem label="Кластерный анализ" icon="microphone" />
        <SidebarNavItem label="Классифик. анализ" icon="box" />
      </div>
      <div class="ml-4 mt-3">
        <p class="text-[#E2E7EE] font-bold text-lg">Выберите дату</p>
      </div>
      <div class="mt-2">
        <DatePickerMain />
      </div>
      <Filter />
      <div class="absolute left-0 bottom-0">
        <Button label="Применить" />
      </div>
    </div>
  </aside>
</template>

<script>
import Filter from "./Filter.vue";
import Button from "./Button.vue";
import LogoMain from "./LogoMain.vue";
import SidebarNavItem from "./SidebarNavItem.vue";
import DatePickerMain from "./DatePickerMain.vue";
import SidebarSection from "./SidebarSection.vue";
export default {
  components: {
    Filter,
    Button,
    LogoMain,
    SidebarNavItem,
    DatePickerMain,
    SidebarSection,
  },

  computed: {
    classes() {
      return ["w-64", "fixed", "top-0", "bg-[#2F3342]", "z-50", "h-screen"];
    },
  },
};
</script>

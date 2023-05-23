<template>
  <aside :class="classes">
    <div class="">
      <LogoMain />
      <div class="mt-4">
        <SidebarNavItem label="Карта" icon="dashboard" />
        <SidebarNavItem label="Статистика" icon="x" is-active />
        <SidebarNavItem label="Кластерный анализ" icon="microphone" />
        <SidebarNavItem label="Классификационный анализ" icon="box" />
      </div>
      <Filter />
      <div class="ml-6 mt-2">
        <p class="text-[#E2E7EE] font-bold">Выберите дату:</p>
      </div>
      <DatePickerMain />
      <div class="ml-6 mt-3">
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

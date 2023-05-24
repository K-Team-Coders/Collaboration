<template>
  <aside :class="classes">
    <div class="">
      <LogoMain />
      <div class="mt-2.5">
        <SidebarNavItem
          v-for="(navItem, index) in navItems"
          :key="index"
          :is-active.sync="activeIndex === index"
          @update:isActive="
            (value) => {
              activeIndex = value ? index : -1;
              $emit('updateActiveIndex', activeIndex);
            }
          "
          :label="navItem.label"
          :icon="navItem.icon"
        />
      </div>
      <div class="ml-4">
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
import { provide } from "vue";
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
  data() {
    return {
      activeIndex: 0,
      navItems: [
        { label: "Карта", icon: "map" },
        { label: "Кластерный анализ", icon: "dashboard" },
        { label: "Таблица", icon: "table" },
        { label: "Клас. анализ", icon: "box" },
      ],
    };
  },
  created() {
    provide("activeIndex", this.activeIndex);
  },
};
</script>

<template>
  <li class="">
    <p href="#" :class="classes">
      <BaseIcon :name="icon" :class="iconClasses" />
      <span>{{ label }}</span>
    </p>
  </li>
</template>

<script>
import BaseIcon from "./BaseIcon.vue";
export default {
  components: {
    BaseIcon,
  },
  props: {
    label: String,
    icon: String,
    isActive: Boolean,
  },
  computed: {
    classes() {
      const classes = [
        "flex",
        "items-center",
        "px-6",
        "py-2",
        "text-sm",
        "text-[#E2E7EE]",
      ];
      return this.isActive
        ? [
            ...classes,
            "font-semibold",
            "text-white",
            "bg-idealRed",
            "shadow-3xl",
          ]
        : [...classes, "hover:shadow-innerMax"];
    },
    iconClasses() {
      return this.isActive
        ? "w-6 h-6 mr-6 text-white"
        : "w-6 h-6 mr-6 text-white";
    },
  },
};
</script>

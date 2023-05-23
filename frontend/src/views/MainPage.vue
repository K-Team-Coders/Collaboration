<template>
  <div class="bg-[#E2E7EE]">
    <div class="fixed w-full z-30 shadow-cards">
      <TheHeader />
    </div>
    <TheSidebar/>
    <TheMainContent />
  </div>
</template>

<script>
import TheHeader from "@/components/TheHeader.vue";
import TheSidebar from "@/components/TheSidebar.vue";
import TheMainContent from '@/components/TheMainContent.vue';
export default {
  components: {
    TheHeader,
    TheSidebar,
    TheMainContent
  },
}
</script>
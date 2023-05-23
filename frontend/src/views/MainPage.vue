<template>
  <div>
    <div class="fixed w-full z-30">
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
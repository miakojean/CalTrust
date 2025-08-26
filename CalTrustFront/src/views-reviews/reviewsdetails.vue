<template>
  <main>
    <newNavbar />
    <reviewdetailSection />
    <footerSection />
  </main>
</template>

<script>
import newNavbar from '@/layout/newNavbar.vue';
import footerSection from '@/layout/footerSection.vue';
import reviewdetailSection from './reviewdetailSection.vue';
export default {
  components: {
    newNavbar,
    footerSection,
    reviewdetailSection
  }
}
</script>

<style scoped>

</style>

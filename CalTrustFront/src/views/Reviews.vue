<template>
  <main>
    <NewNavbar/>
    <ctaReviewSection/>
    <footerSection/>
  </main>
</template>


<script>
import NewNavbar from '@/layout/newNavbar.vue';
import ctaReviewSection from '@/section/ctaReviewSection.vue';
import footerSection from '@/layout/footerSection.vue';

export default {
  components:{
    NewNavbar,
    ctaReviewSection,
    footerSection
  }
}
</script>
<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>

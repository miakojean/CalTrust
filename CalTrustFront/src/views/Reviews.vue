<template>
  <main>
    <NewNavbar/>
    <ctaReviewSection/>
    <reviewstestimonials/>
    <footerSection/>
  </main>
</template>


<script>
import NewNavbar from '@/layout/newNavbar.vue';
import ctaReviewSection from '@/section/ctaReviewSection.vue';
import reviewstestimonials from '@/section/reviewsTestimonials.vue';
import footerSection from '@/layout/footerSection.vue';

export default {
  components:{
    NewNavbar,
    ctaReviewSection,
    reviewstestimonials,
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

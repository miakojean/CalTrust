<template>
  <main>
    <NewNavbar/>
    <ctaReviewSection/>
    <companieSection/>
    <footerSection/>
  </main>
</template>


<script>
import NewNavbar from '@/layout/newNavbar.vue';
import ctaReviewSection from '@/section/ctaReviewSection.vue';
import reviewstestimonials from '@/section/reviewsTestimonials.vue';
import companieSection from '@/views-companies/CompanySections/companieSection.vue';
import footerSection from '@/layout/footerSection.vue';

export default {
  components:{
    NewNavbar,
    ctaReviewSection,
    companieSection,
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


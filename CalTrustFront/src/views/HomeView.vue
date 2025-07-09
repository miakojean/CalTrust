<template>
  <main>
    <navbar/>
    <ctaSection></ctaSection>
    <featureSection/>
    <testimonials/>
    <firmsSection/>
  </main>
</template>

<script>
import navbar from '@/layout/navbar.vue';
import ctaSection from '@/section/ctaSection.vue';
import featureSection from '@/section/featureSection.vue';
import testimonials from '@/section/testimonials.vue';
import firmsSection from '@/section/firmsSection.vue';
export default {
    components:{
      navbar,
      ctaSection,
      featureSection,
      testimonials,
      firmsSection
    },

    setup(){
        
    }
}
</script>

<style>

</style>
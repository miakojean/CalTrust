<template>
  <main>
    <navbar/>
    <ctaSection></ctaSection>
    <stepper/>
    <featureSection/>
    <testimonials/>
    <firmsSection/>
    <stepper title="Améliorer certains biens et services"/>
    <footerSection/>
  </main>
</template>

<script>
import navbar from '@/layout/navbar.vue';
import newNavbar from '@/layout/newNavbar.vue';
import ctaSection from '@/section/ctaSection.vue';
import featureSection from '@/section/featureSection.vue';
import testimonials from '@/section/testimonials.vue';
import firmsSection from '@/section/firmsSection.vue';
import stepper from '@/components/cards/stepper.vue';
import footerSection from '@/layout/footerSection.vue';
export default {
    components:{
      navbar,
      newNavbar,
      ctaSection,
      featureSection,
      testimonials,
      firmsSection,
      stepper,
      footerSection
    },

    setup(){
        
    }
}
</script>

<style>

</style>
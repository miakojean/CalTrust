<template>
  <main>
    <navbar/>
    <ctaSection></ctaSection>
    <stepper/>
    <featureSection/>
    <testimonials/>
    <stepper title="Améliorer certains biens et services"/>
    <firmsSection/>
  </main>
</template>

<script>
import navbar from '@/layout/navbar.vue';
import ctaSection from '@/section/ctaSection.vue';
import featureSection from '@/section/featureSection.vue';
import testimonials from '@/section/testimonials.vue';
import firmsSection from '@/section/firmsSection.vue';
import stepper from '@/components/cards/stepper.vue';
export default {
    components:{
      navbar,
      ctaSection,
      featureSection,
      testimonials,
      firmsSection,
      stepper
    },

    setup(){
        
    }
}
</script>

<style>

</style>
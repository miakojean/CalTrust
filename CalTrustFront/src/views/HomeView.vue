<template>
  <main>
    <navbar/>
    <ctaSection></ctaSection>
    <featureSection/>
  </main>
</template>

<script>
import navbar from '@/layout/navbar.vue';
import ctaSection from '@/section/ctaSection.vue';
import featureSection from '@/section/featureSection.vue';
export default {
    components:{
      navbar,
      ctaSection,
      featureSection
    },

    setup(){
        
    }
}
</script>

<style>

</style>
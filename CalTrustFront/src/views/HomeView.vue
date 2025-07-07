<template>
  <main>
    <navbar/>
    <ctaSection></ctaSection>
  </main>
</template>

<script>
import navbar from '@/layout/navbar.vue';
import ctaSection from '@/section/ctaSection.vue';
export default {
    components:{
      navbar,
      ctaSection
    },

    setup(){
        
    }
}
</script>

<style>

</style>
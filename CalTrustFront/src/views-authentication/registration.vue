<template>
  <main>
    <newNavbar/>
    <registrationSection/>
    <footerSection/>
  </main>
</template>

<script>
import newNavbar from '@/layout/newNavbar.vue';
import registrationSection from './registrationSection.vue';
import footerSection from '@/layout/footerSection.vue';
export default {
    components:{
        newNavbar, registrationSection, footerSection
    }
}
</script>

<style>

</style>
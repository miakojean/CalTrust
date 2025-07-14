<template>
  <main>
    <newNavbar/>
    <loginSection/>
    <footerSection/>
  </main>
</template>

<script>
import newNavbar from '@/layout/newNavbar.vue';
import loginSection from './loginSection.vue';
import footerSection from '@/layout/footerSection.vue';
export default {
    components:{
        newNavbar, loginSection, footerSection
    }
}
</script>

<style>

</style>
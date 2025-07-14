<template>
  <main>
    <newNavbar/>
    <loginSection/>
  </main>
</template>

<script>
import newNavbar from '@/layout/newNavbar.vue';
import loginSection from './loginSection.vue';
export default {
    components:{
        newNavbar, loginSection
    }
}
</script>

<style>

</style>
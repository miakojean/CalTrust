<template>
  <main>
    <new-navbar/>
    <companyDetailSection/>
    <companyReviews/>
    <globalRatingCard/>
    <footerSection/>
  </main>
</template>

<script>
import newNavbar from '@/layout/newNavbar.vue';
import companyDetailSection from './companyDetailSection.vue';
import companyReviews from './companyReviews.vue';
import globalRatingCard from '@/components/cards/globalRatingCard.vue';
import footerSection from '@/layout/footerSection.vue';

export default {

    components:{
        newNavbar,
        footerSection,
        companyReviews,
        companyDetailSection,
        globalRatingCard
    }

}
</script>

<style>

</style>
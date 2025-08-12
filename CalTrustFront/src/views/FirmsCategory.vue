<template>
    <main>
        <newNavbar/>
        <ctaFirms/>
        <firm_Category/>
        <footerSection/>
    </main>
</template>

<script>
import newNavbar from '@/layout/newNavbar.vue';
import firm_Category from '@/views-companies/category/firm_Category.vue';
import footerSection from '@/layout/footerSection.vue';
import ctaFirms from '@/section/ctaFirms.vue';
export default {

    components:{
        newNavbar,
        ctaFirms,
        firm_Category,
        footerSection
    }

}
</script>

<style>

</style>
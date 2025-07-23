<template>
    <main>
        <newNavbar />
        <section class="regis__section main__section">
            <PasswordResetForm/>
        </section>
        <footerSection/>
    </main>
</template>

<script>
import newNavbar from '@/layout/newNavbar.vue';
import PasswordResetForm from '../authtools/passwordResetForm.vue';
import footerSection from '@/layout/footerSection.vue';

export default {

    components:{
        newNavbar, PasswordResetForm, footerSection
    }

}
</script>

<style>

</style>
<template>
  <section class="section__container">
    <div class="main__container">
      <h3>Se connecter</h3>
      <ourForm/>
      <stepper title="Pas de compte?"/>
    </div>
  </section>
</template>

<script>
import ourForm from '@/components/tools/ourSigninForm.vue';
import stepper from '@/components/cards/stepper.vue';
export default {
    components:{
      ourForm, stepper
    }
}
</script>

<style>

</style>
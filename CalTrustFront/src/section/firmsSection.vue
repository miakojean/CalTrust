<template>
  <section class="main__container">
    <h2>Contribuez à l'amélioration des entreprises</h2>
    <p>Donnez et recoltez des avis sur toutes les catégories d'entreprises</p>
    <caroussel/>
    <stepper/>
    <BoxConnexion/>
  </section>
</template>

<script>
import caroussel from '@/components/cards/caroussel.vue';
import stepper from '@/components/cards/stepper.vue';
import BoxConnexion from '@/layout/boxConnexion.vue';
export default {
  components:{
    caroussel,
    stepper,
    BoxConnexion
  }
}
</script>

<style>

</style>
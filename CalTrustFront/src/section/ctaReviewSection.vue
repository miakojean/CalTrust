<template>
  <section class="main__section">
    <div class="main__container">
        <h2>
            Trouver une entreprise de confiance
        </h2>
        <p class="subtitle">
            Optez pour le meilleur choix en vous basant 
            sur les expériences d'autres personnes.
        </p>
        <research-box/>
    </div>
  </section>
</template>

<script>
import researchBox from '@/components/tools/researchBox.vue';
export default {

    components:{
        researchBox
    }

}
</script>

<style scoped>

.subtitle{
    font-size: 1rem;
    text-align: center;
    width: 100%;
}

</style>
<template>
    <section class="main__section">
        <div class="main__container">
            <h1>
                Donnez votre avis, Aidez les autres à choisir
            </h1>
            <p>
                Lorem ipsum dolor sit amet consectetur 
                adipisicing elit. Pariatur impedit eaque 
                ipsa culpa recusandae temporibus, non 
                cumque nostrum laborum quibusdam?
            </p>
            <research-box/>
        </div>
        <div class="pic__container">
            <img class="pair" src="@/assets/Pictures/picture_seven.jpg" alt="Reunion of people" />
            <img class="impair" src="@/assets/Pictures/picture_six.jpg" alt="Reunion of people" />
            <img class="pair" src="@/assets/Pictures/picture_one.jpg" alt="Reunion of people" />
            <img class="impair" src="@/assets/Pictures/picture_four.jpg" alt="Reunion of people" /> 
        </div>
    </section>
</template>

<script>
import mainButton from '@/components/button/mainButton.vue';
import moreButton from '@/components/button/moreButton.vue';
import researchBox from '@/components/tools/researchBox.vue';
export default {
    components:{
        mainButton, moreButton, researchBox
    }
}
</script>

<style scoped>
.pic__container {
    min-height: 100vh;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    align-items: flex-start; /* Alignement en haut par défaut */
    gap: 0.5rem;
    height: auto;
}

/* Cible les images paires (2e, 4e) pour les aligner en bas */
.pic__container img:nth-child(even) {
    align-self: flex-end; /* Pousse vers le bas */
}

@media (min-width: 766px) {
    .pic__container {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        align-items: flex-start; /* Alignement en haut par défaut */
        gap: 0.5rem;
    }

    .pic__container {
        min-height: 50vh;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        align-items: flex-start; /* Alignement en haut par défaut */
        gap: 0.5rem;
        height: auto;
    }

        /* Cible les images paires (2e, 4e) pour les aligner en bas */
    .pic__container img:nth-child(even) {
        align-self: flex-end; /* Pousse vers le bas */
    }
}

@media (min-width: 766px) {
    .pic__container {
        min-height: 50vh;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
        align-items: flex-start; /* Alignement en haut par défaut */
        gap: 0.5rem;
        height: auto;
    }

        /* Cible les images paires (2e, 4e) pour les aligner en bas */
    .pic__container img:nth-child(even) {
        align-self: flex-end; /* Pousse vers le bas */
    }

    .pair{
        margin-top: 2rem;
    }
}

@media (min-width: 1024px){

    .main__container {
        width: 50%;
    }
    .pic__container {
        width: 50%;
    }

    .pic__container img:nth-child(even) {
        align-self: flex-end; /* Pousse vers le bas */
    }
}
</style>
<template>
    <section class="main__section">
        <div class="main__container">
            <h1>
                We're changing the way people connect
            </h1>
            <p>
                Lorem ipsum dolor sit amet consectetur 
                adipisicing elit. Pariatur impedit eaque 
                ipsa culpa recusandae temporibus, non 
                cumque nostrum laborum quibusdam?
            </p>
            <div class="btn__flex">
                <main-button></main-button>
                <more-button/>
            </div>
        </div>
        <div class="pic__container">
            <img class="seven" src="@/assets/Pictures/picture_seven.jpg" alt="Reunion of people" />
            <img class="six" src="@/assets/Pictures/picture_six.jpg" alt="Reunion of people" />
            <img class="one" src="@/assets/Pictures/picture_one.jpg" alt="Reunion of people" />
            <img class="four" src="@/assets/Pictures/picture_four.jpg" alt="Reunion of people" />
            
        </div>
    </section>
</template>

<script>
import mainButton from '@/components/button/mainButton.vue';
import moreButton from '@/components/button/moreButton.vue';
export default {
    components:{
        mainButton, moreButton
    }
}
</script>

<style scoped>
.pic__container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: flex-start; /* Alignement en haut par défaut */
    gap: 20px;
    height: auto;
}

/* Cible les images paires (2e, 4e) pour les aligner en bas */
.pic__container img:nth-child(even) {
    align-self: flex-end; /* Pousse vers le bas */
}
</style>
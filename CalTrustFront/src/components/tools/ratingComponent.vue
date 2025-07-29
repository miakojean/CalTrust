<template>
    <div class="my__rating_container">
        <div class="stars__wrapper">
            <!-- Version avec superposition pour les notes décimales -->
            <span class="my__star" v-for="i in maxStars" :key="'filled-' + i">★</span>
            <span class="my__star empty__star" v-for="i in maxStars" :key="'empty-' + i">★</span>

        </div>
        <span class="the__rate">{{ rating.toFixed(1) }}</span>
    </div>
</template>

<script>
import { computed } from 'vue';
export default {
    props: {
        rating: { type: Number, default: 5 },
        maxStars: { type: Number, default: 5 }
    },
    setup(props) {
        const ratingWidth = computed(() => 
            (props.rating / props.maxStars) * 100 + '%'
        );
        return { ratingWidth };
    }
};
</script>

<style>
.my__rating_container{
    display: flex;
    justify-content: start;
    align-items: center;
    gap: 1rem;
}

.stars__comp{
    display: flex;
    justify-content: start;
    align-items: center;
    gap: 0.2rem;
}

.my__star{
    padding: 0.2rem;
    background: var(--primary-color);
    color: white;
    font-size: 1.2rem;
}

.the__rate{
    color: #777777;
    font-size: 0.9  rem;
}

.stars__wrapper {
    position: relative; /* Contexte de positionnement */
    display: inline-flex;
}

.stars__background, .stars__foreground {
    display: flex;
    gap: 0.2rem;
}

.stars__foreground {
    position: absolute; /* Superposition */
    top: 0;
    left: 0;
    white-space: nowrap; /* Empêche le retour à la ligne */
    overflow: hidden;    /* Masque ce qui dépasse */
}

.empty__star {
    color: #ccc; /* Couleur de l'étoile vide */
}
</style>
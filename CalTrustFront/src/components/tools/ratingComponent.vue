<template>
  <div class="my__rating_container">
    <div 
      class="stars__wrapper"
      :class="{ 'low-rating': rating === 1 }"
    >
      <span class="my__star" v-for="i in fullStars" :key="'filled-' + i">★</span>
      <span v-if="partialStarWidth > 0" class="my__star partial__star">
        <span class="stars__foreground" :style="{ width: partialStarWidth + '%' }">★</span>
        <span class="stars__background">★</span>
      </span>
      <span class="my__star empty__star" v-for="i in emptyStars" :key="'empty-' + i">★</span>
    </div>
    <span class="the__rate">{{ rating.toFixed(1) }}</span>
  </div>
</template>

<script>
import { computed } from 'vue';

export default {
  props: {
    rating: {type: Number, default: 3},
    maxStars: { type: Number, default: 5 }, // Renommé pour plus de clarté
  },
  setup(props) {
    // Nombre d'étoiles pleines
    const fullStars = computed(() => Math.floor(props.rating));

    // Largeur de l'étoile partiellement remplie (en pourcentage)
    const partialStarWidth = computed(() => {
      const decimalPart = props.rating - fullStars.value;
      return decimalPart * 100; // Convertit la partie décimale en pourcentage
    });

    // Nombre d'étoiles vides
    const emptyStars = computed(() => {
      return props.maxStars - Math.ceil(props.rating);
    });

    return { fullStars, partialStarWidth, emptyStars };
  },
};
</script>

<style scoped>
.my__rating_container {
  display: flex;
  justify-content: start;
  align-items: center;
  gap: 1rem;
}

.stars__wrapper {
  position: relative;
  display: inline-flex;
  gap: 0.2rem;
}

.my__star {
  padding: 0.2rem;
  background: var(--primary-color);
  color: white;
  font-size: 1rem;
  position: relative;
  height: 1.5rem;
}

.empty__star {
  background: #d4d4d4;
  color: gray;
}

.partial__star {
  position: relative;
  display: inline-block;
}

.stars__foreground {
  position: absolute;
  top: 0;
  left: 0;
  background: var(--primary-color);
  color: white;
  overflow: hidden;
  white-space: nowrap;
}

.stars__background {
  background: #f3f3f3;
  color: gray;
}

.the__rate {
  color: #777777;
  font-size: 0.9rem;
}

.low-rating .my__star {
  background: red;
  color: white;
}

.low-rating .stars__foreground {
  background: red;
  color: white;
}

.low-rating .empty__star,
.low-rating .stars__background {
  background: #f3f3f3;
  color: gray;
}
</style>
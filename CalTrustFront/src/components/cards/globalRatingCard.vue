<template>
  <article class="testimonial-card">
    <div class="title">
        <h2 class="subtitle">Témoignages</h2>
    </div>

    <div class="divider"></div>

    <div class="title">
        <h4>Total Témoignages</h4>
        <h2 class="subtitle">{{ testimonialsTotal }}</h2>
    </div>

    <div class="about__rating">
        <div class="rate__info">
            <h4>Note moyenne</h4>
            <h2 class="subtitle">{{ averageRating }}.0</h2>
        </div>
        <ratingComponent 
            :rating="rating" 
            :max="5"
            size="small"
        />
    </div>

    <global-rating
        :fiveStars="fiveStars"
        :fourStars="fourStars"
        :threeStars="threeStars"
        :twoStars="twoStars"
        :oneStar="oneStar"
    />
    
    <div class="divider__two"></div>

  </article>
</template>

<script lang="ts">
import { computed, defineComponent } from 'vue';
import RatingComponent from '../tools/ratingComponent.vue';
import GlobalRating from '../tools/globalRating.vue';

export default defineComponent({
    name: 'TestimonialCard',
    props: {
        testimonialsTotal: {
            type: Number,
            default: 0
        },
        averageRating: {
            type: Number,
            default: 0,
            validator: (value: number) => value >= 0 && value <= 5
        },
        rating: { 
            type: Number,
            default: 4,
            validator: (value: number) => value >= 0 && value <= 5
        },
        fiveStars: {
            type: Number,
            default: 0,
            validator: (value: number) => value >= 0 && value <= 100
        },
        fourStars: {
            type: Number,
            default: 0,
            validator: (value: number) => value >= 0 && value <= 100
        },
        threeStars: {
            type: Number,
            default: 0,
            validator: (value: number) => value >= 0 && value <= 100
        },
        twoStars: {
            type: Number,
            default: 0,
            validator: (value: number) => value >= 0 && value <= 100
        },
        oneStar: {
            type: Number,
            default: 0,
            validator: (value: number) => value >= 0 && value <= 100
        }
    },
    components: {
        RatingComponent,
        GlobalRating
    },
    setup(props) {
        const formattedRating = computed(() => {
            // Affiche un chiffre après la virgule si nécessaire
            return Number.isInteger(props.averageRating) 
                ? props.averageRating.toFixed(1) 
                : props.averageRating.toFixed(1);
        });

        return { formattedRating };
    }
});
</script>

<style scoped>
.testimonial-card {
  display: flex;
  flex-direction: column;
  align-items: normal;
  gap: 1rem;
  padding: 1rem;
  background: white;
  width: 100%;
  max-width: 400px;

}

.divider {
  height: 2px;
  background: var(--primary-color); /* Couleur grise légère */
  margin: 12px 0; /* Espacement vertical */
}

.divider__two {
  height: 1px;
  background: #d8d8d8; /* Couleur grise légère */
  margin: 0.5rem 0; /* Espacement vertical */
}

.title{
    display:flex;
    flex-direction: column;
    justify-content:start;
}

.subtitle{
    text-align: start;
}

.about__rating{
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: normal;
    gap: 1rem;
}

@media (min-width: 766px) {
    .message__body{
        font-size: 0.8rem;
        text-align: start;
    }
}

@media (min-width: 1260px) {
    .message__body{
        font-size: 0.8rem;
        text-align: start;
    }
}
</style>
<template>
  <article class="testimonial-card">
    <div class="title">
        <h2 class="subtitle">Témoignages</h2>
    </div>

    <div class="divider"></div>

    <div class="title">
        <h4>Total Témoignages</h4>
        <h2 class="subtitle">10.7K</h2>
    </div>

    <div class="about__rating">
        <div class="rate__info">
            <h4>Note moyenne</h4>
            <h2 class="subtitle">4.0</h2>
        </div>
        <ratingComponent 
            :rating="rating" 
            :max="5"
            size="small"
        />
    </div>

    <global-rating/>
    
    <div class="divider__two"></div>

  </article>
</template>

<script>
import fakeRating from '../tools/fakeRating.vue';
import { computed, ref } from 'vue';
import ratingComponent from '../tools/ratingComponent.vue';
import globalRating from '../tools/globalRating.vue';

const defaultPic = new URL('@/assets/Pictures/fakepropfilepic.jpg', import.meta.url).href;

export default {
    props:{

        company:{
            type:String,
            default:'anonymous'
        },
        info:{
            type: String,
            default:"John Doe"
        },
        username:{
            type: String,
            default: 'unknown'
        },
        pic:{
            type: String,
            default: defaultPic
        },
        rating: { 
            type: Number,
            default: 4,  // Valeur par défaut
            validator: (value) => {
                return value >= 0 && value <= 5;  // Validation entre 0 et 5
            }
        }
    },

    components:{
        fakeRating,
        ratingComponent,
        globalRating
    },

    setup(props) {
        const defaultPic = new URL('@/assets/Pictures/fakepropfilepic.jpg', import.meta.url).href;
        const profilePic = computed(() => props.pic || defaultPic);

        const isUseful = ref(false)

        function iLikeIt () {
            if (isUseful.value === false){
                isUseful.value = true
            } else if (isUseful.value === true){
                isUseful.value = false
            }
        }

        return { profilePic, isUseful, iLikeIt };
    }

}
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
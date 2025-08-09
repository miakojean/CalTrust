<template>
  <section class="reviews__section">
    <second-stepper title="Les avis récents sur l'entreprise"/>
    
    <div class="testimonial__container">
      <!-- Boucle sur les avis -->
      <testimonials 
        v-for="(review, index) in reviews"
        :key="review.id || index"  
        :info="review.user || 'Anonyme'"
        :rating="review.rating"
        :message="review.comment"
        :date="review.local_date"
        :avatar="review.user_initial"
        :company="review.establishment"
      />
      
      <!-- State de chargement/erreur -->
      <div v-if="reviews.length === 0" class="loading-state">
        Chargement des avis...
      </div>
    </div>
  </section>
</template>

<script>
import SecondStepper from '@/components/cards/secondStepper.vue';
import testimonials from '@/components/cards/testimonials.vue';
import { onMounted, ref } from 'vue';
import { fetchRecentsReviews } from '@/_services/_fetchreviews';

export default {
    components: {
        testimonials,
        SecondStepper
    },

    props:{
        
    },

    setup() {
        const reviews = ref({});

        onMounted(async () => {
            try {
                const apiData = await fetchRecentsReviews();
                
                // Si l'API retourne { status, data }
                if (apiData.status === 'success') {
                reviews.value = apiData.data;
                } 
                // Si l'API retourne directement le tableau
                else if (Array.isArray(apiData)) {
                reviews.value = apiData;
                }
                
            } catch (error) {
                error.value = error.message;
            }
        });

        return {
            reviews
        }
    }
}
</script>

<style scoped>
.reviews__section{
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 1rem;
}

.testimonial__container{
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

@media(min-width:766px) {
    .testimonial__container{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
    }
}

@media(min-width: 1260px) {
    .testimonial__container{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
    }
}
</style>
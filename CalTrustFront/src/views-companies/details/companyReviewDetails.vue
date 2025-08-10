<template>
  <section class="reviews__section">
    <second-stepper title="Les avis récents sur l'entreprise"/>
    
    <div class="testimonial__container">
      <!-- Boucle sur les avis -->
      <testimonialCardForFirm 
        v-for="(review, index) in reviews"
        :key="review.id || index"
        :info="review.customer_name || 'Anonyme'"  
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
import testimonialCardForFirm from '@/components/cards/testimonialCardForFirm.vue';
import { onMounted, ref } from 'vue';
import { fetchRecentsFirms } from '../_companyservices';

export default {
    components: {
        SecondStepper,
        testimonialCardForFirm
    },

    props:{
        
    },

    setup() {
        const reviews = ref([]);

        const firm = ref({})

        const firmId = history.state.id;

        onMounted(async () => { 
        try {
            const response = await fetchRecentsFirms(firmId);

            if (response?.data) {
            // Données de base

            // Données des avis
            reviews.value = response.data.reviews.list || [];
            
            // Statistiques

            console.log('Données chargées:', { reviews: reviews.value });
            }
        } catch (error) {
            console.error("Erreur de chargement:", error);
        }
        });

        return {
            reviews, firmId
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
<template>
  <section class="reviews__section">
    <second-stepper title="Les avis récents sur l'entreprise"/>
    
    <div class="testimonial__container">

        <template v-if="isLoading === true">
            <cardLoading v-for="n in 4" :key="n" />
        </template>
        <!-- Boucle sur les avis -->
        <testimonialCardForFirm 
            v-for="(review, index) in reviews"
            :key="review.id || index"
            :info="review.user || 'Anonyme'"  
            :rating="review.rating"
            :message="review.comment"
            :date="review.local_date"
            :avatar="review.user_initial"
            :company="review.establishment"
            @review-details="moveToDetails(review)"
        />
      
      <!-- State de chargement/erreur -->
      <div v-if="reviews.length === 0" class="loading-state">
        Chargement des avis...
      </div>
    </div>
  </section>
</template>

<script>
import { onMounted, ref } from 'vue';
import { fetchRecentsFirms } from '../_companyservices';
import cardLoading from '@/components/cards/cardLoading.vue';
import SecondStepper from '@/components/cards/secondStepper.vue';
import testimonialCardForFirm from '@/components/cards/testimonialCardForFirm.vue';
import { useRouter } from 'vue-router';
export default {
    components: {
        SecondStepper,
        testimonialCardForFirm,
        cardLoading
    },

    props:{
        
    },

    setup() {
        const reviews = ref([]);

        const firm = ref({})

        const firmId = history.state.id;

        const isLoading = ref(true)

        const router = useRouter();

        const moveToDetails = (review) => {
            router.push(
                { name: 'avis-detail', 
                params: { reviewId: review.id },
                state: {reviewId: review.id}
            }); // Navigation avec le paramètre reviewId
        };


        onMounted(async () => { 
            try {
                isLoading.value = true
                const response = await fetchRecentsFirms(firmId);

                if (response?.data) {
                    reviews.value = response.data.reviews.list || [];
                    isLoading.value = false
                    // Statistiques

                    console.log('Données chargées:', { reviews: reviews.value });
                }
            } catch (error) {
                isLoading.value = false
                console.error("Erreur de chargement:", error);
            }
        });

        return {
            reviews, firmId, isLoading, moveToDetails, router
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
<template>
  <section class="reviews__section">
    <second-stepper title="Consulter les avis récents"/>
    
    <div class="testimonial__container">
      
        <template v-if="isLoading ===true">
            <cardLoading v-for="n in 4" :key="n" />
        </template>

      <template v-else-if="reviews.length > 0">
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
      </template>

      <div v-else class="no-data__container">
        <p>Aucun avis récent n'est disponible pour le moment.</p>
      </div>

    </div>
  </section>
</template>

<script>
import SecondStepper from '@/components/cards/secondStepper.vue';
import testimonials from '@/components/cards/testimonials.vue';
import cardLoading from '@/components/cards/cardLoading.vue';
import { onMounted, ref } from 'vue';
import { fetchRecentsReviews } from '@/_services/_fetchreviews';

export default {
    components: {
        testimonials,
        SecondStepper,
        cardLoading
    },

    setup() {
        const reviews = ref([]); // Il est plus sûr d'initialiser avec un tableau vide
        const isLoading = ref(true);
        const error = ref(null); // Ajout d'une variable pour gérer les erreurs

        onMounted(async () => {
            try {
                const apiData = await fetchRecentsReviews();
                
                if (apiData.status === 'success') {
                    reviews.value = apiData.data;
                } 
                else if (Array.isArray(apiData)) {
                    reviews.value = apiData;
                }
            } catch (err) {
                // Gestion des erreurs de l'API
                console.error("Erreur lors de la récupération des avis:", err);
                error.value = 'Impossible de charger les avis. Veuillez réessayer.';
            } finally {
                // Cet ajout est CRUCIAL. Il garantit que le chargement se termine
                // que la requête ait réussi ou échoué.
                isLoading.value = true;
            }
        });

        return {
            isLoading, 
            reviews,
            error // Rendre la variable d'erreur disponible dans le template
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

.loading__container{
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

@media(min-width:766px) {
    .testimonial__container{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
    }

    .loading__container{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
    }
}

@media(min-width: 1260px) {
    .testimonial__container{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        gap: 1rem;
    }

    .loading__container{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 1rem;
    }
}
</style>
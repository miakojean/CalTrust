<template>
  <div class="main__container">
    <h3>Details de l'avis sur l'entreprise {{ review.firm_name }}</h3>
    <tesimonialsCardDetail
        :username = review.customer_name
        :message = review.comment
        :rating = review.rating
    />      
  </div>
</template>

<script>
import testimonialCardForFirm from '@/components/cards/testimonialCardForFirm.vue';
import notifCard from '@/components/notifications/notifCard.vue';
import tesimonialsCardDetail from '@/components/cards/tesimonialsCardDetail.vue';
import { onMounted, ref } from 'vue';
import { fetchSpecificReview } from '@/_services/_fetchreviews';

export default {
    components: {
        testimonialCardForFirm,
        notifCard,
        tesimonialsCardDetail
    },

    setup() {

        const reviewId = history.state.reviewId;

        const review = ref({});

        const loadReviewDetails = async (reviewId) => {
            try {
                const apiData = await fetchSpecificReview(reviewId);
                review.value = apiData;
                console.log("Détails de l'avis chargés:", review.value);
            } catch (err) {
                console.error("Erreur lors de la récupération des détails de l'avis:", err);
            }
        };

        onMounted(async () => { 
            console.log("ID de l'avis:", reviewId);
            await loadReviewDetails(reviewId);
        });

        return {
            review,
            reviewId,
            loadReviewDetails
        }
    }
}
</script>

<style scoped>

</style>
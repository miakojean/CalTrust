<template>
  <div class="main__container">
    <h3>Details de l'avis sur l'entreprise {{ review.firm_name }}</h3>
    <tesimonialsCardDetail
        :username = review.customer_name
        :message = review.comment
        :rating = review.rating
        :date="review.created_at"
        :customerInitial = "getInitials(review.customer_name)"
    />      
  </div>
</template>

<script>
import testimonialCardForFirm from '@/components/cards/testimonialCardForFirm.vue';
import notifCard from '@/components/notifications/notifCard.vue';
import tesimonialsCardDetail from '@/components/cards/tesimonialsCardDetail.vue';
import { onMounted, ref, computed } from 'vue';
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

        function getInitials(name) {
            if (typeof name !== 'string') return '';

            const words = name.trim().split(/\s+/); // Sépare les mots par les espaces
            const firstTwoWords = words.slice(0, 2); // Garde les deux premiers mots

            const initials = firstTwoWords
                .map(word => word.charAt(0).toUpperCase()) // Prend la première lettre
                .join('');

            return initials;
        }

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
            loadReviewDetails,
            getInitials
        }
    }
}
</script>

<style scoped>

</style>
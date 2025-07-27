<template>
  <section class="reviews__section">    
    <second-stepper title="Les entreprises les plus mieux notées"/>
    
    <div class="testimonial__container">
      <!-- Boucle sur les avis -->
        <companyCard/>
        <companyCard/>
        <companyCard/>
        <companyCard/>
        <companyCard/>
    </div>
  </section>
</template>

<script>
import SecondStepper from '@/components/cards/secondStepper.vue';
import testimonials from '@/components/cards/testimonials.vue';
import companyCard from './companyCard.vue';
import { onMounted,ref } from 'vue';
import { fetchRecentsReviews } from '@/_services/_fetchreviews';
export default {
    components:{
        testimonials,
        SecondStepper,
        companyCard
    },

    setup(){

        const reviews = ref([]);

        onMounted( async ( ) => { 
            try {
                const response = await fetchRecentsReviews();
                if (response) {
                    reviews.value = response.data; // Stockez les données
                    console.log('Avis chargés:', reviews.value);
                }
            } catch (error) {
                console.error("Erreur de chargement:", error);
            }
        });

        return{
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

@media(min-width: 1024px) {
    .testimonial__container{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        gap: 1rem;
    }
}
</style>
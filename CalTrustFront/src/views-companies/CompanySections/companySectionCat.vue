<template>
  <section class="reviews__section">    
    <second-stepper title="Les entreprises recemment ajoutées"/>
    
    <div class="testimonial__container">
      <!-- Boucle sur les avis -->
        <companyCard 
            v-for="(firm, index) in firms"
            :key="index"
            :firm="firm.name.company_name"
            :category="firm.category_display"
            :user = "firm.firm_profile_id"
        />
    </div>
  </section>
</template>

<script>
import SecondStepper from '@/components/cards/secondStepper.vue';
import testimonials from '@/components/cards/testimonials.vue';
import companyCard from '@/views-companies/CompanySections/companyCard.vue';
import { onMounted,ref } from 'vue';
import { fetchRecentsFirms } from '@/_services/_fetchreviews';
export default {
    components:{
        testimonials,
        SecondStepper,
        companyCard
    },

    setup(){

        const firms = ref([]);

        onMounted( async ( ) => { 
            try {
                const response = await fetchRecentsFirms();
                if (response) {
                    firms.value = response.data; // Stockez les données
                    console.log('Entreprises récentes chargées:', firms.value);
                }
            } catch (error) {
                console.error("Erreur de chargement:", error);
            }
        });

        const myFirmId = ref(0)

        const voirFirm = (index) =>{
            myFirmId.value = index
            console.log(index)
        }

        return{
            firms, voirFirm, myFirmId
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
        grid-template-columns: 1fr 1fr 1fr;
        gap: 1rem;
    }
}

@media(min-width: 1280px) {
    .testimonial__container{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        gap: 1rem;
    }
}
</style>
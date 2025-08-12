<template>
   <section class="reviews__section">    
    <second-stepper :title="categoryTitle || 'Les entreprises récemment ajoutées'"/>

    <div class="testimonial__container">
        <template v-if="isLoading === true">
            <cardLoading v-for="n in 4" :key="n" />
        </template>

        <companyCard 
            v-for="(firm, index) in firms"
            :key="index"
            :firm="firm.name.company_name"
            :category="firm.category_display"
            :user="firm.id"
        />
    </div>
    <moreButton
        label="toutes les entreprises"
    />
  </section>
</template>

<script>
import SecondStepper from '@/components/cards/secondStepper.vue';
import testimonials from '@/components/cards/testimonials.vue';
import companyCard from '@/views-companies/CompanySections/companyCard.vue';
import cardLoading from '@/components/cards/cardLoading.vue';
import moreButton from '@/components/button/moreButton.vue';
import { useRoute } from 'vue-router';
import { onMounted, ref, watch } from 'vue';
import { fetchRecentsFirms } from '@/_services/_fetchreviews';
import caroussel from '@/components/cards/caroussel.vue';
import api from '@/_services/_authservices';

export default {
    components:{
        testimonials,
        SecondStepper,
        companyCard,
        cardLoading,
        moreButton,
        caroussel
    },

    setup() {
        const firms = ref([]);
        const isLoading = ref(true);
        const categoryTitle = ref('');
        const route = useRoute();

        const fetchFirmsByCategory = async (categoryCode) => {
            try {
                isLoading.value = true;
                const response = await api.get(`/companies/search/?category=${categoryCode}`);
                if (response) {
                    firms.value = response.data.results;
                    categoryTitle.value = `Entreprises: ${route.params.categoryName}`;
                }
            } catch (error) {
                console.error("Erreur de chargement:", error);
            } finally {
                isLoading.value = false;
            }
        };

        // Gérer le chargement initial basé sur l'URL
        onMounted(() => {
            if (route.params.categoryCode) {
                fetchFirmsByCategory(route.params.categoryCode);
            } else {
                fetchRecentsFirms(); // Fallback aux entreprises récentes
            }
        });

        // Réagir aux changements de route
        watch(() => route.params.categoryCode, (newCode) => {
            if (newCode) fetchFirmsByCategory(newCode);
        });

        const handleCategorySelection = (category) => {
            // Cette méthode sera appelée quand une catégorie est sélectionnée dans le carousel
            fetchFirmsByCategory(category.code);
        };

        return {
            firms,
            isLoading,
            categoryTitle,
            handleCategorySelection
        };
    }
};
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
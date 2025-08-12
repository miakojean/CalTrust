<template>
  <main>
    <new-navbar/>
    <section class="company__section">
      <div class="company__left-sidebar">
        <company-detail-card
          :firm="firm.company_name"
          :category="firm.category"
          :user="firm.id"
          :email="firm.email || ''"
          :website="firm.website || ''"
          :address="firm.address || ''"
        />
      </div>
      <div class="company__center">
        <company-review-details
          :reviews="reviews"
          :stats="stats"
        />
      </div>
      <div class="company__right-sidebar">
        <global-rating-card
          :testimonials-total="stats.total"
          :average-rating="stats.average"
          :rating="stats.average"
          :five-stars="stats.percentages[5] || 0"
          :four-stars="stats.percentages[4] || 0"
          :three-stars="stats.percentages[3] || 0"
          :two-stars="stats.percentages[2] || 0"
          :one-star="stats.percentages[1] || 0"
        />
      </div>
    </section>
    <footer-section/>
  </main>
</template>

<script>
import { ref, onMounted } from 'vue';
import newNavbar from '@/layout/newNavbar.vue';
import footerSection from '@/layout/footerSection.vue';
import globalRatingCard from '@/components/cards/globalRatingCard.vue';
import companyDetailCard from './companyDetailCard.vue';
import companyReviewDetails from './companyReviewDetails.vue';
import { fetchRecentsFirms } from '../_companyservices';

export default {
  components: {
    newNavbar,
    footerSection,
    companyDetailCard,
    companyReviewDetails,
    globalRatingCard
  },

  setup() {
    const firm = ref({
      id: null,
      company_name: '',
      address: '',
      email: '',
      website: '',
      category: ''
    });

    const reviews = ref([]);
    const stats = ref({
      average: 0,
      total: 0,
      distribution: {},
      percentages: {}
    });

    const firmId = history.state.id;

    onMounted(async () => { 
      try {
        const response = await fetchRecentsFirms(firmId);

        if (response?.data) {
          // Données de base
          firm.value = {
            id: response.data.company.id,
            company_name: response.data.company.name?.company_name || '',
            address: response.data.company.name?.address || '',
            email: response.data.name?.email || '',
            website: response.data.website || '',
            category: response.data.company.category_display || ''
          };

          // Données des avis
          reviews.value = response.data.reviews || [];
          
          // Statistiques
          stats.value = response.data.stats || {
            average: 0,
            total: 0,
            distribution: {5: 0, 4: 0, 3: 0, 2: 0, 1: 0},
            percentages: {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
          };

          console.log('Données chargées:', { 
            firm: firm.value, 
            reviews: reviews.value, 
            stats: stats.value,
            rawData: response.data // Ajoutez ceci pour debug
          });
        }
      } catch (error) {
        console.error("Erreur de chargement:", error);
      }
    });

    return { firm, reviews, stats };
  }
}
</script>

<style>
.company__section {
  display: flex;
  max-width: 1440px; /* ou la largeur maximale que vous souhaitez */
  margin: 0 auto;
  padding: 20px;
  gap: 20px; /* espace entre les colonnes */
}

.company__left-sidebar {
  position: sticky;
  top: 100px; /* Ajustez selon la hauteur de votre navbar */
  height: fit-content;
  width: 300px; /* Largeur fixe pour la sidebar gauche */
  flex-shrink: 0;
}

.company__center {
  flex-grow: 1;
  max-width: 800px; /* Largeur max pour la section centrale */
  margin: 0 auto;
}

.company__right-sidebar {
  position: sticky;
  top: 100px; /* Ajustez selon la hauteur de votre navbar */
  height: fit-content;
  width: 300px; /* Largeur fixe pour la sidebar droite */
  flex-shrink: 0;
}

/* Version tablette */
@media (min-width: 768px) and (max-width: 1199px) {
  .company__section {
    display: grid;
    grid-template-columns: 250px 1fr;
    grid-template-areas: "left center"
                         "right center";
  }
  
  .company__left-sidebar {
    grid-area: left;
    width: 100%;
    position: sticky;
    top: 100px;
  }
  
  .company__center {
    grid-area: center;
    max-width: 100%;
  }
  
  .company__right-sidebar {
    grid-area: right;
    width: 100%;
    position: sticky;
    top: 100px;
  }
}

/* Version mobile */
@media (max-width: 767px) {
  .company__section {
    flex-direction: column;
  }
  
  .company__left-sidebar,
  .company__right-sidebar {
    position: static;
    width: 100%;
    margin-bottom: 20px;
  }
}
</style>
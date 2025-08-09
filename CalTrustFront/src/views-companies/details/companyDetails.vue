<template>
  <main>
    <new-navbar/>
    <section class="company__section">
      <div class="company__left-sidebar">
        <companyDetailCard
          :firm="firm.company_name"
          :category="firm.category"
          :user="firm.id"
          :email="firm.email"
          :website="firm.website"
          :addresse="firm.address"
        />
      </div>
      <div class="company__center">
        <companyReviewDetails
          
        />
      </div>
      <div class="company__right-sidebar">
        <globalRatingCard/>
      </div>
    </section>
    <footerSection/>
  </main>
</template>

<script>
import newNavbar from '@/layout/newNavbar.vue';
import companyDetailSection from './companyDetailSection.vue';
import companyReviews from '../companyReviews.vue';
import globalRatingCard from '@/components/cards/globalRatingCard.vue';
import companyDetailCard from './companyDetailCard.vue';
import companyReviewDetails from './companyReviewDetails.vue';
import footerSection from '@/layout/footerSection.vue';
import { fetchRecentsFirms } from '../_companyservices';
import { ref, onMounted } from 'vue';
import CompanyDetailCard from './companyDetailCard.vue';

export default {

  components:{
    newNavbar,
    footerSection,
    companyReviews,
    companyDetailSection,
    companyDetailCard,
    companyReviewDetails,
    globalRatingCard
  },

  setup(){
    
    const firm = ref({
      name:"",
      company_name:"",
      address: "",
      email:"",
      website:"",
      category:""
    })

    const reviews = ref([])

    const firmId = history.state.id;

    onMounted(async () => { 
      try {
        const response = await fetchRecentsFirms(firmId);

        if (response) {
          // On récupère le bloc "name"
          const nameData = response.data.name;
          const reviewsData = response.data.reviews
          const globalResponse = response.data

          firm.value = {
            id: nameData.user_id,
            company_name: nameData.company_name,
            address: nameData.address,
            email: nameData.email,        // Ajoutez
            website: globalResponse.website,     // Ajoutez
            category: globalResponse.category_display   // Ajoutez si nécessaire
          };

          reviews.value = reviewsData

          console.log('Entreprise chargée:', firm.value);
        }
      } catch (error) {
        console.error("Erreur de chargement:", error);
      }
    });


    return {firm, firmId}
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
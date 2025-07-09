<template>
  <section id="features__section" class="main__section">
    <div class="main__container">
      <h2 class="main__feat__title">
        Donnez votre avis, Aidez les autres à choisir
      </h2>
      <p class="paragraph__feat">
        Lorem ipsum dolor sit amet consectetur 
        adipisicing elit. Pariatur impedit eaque 
        ipsa culpa recusandae temporibus, non 
        cumque nostrum laborum quibusdam?
      </p>
    </div>
    
    <div class="features__container">
      <features-cards/>
      <features-cards
        title="Réponse aux Avis"
        subtitle="Les entreprises peuvent répondre aux avis pour engager le dialogue, clarifier une situation ou remercier leurs clients" 
        icon="fas fa-comment-dots"
      />
      <features-cards
        title="Notation par Critères"
        subtitle="Notez sur plusieurs critères (service, qualité, rapport qualité-prix...) pour des évaluations plus détaillées et utiles." 
        icon="fas fa-star-half-alt"
      />
      <features-cards
        title="Alertes Nouvelles Évaluations"
        subtitle="Soyez notifié(e) quand une entreprise que vous suivez reçoit un nouvel avis ou améliore sa note." 
        icon="fas fa-bell"
      />
      <features-cards
        title="Classements & Palmarès"
        subtitle="Découvrez le top des entreprises les mieux notées par catégorie, et comparez leurs performances grâce à nos classements mensuels." 
        icon="fas fa-trophy"
      />
    </div>
  </section>
</template>

<script>
import featuresCards from '@/components/cards/featuresCards.vue';
export default {
  components:{
    featuresCards,
  }
}
</script>

<style scoped>
.main__feat__title{
  color: #fff;
}

.paragraph__feat{
  color: #fff;
}

.features__container{
  display: flex;
  flex-direction: column;
  gap: 1rem;
}


#features__section{
  padding: 0.5rem;
  border-radius: 1rem;
  background: linear-gradient(179deg,rgba(27, 60, 83, 1) 0%, rgba(186, 186, 186, 1) 89%, rgba(252, 252, 250, 1) 100%);
}

@media(min-width: 766px){

  .features__container{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
  }

  .features__cards{
    width: auto;
  }

  #features__section{
    height: 60vh;
    padding: 0.5rem;
    background: linear-gradient(179deg,rgba(27, 60, 83, 1) 0%, rgba(186, 186, 186, 1) 89%, rgba(252, 252, 250, 1) 100%);
  }
}
</style>
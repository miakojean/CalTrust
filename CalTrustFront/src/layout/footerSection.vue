<template>
  <footer class="flex__center">
    <div class="ft__header flex__center">

      <h2 class="ft__title">Caltrust</h2>

      <h3 class="title">
        Making the world a better place through constructing elegant hierarchies.
      </h3>
      <div class="logo flex__inline">
        <i class="ri-facebook-circle-fill"></i>
        <i class="ri-instagram-line"></i>
        <i class="ri-twitter-x-fill"></i>
      </div>
    </div>
    
    <div class="ft__links grid__two_and_four__fr">
      <footerCard/>
      <footerCard title="support" :tables="support"/>
      <footerCard title="company" :tables="company"/>
      <footerCard title="legal" :tables="legal"/>
    </div>

    <div class="newsletter flex__center">
      <h3 class="title">
        S'abonner à la newsletter
      </h3>
      <inputfamily label="Email" type ="email" placeholder = "Entrer votre addresse mail"/>
      <mainButton_2 label="s'inscrire"/>
    </div>

    <div class="rights">
      <p>© 2025 Caladrius LLC. All rights reserved.</p>
    </div>
  </footer>
</template>

<script>
import footerCard from '@/components/cards/footerCard.vue';
import inputfamily from '@/components/tools/inputfamily.vue';
import mainButton_2 from '@/components/button/mainButton_2.vue';
export default {
  components:{
    footerCard, inputfamily, mainButton_2
  },
  setup(){
    const support = ['Submit ticket', 'documentation', 'Guides']
    const company = ['About', 'Job', 'Blog', 'Press']
    const legal = ['terms of services', 'privacy policy', 'License']

    return {
      support, company, legal
    }
  }
}
</script>

<style scoped>
footer{
  padding: 1rem;
  background: var(--primary-color);
  color: #f3f3f3;
  border-radius: 1rem;
  width: 100%;
}

.ft__title{
  color: var(--near-white);
  font-size: 1.8rem;
  text-align: start;
}

.title{
  font-size: 1.2rem;
  font-weight: 500;
}

.logo i{
  font-size: 1.5rem;
  font-weight: 400;
}

.rights p{
  color: var(--near-white);
  font-size: 1rem;
}
</style>
<template>
  <footer class="flex__center">
    <div class="ft__header flex__center">
      <h3>
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
      <footerCard/>
      <footerCard/>
      <footerCard/>
    </div>
  </footer>
</template>

<script>
import footerCard from '@/components/cards/footerCard.vue';
export default {
  components:{
    footerCard
  }
}
</script>

<style scoped>
footer{
  padding: 1rem;
  background: var(--primary-color);
  color: #f3f3f3;
  border-radius: 1rem;
  height:100vh;
}

.logo i{
  font-size: 1.5rem;
  font-weight: 400;
}
</style>
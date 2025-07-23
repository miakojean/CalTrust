<template>
    <main>
        <newNavbar />
        <section class="regis__section main__section">
            <customerRegistration/>
        </section>
        <footerSection/>
    </main>
</template>
  
<script>

import footerSection from '@/layout/footerSection.vue';
import newNavbar  from '@/layout/newNavbar.vue';
import customerRegistration from '@/views-authentication/authtools/customerRegistration.vue';

export default {
    components:{ 
      newNavbar,
      footerSection,
      customerRegistration
    },
  
    
}
  
</script>
  
<style scoped>
  
  form p{
    font-size: 1.2rem;
    font-weight: 600;
    color: var(--primary-color);
  }
  
  .regis__btn{
    display: flex;
    justify-content: center;
    width: 100%;
    gap: 1rem;
  }
  
  .v-enter-active,
  .v-leave-active {
  transition: opacity 0.5s ease;
  }
  
  .v-enter-from,
  .v-leave-to {
  opacity: 0;
  }
  
  .errorMessage{
  color: red;
  font-size: 0.8rem;
  }
  
  .succesMessage{
    color: var(--primary-color);
    font-size: 0.8rem;
  }
  </style>
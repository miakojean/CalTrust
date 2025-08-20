<template>
  <div class="profile__container">
    <h4>{{ title }}</h4>
    <p>{{ description }}</p>

    <div class="divider"></div>
    <notification__card/>
    <notification__card/>
    <notification__card/>
    <notification__card/>
    
    
  </div>
</template>

<script>
import notification__card from '@/components/cards/notification__card.vue';

export default {
    components:{
        notification__card
    },

    props:{
        title:{
            type:String,
            default:'Informations de base'
        },
        description:{ 
            /* This is description of the block */
            type:String,
            default:'Cette section présente les différentes information de base de votre entreprise '
        },
        
    },

    setup() {
    
    
    

    return {
      
    };
  }
}
</script>

<style scoped>
.profile__container{
    display: flex;
    flex-direction: column;
    justify-content: start;
    gap: 0.5rem;
    width: 100%;
}

.profile__container h4,p{
    text-align: start;
}

h4{
    font-size: 1rem;
}

p{
    font-size: 0.9rem;
    font-weight: 400;
}

.divider {
  height: 2px;
  background: #d8d8d8; /* Couleur grise légère */
  margin: 1rem 0; /* Espacement vertical */
}
</style>
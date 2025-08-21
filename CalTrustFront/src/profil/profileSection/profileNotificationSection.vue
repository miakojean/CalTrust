<template>
  <section class="profile__section">
    
    <profile__notifications
      title="Notifications"
      description="Consultez les avis récents sur votre entreprise"
    />
    
    
  </section>
</template>

<script>
import profileInfoBlock from '../profileComponents/profileInfoBlock.vue';
import profile__notifications from '../profileComponents/profile__notifications.vue';

export default {
  components:{
    profileInfoBlock,
    profile__notifications
  },

  setup(){
    

    return{
      
    }
  }
}
</script>

<style scoped>
.profile__section{
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 1rem;
}
</style>
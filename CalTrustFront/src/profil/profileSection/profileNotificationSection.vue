<template>
  <section class="profile__section">
    
    <profile__notifications
      title="Notifications"
      description="Consultez les avis récents sur votre entreprise"
    />
    
    
  </section>
</template>

<script>
import { ref } from 'vue';
import profileInfoBlock from '../profileComponents/profileInfoBlock.vue';
import profileNotifications from '../FirmView/profileNotifications.vue';
import profile__notifications from '../profileComponents/profile__notifications.vue';
export default {
  components:{
    profileInfoBlock,
    profile__notifications
  },

  setup(){
    const securityFields = ref([
      { label: 'Mot de passe', value: "****************" },
      { label: 'Authentification', value: "www.firms.com" },
    ])

    const administratifs = ref([
        {label:'Registre de commerce', value:""},
        {label:'Registre fiscal', value:""},
    ])

    return{
      securityFields, administratifs
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
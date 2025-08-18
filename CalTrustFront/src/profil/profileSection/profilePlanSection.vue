<template>
  <section class="profile__section">
    <profileInfoBlock
      title="Mon plan de souscription"
      :fields="securityFields"
      :isThereDescription="false"
      :isThereToggle="false"
      :uploadFile="false"
    />

    <profileInfoBlock
      title="Mes documents administratifs"
      :fields="administratifs"
      :isThereDescription="false"
      :isThereToggle="false"
      :uploadFile="false"
    />
  </section>
</template>

<script>
import { ref } from 'vue';
import profileInfoBlock from '../profileComponents/profileInfoBlock.vue';
export default {
  components:{
    profileInfoBlock,
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
<template>
  <section class="profile__section">
    <profileInfoBlock
      title="Sécurité"
      :fields="securityFields"
      :isThereDescription="false"
      :isThereToggle="false"
      :uploadFile="false"
    />

    <profile__BlockFile
      title="Mes documents administratifs"
      description="Cette section contient tous les documents administratifs"
      
    />
  </section>
</template>

<script>
import { ref } from 'vue';
import profileInfoBlock from '../profileComponents/profileInfoBlock.vue';
import profile__BlockFile from '../profileComponents/profile__BlockFile.vue';

export default {
  components:{
    profileInfoBlock,
    profile__BlockFile
  },

  setup(){
    const securityFields = ref([
      { label: 'Mot de passe', value: "****************" },
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
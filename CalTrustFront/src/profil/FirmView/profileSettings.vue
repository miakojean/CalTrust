<template>
  <section class="profile__section">
    <profileInfoBlock
      :isThereDescription="false"
      :isThereToggle="false"
    />
    <profileInfoBlock
      title="Informations supplémentaires"
      description="Ici vous retrouvez vos informations supplémentaires"
      :fields="otherFields"
      :uploadFile="false"
    />
  </section>
</template>

<script>
import { ref, onMounted } from 'vue';
import profileInfoBlock from '../profileComponents/profileInfoBlock.vue';
import { fetchMyPersonalInfo } from '../_profileServices/callToApi';

export default {
  components:{
    profileInfoBlock,
  },

  setup(){
    const otherFields = ref([
      { label: 'Catégorie', value: "Services Financiers & Banques" },
      { label: 'website', value: "www.firms.com" },
      {label:'Mise en ligne', value:"12/02/2025"}
    ])

    onMounted(async () => {
      try {
        const response = await fetchMyPersonalInfo()

        if (response?.data){
          console.log(response.data)
        }
      } catch(error) {
        console.error("Erreur de chargement:", error);
      }
    })

    return{
      otherFields,
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
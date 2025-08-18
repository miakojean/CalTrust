<template>
  <section class="profile__section">
    <profileInfoBlock
      :isThereDescription="false"
      :isThereToggle="false"
      :fields="baseFields"
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

    const baseFields = ref([])

    const otherFields = ref([])

    onMounted(async () => {
      try {
        const response = await fetchMyPersonalInfo()
        console.log("Réponse complète de l'API:", response) // Affiche toute la réponse
        
        if (response) {
          // Affiche les données si elles existent
          console.log("Données de la réponse:", response.data || response)
          
          // Pour voir la structure complète de l'objet
          console.log("Structure de la réponse:", JSON.stringify(response, null, 2))

          baseFields.value = [
            { label: 'Nom de l\'entreprise', value: response.company_name },
            { label: 'Adresse', value: response.address },
            { label: 'Email', value: response.email },
            {label:'Téléphone', value: response.phone_number}
          ]

          otherFields.value = ref[
            { label: 'Catégorie', value: "" },
            { label: 'website', value: "" },
            {label:'Mise en ligne', value:""}
          ]
        }
      } catch(error) {
        console.error("Erreur de chargement:", error)
        // Affiche aussi les détails de l'erreur si disponible
        console.error("Détails de l'erreur:", error.response?.data || error.message)
      }
    })

    return{
      baseFields,
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
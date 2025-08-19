<template>
  <section class="profile__section">
    <profileInfoBlock
      :isThereDescription="false"
      :isThereToggle="false"
      :fields="baseFields"
      @field-updated="handleFieldUpdated"
    />
    <profileInfoBlock
      title="Informations supplémentaires"
      description="Ici vous retrouvez vos informations supplémentaires"
      :fields="otherFields"
      :uploadFile="false"
      :DescriptionValue="description"
      @field-updated="handleFieldUpdated"
    />
  </section>
</template>

<script>
import { ref, onMounted } from 'vue';
import profileInfoBlock from '../profileComponents/profileInfoBlock.vue';
import { fetchMyPersonalInfo } from '../_profileServices/callToApi';

export default {
  components: {
    profileInfoBlock,
  },
  setup() {
    const baseFields = ref([]);
    const otherFields = ref([]);
    const description = ref('');

    const loadData = async () => {
      try {
        const response = await fetchMyPersonalInfo();
        console.log("Réponse API:", response);
        
        if (response) {
          baseFields.value = [
            { label: 'Nom de l\'entreprise', value: response.company_name || "Non renseigné" },
            { label: 'Adresse', value: response.address || "Non renseigné" },
            { label: 'Email', value: response.email || "Non renseigné" },
            { label: 'Téléphone', value: response.phone_number || "Non renseigné" }
          ];

          otherFields.value = [
            { label: 'Catégorie', value: response.company?.category_display || "Non renseigné" },
            { label: 'Website', value: response.company?.website || "Non renseigné" },
            { 
              label: 'Mise en ligne', 
              value: response.company?.created_at 
                ? new Date(response.company.created_at).toLocaleDateString() 
                : "Non renseigné" 
            },
          ];

          description.value = response.company?.description || "Non renseigné";
        }
      } catch(error) {
        console.error("Erreur:", error);
      }
    };

    const handleFieldUpdated = (result) => {
      if (result.success) {
        console.log('Champ mis à jour avec succès');
        // Recharger les données si nécessaire
        // loadData();
      } else {
        console.error('Échec de la mise à jour:', result.error);
      }
    };

    onMounted(() => {
      loadData();
    });

    return {
      baseFields,
      otherFields,
      description,
      handleFieldUpdated,
      loadData
    };
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
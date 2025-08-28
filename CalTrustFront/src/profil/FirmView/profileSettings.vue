<template>
  <section class="profile__section">
    <profileInfoBlock
      :isThereDescription="false"
      :isThereToggle="false"
      :fields="baseFields"
      @field-updated="handleFieldUpdated"
      :InitialProfileImage="myProfilePicture"
      :isPDF="false"
    />
    <profileBlockCompany
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
import profileBlockCompany from '../profileComponents/profileBlockCompany.vue';
import { fetchMyPersonalInfo} from '../_profileServices/callToApi';

export default {
  components: {
    profileInfoBlock,
    profileBlockCompany
  },
  setup() {
    const baseFields = ref([]);
    const otherFields = ref([]);
    const description = ref('');
    const myProfilePicture = ref(null);

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
            { label: 'Website', value: response.company?.website || "Non renseigné", },
            { 
              label: 'Mise en ligne', 
              value: response.company?.created_at 
                ? new Date(response.company.created_at).toLocaleDateString() 
                : "Non renseigné" 
            },
          ];

          description.value = response.company?.description || "Non renseigné";
          myProfilePicture.value = response.company_logo || null;
        }
      } catch(error) {
        console.error("Erreur:", error);
      }
    };

    // For firm profile which is based on User model
    const handleFieldUpdated = async() => {
      try {
        await loadData(); // Recharger les données après la mise à jour
      } catch (error) {
        console.error("Erreur lors de la mise à jour:", error);
      }
    };

    const handleOhterFieldUpdate = async() => {
      try {
        await loadData(); // Recharger les données après la mise à jour
      } catch (error) {
        console.error("Erreur lors de la mise à jour:", error);
      }
    }

    onMounted(() => {
      loadData();
    });

    return {
      baseFields,
      otherFields,
      description,
      handleFieldUpdated,
      loadData,
      myProfilePicture
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
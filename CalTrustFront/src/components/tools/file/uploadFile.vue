<template>
  <div class="upload-container">
    <div class="label__family">
      <label for="avatar" class="label">Photo de profil</label>
      <span v-if="imageUrl || initialImageUrl" class="update-btn" @click="emitFileUpdate">
        Mettre à jour
      </span>
    </div>

    <!-- Afficher la zone d'upload seulement si aucune image n'est affichée -->
    <label v-if="!imageUrl && !initialImageUrl" for="avatar" class="upload-label">
      <div class="upload-content">
        <i class="ri-image-line"></i>
        <p class="file-label">Ajouter une photo ici</p>
        <p class="details">SVG, PNG, JPG or GIF (max. 5MB)</p>
      </div>
      <input
        type="file"
        id="avatar"
        accept="image/png, image/jpeg"
        @change="handleFileUpload"
      />
    </label>

    <!-- Afficher la prévisualisation de la nouvelle image si elle existe -->
    <div v-else-if="imageUrl" class="image-preview">
      <img :src="imageUrl" alt="Nouvelle image uploadée" class="preview-image">
      <button @click="resetImage" class="reset-btn">
        <i class="ri-close-line"></i>
      </button>
    </div>

    <!-- Afficher l'image initiale si aucune nouvelle image n'est sélectionnée -->
    <div v-else-if="initialImageUrl" class="image-preview">
      <img :src="initialImageUrl" alt="Photo de profil actuelle" class="preview-image">
      <button @click="resetImage" class="reset-btn">
        <i class="ri-close-line"></i>
      </button>
    </div>

    <div class="divider"></div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { updateCompanyInfo } from '@/profil/_profileServices/callToApi';

export default {
  props: {
    initialImageUrl: {
      type: String,
      default: null
    }
  },

  emits: ['update-field'],

  setup(props, { emit }) {
    const imageUrl = ref(null);
    const uploadedFile = ref(null);

    const handleFileUpload = (event) => {
      const file = event.target.files[0];
      if (file) {
        if (file.size > 5 * 1024 * 1024) {
          alert('Le fichier est trop volumineux (max 5MB)');
          return;
        }
        
        if (imageUrl.value) {
          URL.revokeObjectURL(imageUrl.value);
        }

        imageUrl.value = URL.createObjectURL(file);
        uploadedFile.value = file;
      }
    };

    const emitFileUpdate = async() => {
      try {
        if (uploadedFile.value) {
          const formData = new FormData();
          formData.append('company_logo', uploadedFile.value);
          await updateCompanyInfo(formData);
          console.log(formData);
          alert('Photo de profil mise à jour avec succès');
        } else {
          alert('Aucun fichier sélectionné');
        }
      } catch (error) {
        console.error('Erreur lors de la mise à jour de la photo de profil:', error);
        alert('Erreur lors de la mise à jour de la photo de profil');
      }
      emit('update-field', uploadedFile.value);
    };

    const resetImage = () => {
      if (imageUrl.value) {
        URL.revokeObjectURL(imageUrl.value);
        imageUrl.value = null;
        uploadedFile.value = null;
      }
    };

    return { imageUrl, handleFileUpload, resetImage, emitFileUpdate };
  }
};
</script>

<style scoped>

</style>
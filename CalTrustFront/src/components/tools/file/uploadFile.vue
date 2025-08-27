<template>
  <div class="upload-container">

    <div class="label__family">
      <label for="avatar" class="label">Photo de profil</label>
      <span class="update-btn" @click="emitFileUpdate">Mettre à jour</span>
    </div>
    <label v-if="!imageUrl" for="avatar" class="upload-label">
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

    <div v-else class="image-preview">
      <img :src="imageUrl" alt="Image uploadée" class="preview-image">
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
  emits: ['update-field'],

  // On ajoute { emit } comme deuxième argument
  setup(props, { emit }) {
    const imageUrl = ref(null);
    const uploadedFile = ref(null); // Ajout pour garder une référence au fichier

    const handleFileUpload = (event) => {
      const file = event.target.files[0];
      if (file) {
        if (file.size > 5 * 1024 * 1024) { // Correction de la taille à 5MB
          alert('Le fichier est trop volumineux (max 5MB)');
          return;
        }
        
        // On libère l'ancienne URL si elle existe
        if (imageUrl.value) {
          URL.revokeObjectURL(imageUrl.value);
        }

        imageUrl.value = URL.createObjectURL(file);
        uploadedFile.value = file; // On stocke le fichier lui-même
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
      // C'est une bonne pratique d'émettre l'objet Fichier réel, pas l'URL blob
      emit('update-field', uploadedFile.value); 
    };

    const resetImage = () => {
      if (imageUrl.value) {
        URL.revokeObjectURL(imageUrl.value);
        imageUrl.value = null;
        uploadedFile.value = null;
      }
    };

    // N'oubliez pas de retourner `emitFileUpdate` si vous l'utilisez dans le template
    return { imageUrl, handleFileUpload, resetImage, emitFileUpdate };
  }
};
</script>

<style scoped>
.upload-container {
  width: 100%;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: start;
  gap: 0.5rem;
}

.upload-label {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  padding: 2rem;
  width: 100%;
  max-width: 400px;
  border: 1px dashed gray;
  border-radius: 0.2rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.upload-label:hover {
  background: #f5f5f5;
  border-color: #525252;
}

input[type="file"] {
  display: none;
}

/* --- MODIFICATIONS CI-DESSOUS --- */

.image-preview {
  position: relative;
  width: 100%; /* Garde la largeur responsive */
  max-width: 400px; /* Limite la largeur maximale */
  /* Les propriétés 'height' et 'max-height' ont été supprimées */
}

.preview-image {
  width: 100%; /* L'image prend toute la largeur de son conteneur */
  height: auto; /* La hauteur s'ajuste pour garder les proportions */
  border-radius: 0.2rem;
  display: block;
  /* La propriété 'object-fit' a été supprimée car inutile */
}

/* --- FIN DES MODIFICATIONS --- */


.label__family{
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding-bottom: 0.8rem;
}

.reset-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.reset-btn:hover {
  background: rgba(0, 0, 0, 0.8);
}

.reset-btn i {
  font-size: 1.2rem;
}

/* Styles pour le contenu du label */
.upload-content {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.upload-content i {
  font-size: 2rem;
  color: #c5c0c0;
  margin-bottom: 0.5rem;
}

.file-label {
  font-size: 1rem;
  margin: 0;
}

.details {
  font-size: 0.8rem;
  margin: 0;
  color: #777;
}

.divider {
  height: 1px;
  background-color: #e0e0e0;
  width: 100%;
}

.label {
  color: var(--my-black-color);
  font-size: 0.9rem;
  min-width: 120px;
  text-align: left;
}

.update-btn {
  font-weight: 500;
  color: var(--primary-color);
  cursor: pointer;
  margin-left: 1rem;
  min-width: 60px;
  text-align: right;
  font-size: 0.9rem;
}

.update-btn:hover {
  text-decoration: underline;
}
</style>
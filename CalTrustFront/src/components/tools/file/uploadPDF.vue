<template>
    <div class="upload-container">
      <!-- Conteneur principal -->
      <label v-if="!imageUrl" for="avatar" class="upload-label">
        <div class="upload-content">
          <i class="ri-file-pdf-2-line"></i>
          <p class="file-label">Importer un document</p>
          <p class="details">PDF, PNG (max. 5MB)</p>
        </div>
        <input
          type="file"
          id="avatar"
          accept="image/png, application/pdf"
          @change="handleFileUpload"
        />
      </label>
  
      <!-- Prévisualisation avec bouton de suppression -->
      <div v-else class="image-preview">
        <img :src="imageUrl" alt="Image uploadée" class="preview-image">
        <button @click="resetImage" class="reset-btn">
          <i class="ri-close-line"></i>
        </button>
      </div>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  
  export default {
    setup() {
      const imageUrl = ref(null);
  
      const handleFileUpload = (event) => {
        const file = event.target.files[0];
        if (file) {
          // Vérification de la taille (5MB max)
          if (file.size > 10 * 1024 * 1024) {
            alert('Le fichier est trop volumineux (max 5MB)');
            return;
          }
          
          // Création de l'URL de prévisualisation
          imageUrl.value = URL.createObjectURL(file);
        }
      };
  
      const resetImage = () => {
        if (imageUrl.value) {
          URL.revokeObjectURL(imageUrl.value);
          imageUrl.value = null;
        }
      };
  
      return { imageUrl, handleFileUpload, resetImage };
    }
  };
  </script>
  
  <style scoped>
  .upload-container {
    width: 100%;
    max-width: 400px;
    position: relative;
  }
  
  .upload-label {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 1rem;
    padding: 2rem;
    width: 100%;
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
  
  .image-preview {
    position: relative;
    width: 100%;
    height: 100%;
  }
  
  .preview-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 0.2rem;
    display: block;
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
  </style>
<template>
  
  <div v-if="isOpen" class="modal-overlay" @click.self="close">
    
    <div class="modal-content">
      <div class="modal-header">
        <h4>{{ title }} <span> {{ firm }}</span></h4>
        <button @click="close" class="close-btn">&times;</button>
      </div>
      <div class="modal-body">
        <p 
          v-if="message.errorMessage"
          class="errorMessage"
        >
          {{ message.errorMessage }}
        </p>
        <rating
          v-model="ratingValue"
          :max-stars="5"
        />
        <inputArea 
        v-model="comment"/>
      </div>
      <div class="modal-footer">
        <secondButton2 label="annuler"/>
        <mainButton label = "envoyer" @click="submitForm"/>
      </div>
    </div>
  
  </div>
</template>

<script>
import rating from '@/components/tools/rating.vue';
import inputArea from '@/components/tools/inputArea.vue';
import mainButton from '@/components/button/mainButton.vue';
import secondButton2 from '@/components/button/secondButton2.vue';
import api from '@/_services/_authservices';
import { ref, watch } from 'vue';

export default {
  components: {rating, inputArea , mainButton, secondButton2},
  props: {
    modelValue: Boolean,
    title: {
      type: String,
      default: 'Titre de la modale'
    },
    firm:{
      type: String,
      default:"Anonyme"
    },
    firmId:{
      type:Number
    }
  },
  emits: ['update:modelValue', 'submit'],
  
  setup(props, { emit }) {
    const isOpen = ref(props.modelValue);

    watch(() => props.modelValue, (newVal) => {
      isOpen.value = newVal;
      toggleBodyScroll(newVal);
    });

    const toggleBodyScroll = (shouldDisable) => {
      document.body.style.overflow = shouldDisable ? 'hidden' : 'auto';
    };

    const close = () => {
      emit('update:modelValue', false);
    };

    const ratingValue = ref(3)

    const submit = () => {
      emit('submit');
      close();
    };
    
    //la logique commence ici
    const comment = ref('');
    const message = ref({
      errorMessage: "",
      successMessage: ""
    });
    
    const token = ref('')
    const firmId = ref(props.firmId)
    async function submitForm() {
      if (comment.value.trim() === '') {
        message.value.errorMessage = "Le commentaire ne peut être vide.";
        return;
      }
      token.value = localStorage.getItem('userToken');

      try {
        // 1. Préparer le corps (body) de la requête avec le refresh token
        const requestBody = {
            rating: ratingValue.value,
            comment: comment.value
        };

        // 2. Préparer les en-têtes (headers) avec l'access token
        const requestConfig = {
          headers: {
            'Authorization': `Bearer ${token.value}`
          }
        };

        // 3. Envoyer la requête POST avec l'URL, le corps et les en-têtes
        await api.post(`/reviews/firms/${firmId.value}/`, requestBody, requestConfig);
        
        console.log("Avis posté surl'entreprise");

      } catch (error) {
        console.error("Un problème est survenu:", error.response ? error.response.data : error.message);
        // Même en cas d'erreur (ex: token expiré), il faut déconnecter l'utilisateur côté client.
      }
    }

    return {
      isOpen,
      close,
      ratingValue,
      submit,
      comment,
      message,
      submitForm,
    };
  }
};
</script>

<style scoped>
/* Style pour l'overlay de la modale */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

/* Style pour le contenu de la modale */
.modal-content {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  background-color: white;
  border-radius: 8px;
  width: 100%;
  margin-top: 40vh;
  max-width: 500px;
  min-height: 100%;
  overflow-y: auto;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.modal-header{
  color: gray;
  font-weight: 600;
  font-size: 0.9rem;
}

.modal-header span{
  color: var(--primary-color);
  font-weight: 700;
  font-size: 1rem;
}

/* Style pour l'en-tête de la modale */
.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px;
  border-bottom: 1px solid #eee;
}

/* Style pour le corps de la modale */
.modal-body {
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

/* Style pour le pied de la modale */
.modal-footer {
  display: flex;
  justify-content: flex-end;
  padding: 16px;
  border-top: 1px solid #eee;
  gap: 8px;
}

/* Style pour le bouton de fermeture */
.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: #666;
}

/* Style pour les boutons d'action */
.cancel-btn, .submit-btn {
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
}

.cancel-btn {
  background-color: #f5f5f5;
  border: 1px solid #ddd;
}

.submit-btn {
  background-color: #42b983;
  color: white;
  border: none;
}

/* Style pour le bouton d'ouverture de la modale */
.open-modal-btn {
  padding: 10px 20px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin: 20px;
}

/* Style pour l'input dans la modale */
input {
  width: 100%;
  padding: 8px;
  margin-top: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

.errorMessage{
  color: red;
  font-size: 0.8rem;
}
</style>
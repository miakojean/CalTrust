<template>
  <Transition>
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
        <p 
          v-if="message.successMessage"
          class="succesMessage"
        >
          {{ message.successMessage }}
        </p>
        <rating
          v-model="ratingValue"
          :max-stars="5"
        />
        <inputArea 
        v-model="comment"/>
      </div>
      <div class="modal-footer">
        <secondButton2 
          label="annuler"
          @click="close"
        />
        <mainButton 
          label = "envoyer"
          :isLoading = isloading
          @click="submitForm"
        />
      </div>
    </div>
  
  </div>
  </Transition>
</template>

<script>
import rating from '@/components/tools/rating.vue';
import inputArea from '@/components/tools/inputArea.vue';
import mainButton from '@/components/button/mainButton.vue';
import secondButton2 from '@/components/button/secondButton2.vue';
import { useRouter } from 'vue-router';
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
    firmId:{ // id for getting details about firm
      type:Number
    },
    postReviewId:{
      type:Number
    }
  },
  emits: ['update:modelValue', 'submit'],
  
  setup(props, { emit }) {

    const router = useRouter();
    const isOpen = ref(props.modelValue);

    watch(() => props.modelValue, (newVal) => {
      isOpen.value = newVal;
    })

    watch(isOpen, (newVal) => {
      toggleBodyScroll(newVal);
      if (!newVal) {
        // Réinitialise les messages et valeurs quand la modal se ferme
        message.value = { errorMessage: "", successMessage: "" };
        comment.value = '';
        ratingValue.value = 1;
      }
    });

    const toggleBodyScroll = (shouldDisable) => {
      document.body.style.overflow = shouldDisable ? 'hidden' : 'auto';
    };

    const close = () => {
      toggleBodyScroll(false);
      isOpen.value = false;
      emit('update:modelValue', false);
    };

    const ratingValue = ref(1)

    const submit = () => {
      emit('submit');
      close();
    };
    
    //la logique du formulaire commence à partir de là
    const isloading = ref(false)
    
    const message = ref({
      errorMessage: "",
      successMessage: ""
    });

    const comment = ref('');
    
    const token = ref('')
    const firmId = ref(props.firmId)
    
    async function submitForm() {
      isloading.value = true;
      
      // Validation
      if (comment.value.trim() === '') {
        message.value.errorMessage = "Le commentaire ne peut être vide.";
        isloading.value = false;
        return;
      }
      
      message.value.errorMessage = "";
      
      try {
        const response = await api.post(`/reviews/firms/${props.postReviewId}/`, {
          rating: ratingValue.value,
          comment: comment.value
        });
        
        message.value.successMessage = "Avis posté avec succès ! Merci pour votre temps";
        
        setTimeout(() => close(), 3000);
      } catch (error) {
        handleSubmissionError(error);
      } finally {
        isloading.value = false;
      }
    }

    // Gestion centralisée des erreurs
    function handleSubmissionError(error) {
      if (error.response) {
        switch (error.response.status) {
          case 400:
            message.value.errorMessage = "Vous avez déjà posté un avis sur cet entreprise";
            toggleBodyScroll(false);
            break;
          case 401:
            message.value.errorMessage = "Session expirée. Veuillez vous reconnecter.";
            toggleBodyScroll(false);
            router.push('/signin');
            break;
          case 403:
            message.value.errorMessage = "Permission refusée.";
            router.push('/signin');
            break;
          case 500:
            message.value.errorMessage = "Erreur serveur. Veuillez réessayer plus tard.";
            break;
          default:
            message.value.errorMessage = error.response.data?.message || "Erreur lors de la soumission";
        }
      } else {
        message.value.errorMessage = "Problème de connexion. Vérifiez votre réseau.";
      }
      
      console.error("Erreur:", {
        message: error.message,
        response: error.response?.data,
        config: error.config
      });
    }

    return {
      isOpen, close, ratingValue, submit, comment,
      isloading, message, submitForm,
    };
  }
};
</script>

<style scoped>

.errorMessage{
  color: red;
  font-size: 0.8rem;
  width: 100%;
  text-align: start;
}

.succesMessage{
  width: 100%;
  text-align: start;
  font-size: 1rem;
  font-weight:600;
  color:var(--primary-color)
}

/* nous vous expliquerons ensuite ce que font ces classes ! */
.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
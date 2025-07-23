<template>
    <!-- Étape 1 : Email -->
    <form @submit.prevent="submitForm" v-if="step === 1">
      <div class="firms__form flex__center">
        <second-stepper title="Réinitialiser mon mot de passe"/>
        
        <Transition>
          <p class="errorMessage" v-if="message.errorMessage">{{ message.errorMessage }}</p>
        </Transition>
        <Transition>
          <p class="succesMessage" v-if="message.successMessage">{{ message.successMessage }}</p>
        </Transition>
  
        <inputFamily__2 
          label="Email"
          type="email"
          placeholder="Entrer votre email"
          v-model="formData.email"
          required
        />
        
        <stepper title="Conditions d'utilisations appliquées"/>
        
        <div class="regis__btn">
          <mainButton
            label="Suivant" 
            type="submit"
            :isLoading="isLoading"
          />
        </div>
        
        <stepper title="J'ouvre mon compte"/>
        <RouterLink to="/registration">
          J'ouvre un compte
        </RouterLink>
      </div>
    </form>
  
    <!-- Étape 2 : Token -->
    <form @submit.prevent="verifyToken" v-else-if="step === 2">
      <div class="firms__form flex__center">
        <second-stepper title="Réinitialiser mon mot de passe"/>
        
        <Transition>
          <p class="errorMessage" v-if="message.errorMessage">{{ message.errorMessage }}</p>
        </Transition>
        <Transition>
          <p class="succesMessage" v-if="message.successMessage">{{ message.successMessage }}</p>
        </Transition>
  
        <inputFamily__2 
          label="Code de vérification"
          type="text"
          placeholder="Coller le code reçu"
          v-model="formToken"
          required
        />
        
        <div class="regis__btn">
          <mainButton
            label="Vérifier le code" 
            type="submit"
            :isLoading="isLoading"
          />
        </div>
      </div>
    </form>
  
    <!-- Étape 3 : Nouveau mot de passe -->
    <form @submit.prevent="updatePassword" v-else-if="step === 3">
      <div class="firms__form flex__center">
        <second-stepper title="Réinitialiser mon mot de passe"/>
        
        <Transition>
          <p class="errorMessage" v-if="message.errorMessage">{{ message.errorMessage }}</p>
        </Transition>
        <Transition>
          <p class="succesMessage" v-if="message.successMessage">{{ message.successMessage }}</p>
        </Transition>
  
        <inputFamily__2 
          label="Nouveau mot de passe"
          type="password"
          placeholder="Entrez votre nouveau mot de passe"
          v-model="formData.newPassword"
          required
        />
        
        <inputFamily__2 
          label="Confirmer le mot de passe"
          type="password"
          placeholder="Confirmez votre mot de passe"
          v-model="formData.confirmPassword"
          required
        />
        
        <div class="regis__btn">
          <mainButton
            label="Réinitialiser" 
            type="submit"
            :isLoading="isLoading"
          />
        </div>
      </div>
    </form>
  </template>
  
<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import inputFamily__2 from '@/components/tools/inputFamily__2.vue';
import mainButton from '@/components/button/mainButton.vue';
import stepper from '@/components/cards/stepper.vue';
import secondStepper from '@/components/cards/secondStepper.vue';
import { passwordReset} from '../passwordReseting';
import api from '@/_services/_authservices';
  
  export default {
    components: { 
      inputFamily__2, 
      mainButton, 
      stepper,
      secondStepper
    },
  
    setup() {
      const router = useRouter();
      const step = ref(1);
      const isLoading = ref(false);
      const formToken = ref("");
  
      const message = ref({
        errorMessage: "",
        successMessage: ""
      });
  
      const formData = ref({
        email: "",
        newPassword: "",
        confirmPassword: ""
      });
  
      const submitForm = async () => {
        if (!formData.value.email?.trim()) {
          message.value.errorMessage = "L'email est obligatoire";
          return;
        }
  
        isLoading.value = true;
        message.value.errorMessage = "";
  
        try {
          const payload = {
            email: formData.value.email.trim().toLowerCase()
          };
          
          const success = await passwordReset(payload);
          
          if (success) {
            message.value.successMessage = "Email envoyé avec succès !";
            step.value = 2;
          } else {
            message.value.errorMessage = "Échec d'envoi. Veuillez réessayer.";
          }
        } catch (error) {
          message.value.errorMessage = error.message || "Erreur réseau. Veuillez réessayer plus tard.";
        } finally {
          isLoading.value = false;
        }
    };
      
    const verifyToken = async () => {
        isLoading.value = true;
        message.value.errorMessage = "";

        if (!formToken.value.trim()) {
            isLoading.value = false;
            message.value.errorMessage = "Veuillez saisir le code de réinitialisation";
            return false;
        }

        try {
            const payload = {
                token: formToken.value
            };

            const response = await api.post(
                '/account/password-reset/verify-token/', 
                payload,  // Envoie l'objet payload
                {
                    headers: { 
                        'Content-Type': 'application/json',
                    }
                }
            );

            if (response.status === 200) {
                step.value = 3;
                return true;
            }
                
            } catch (error) {
                let errorMsg = "Une erreur est survenue";
                
                if (error.response) {
                    // Gestion des erreurs spécifiques du serveur
                    errorMsg = error.response.data?.error || 
                            error.response.data?.detail || 
                            "Code invalide ou expiré";
                }

                message.value.errorMessage = errorMsg;
                console.error("Erreur de vérification:", error);
                return false;
            } finally {
                isLoading.value = false;
            }
        };
      
        const updatePassword = async () => {
            isLoading.value = true;
            message.value.errorMessage = "";
            if (!formData.value.newPassword || !formData.value.confirmPassword) {
                message.value.errorMessage = "Veuillez remplir tous les champs obligatoires";
                isLoading.value = false;
                return;
            }
            if (formData.value.newPassword !== formData.value.confirmPassword) {
                message.value.errorMessage = "Les mots de passe ne correspondent pas";
                isLoading.value = false;
                return;
            }
            try {
                const payload = {
                    new_password: formData.value.newPassword.trim(),
                    token: formToken.value.trim()
                };

                const response = await api.post(
                    '/account/password-reset/confirm/', 
                    payload, 
                    {
                        headers: { 
                            'Content-Type': 'application/json',
                        }
                    }
                );

                if (response.status === 200) {
                    message.value.successMessage = "Mot de passe réinitialisé avec succès !";
                    setTimeout(() => {
                        router.push('/signin');
                    }, 2000);
                } else {
                    message.value.errorMessage = "Échec de la réinitialisation du mot de passe.";
                }
            } catch (error) {
                message.value.errorMessage = error.response?.data?.detail || "Erreur lors de la mise à jour du mot de passe.";
            } finally {
                isLoading.value = false;
            }
        }
      
      return {
        router,
        message,
        step,
        isLoading,
        formData,
        formToken,
        submitForm,
        verifyToken,
        updatePassword
      };
    }   
  }
  </script>

<style scoped>
form p{
  font-size: 1.2rem;
  font-weight: 600;
  color: var(--primary-color);
}

.v-enter-active,
.v-leave-active {
transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
opacity: 0;
}

.errorMessage{
color: red;
font-size: 0.8rem;
}

.succesMessage{
  color: var(--primary-color);
  font-size: 0.8rem;
}
</style>
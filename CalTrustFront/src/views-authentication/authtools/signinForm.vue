<template>
    <form @submit.prevent="submitForm" action="">
    
        <div class="firms__form flex__center">

            <secondStepper title="Connexion"/>

            <Transition>
                <p v-if="message.errorMessages" style="color: red;">{{ message.errorMessages }}</p>
            </Transition>
            <Transition>
                <p v-if="message.emptyfields">{{ message.emptyfields }}</p>
            </Transition>
            <inputfamily__2
                label="username"
                type="text"
                placeholder="Entrer votre username"
                v-model="username"
            />
            <inputfamily__2
                label="mot de passe"
                type="password"
                placeholder="Entrer votre mot de passe"
                v-model="password"
            />
            <mainButton
                label="Connexion"
                type="submit" :isLoading="isLoading"
            />
            <stepper
                title="Pas de compte?"
            />
            <RouterLink to="/registration">
                J'ouvre mon compte
                <i class="ri-contract-right-line"></i>
            </RouterLink>
            <Transition>
                <p v-if="attempt > 0">Mot de passe oublié? <a href="#">Cliquer ici</a></p>
            </Transition>

        </div>

    </form>
</template>

<script>
import inputfamily__2 from '@/components/tools/inputFamily__2.vue';
import mainButton from '@/components/button/mainButton.vue';
import stepper from '@/components/cards/stepper.vue';
import api from '@/_services/_authservices'; // Your Axios instance
import secondStepper from '@/components/cards/secondStepper.vue';
import { ref } from 'vue';

export default {
  components: {
    inputfamily__2,
    mainButton,
    stepper,
    secondStepper
  },

  setup() {
    const username = ref('');
    const password = ref('');

    const message = ref({
      errorMessages: '',
      succesMessage: '',
      emptyfields: ""
    });

    const attempt = ref(0);
    const isLoading = ref(false);

    // This function will now handle the API call
    const submitForm = async () => {
      isLoading.value = true;
      message.value.errorMessages = ''; // Clear previous errors
      message.value.succesMessage = ''; // Clear previous success messages
      message.value.emptyfields = "";

      if (username.value === "" || password.value === ""){
        message.value.emptyfields = "Veuillez remplir tous les champs obligatoires";
        isLoading.value = false;
        return
      }

      try {
        const response = await api.post('/account/token/', {
          username: username.value, 
          password: password.value,
        });

        // Assuming Django returns a token in response.data.token or similar
        const token = response.data;
        if (token) {
          console.log("✅ Connexion établie. Token:", token);
          message.value.succesMessage = "Connexion établie avec succès !";
          localStorage.setItem('userToken', token.access); // ou adapter selon la structure de réponse;
          localStorage.setItem('userTokenRefresh', token.refresh)
        } else {
          // If no token but success response (shouldn't happen with DRF TokenObtainPairView)
          message.value.errorMessages = "Connexion réussie mais pas de jeton reçu.";
        }

      } catch (error) {
        console.error("❌ Erreur de connexion:", error);
        if (error.response) {
          // Server responded with an error status (e.g., 400, 401, 403)
          if (error.response.status === 401 || error.response.status === 400) {
            // Common errors for wrong credentials
            attempt.value++; // Increment attempt on each submission
            message.value.errorMessages = error.response.data.detail || "Email ou mot de passe incorrect.";
          } else {
            message.value.errorMessages = error.response.data.detail || "Une erreur est survenue lors de la connexion.";
          }
        } else if (error.request) {
          // No response received (network error, server down)
          message.value.errorMessages = "Pas de réponse du serveur. Vérifiez votre connexion ou réessayez plus tard.";
        } else {
          // Something else happened
          message.value.errorMessages = "Une erreur inattendue est survenue.";
        }
      } finally {
        isLoading.value = false; // Always stop loading after attempt
      }
    };

    return {
      message,
      username,
      password,
      attempt,
      isLoading,
      submitForm, // Expose submitForm to the template
    };
  },
};
</script>

<style scoped>

.form__label{
  color: gray;
  font-weight: 400;
}
p, a{
  color: red;
  font-size: 0.8rem;
}

a{
  color: var(--primary-color);
  font-size: 0.8rem;
}

.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
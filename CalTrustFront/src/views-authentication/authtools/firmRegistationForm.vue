<template>
  <form @submit.prevent="submitForm" class="regis__form">
    <second-stepper title="Inscription entreprise"/>
    
    <Transition name="fade">
      <p class="errorMessage" v-if="message.errorMessage">
        {{ message.errorMessage }}
      </p>
    </Transition>
    
    <Transition name="fade">
      <p class="succesMessage" v-if="message.successMessage">
        {{ message.successMessage }}
      </p>
    </Transition>

    <div class="form__flex__center">
      <inputFamily__2
        label="Nom de l'entreprise"
        placeholder="Votre raison sociale"
        v-model="formData.company_name"
        required
      />
      <inputFamily__2
        label="SIRET"
        placeholder="14 chiffres (ex: 12345678901234)"
        v-model="formData.siret"
        maxlength="14"
        required
      />
    </div>

    <inputFamily__2
      label="Email professionnel"
      placeholder="email@votre-entreprise.com"
      type="email"
      v-model="formData.email"
      required
    />

    <inputFamily__2
      label="Adresse"
      placeholder="Adresse complète de l'entreprise"
      v-model="formData.address"
      required
    />

    <div class="form__flex__center">
      <inputFamily__2
        label="Mot de passe"
        placeholder="8 caractères minimum"
        type="password"
        v-model="firstPassword"
        required
        minlength="8"
      />
      <inputFamily__2
        label="Confirmation"
        placeholder="Identique au mot de passe"
        type="password"
        v-model="formData.password"
        required
      />
    </div>

    <stepper
      title="Conditions d'utilisations appliquées"
    />

    <mainButton
      label="Créer mon compte professionnel"
      type="submit"
      :isLoading="isLoading"
    />
    <stepper
      title="J'ai déjà un compte"
    />
    <RouterLink to="/signin">
      Je me connecte ici
    </RouterLink>
  </form>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import inputFamily__2 from '@/components/tools/inputFamily__2.vue';
import mainButton from '@/components/button/mainButton.vue';
import api from '@/_services/_authservices';
import secondStepper from '@/components/cards/secondStepper.vue';
import stepper from '@/components/cards/stepper.vue';

export default {
  components: { inputFamily__2, mainButton, secondStepper, stepper },
  setup() {
    const router = useRouter();
    const firstPassword = ref('');
    const isLoading = ref(false);
    const message = ref({ errorMessage: '', successMessage: '' });

    const formData = ref({
      username: '', // Généré automatiquement plus tard
      email: '',
      password: '',
      user_type: 'firm',
      company_name: '',
      company_category: "Commerce", // Valeur par défaut
      siret: '',
      address: ''
    });

    const generateUsername = (email, companyName) => {
      const prefix = companyName.toLowerCase()
        .replace(/\s+/g, '_')
        .replace(/[^a-z0-9_]/g, '');
      const suffix = email.split('@')[0];
      return `${prefix}_${suffix}`.substring(0, 150);
    };

    async function submitForm() {
      isLoading.value = true;
      message.value = { errorMessage: '', successMessage: '' };

      // Validation
      if (formData.value.company_name === "") {
        message.value.errorMessage = "Entrer le nom de votre entreprise"
      }

      if (firstPassword.value !== formData.value.password) {
        message.value.errorMessage = 'Les mots de passe ne correspondent pas';
        isLoading.value = false;
        return;
      }

      if (!formData.value.siret || !/^\d{14}$/.test(formData.value.siret)) {
        message.value.errorMessage = 'Le SIRET doit comporter 14 chiffres';
        isLoading.value = false;
        return;
      }

      // Génération automatique du username
      formData.value.username = generateUsername(
        formData.value.email, 
        formData.value.company_name
      );

      try {
        const payload = { 
          ...formData.value,
          email: formData.value.email.trim().toLowerCase()
        };

        const response = await api.post('/account/', payload);

        if (response.status === 201) {
          message.value.successMessage = 'Compte créé avec succès! Redirection...';
          setTimeout(() => router.push('/signin'), 2000);
        }
      } catch (error) {
        handleApiError(error);
      } finally {
        isLoading.value = false;
      }
    }

    const handleApiError = (error) => {
      if (error.response?.status === 401) {
    // Cas spécifique d'inscription
    if (error.config.url.includes('/register')) {
      message.value = "Création de compte non autorisée";
    } else {
      message.value = "Session expirée, veuillez vous reconnecter";
    }
  }
  // Erreur réseau ou requête non atteinte
  if (!error.response) {
    message.value.errorMessage = 'Erreur réseau. Veuillez réessayer.';
    return;
  }
  const { status, data } = error.response;
  // Erreur d'authentification
  if (status === 401) {
    message.value.errorMessage = 'Session expirée. Veuillez vous reconnecter.';
    return;
  }
  // Format classique d'erreur Django/DRF/Rails
  if (data && typeof data === 'object') {
    // Cas où l'API renvoie {errors: [...]} ou {message: string}
    if (data.errors) {
      message.value.errorMessage = `Erreur: ${Array.isArray(data.errors) 
        ? data.errors.join(', ') 
        : data.errors}`;
    } else if (data.message) {
      message.value.errorMessage = `Erreur: ${data.message}`;
    } 
    // Format Django/DRF standard
    else if (Object.keys(data).length > 0) {
      message.value.errorMessage = Object.entries(data)
        .map(([field, messages]) => 
          `${field}: ${Array.isArray(messages) 
            ? messages.join(', ') 
            : messages}`
        )
        .join(' | ');
    } else {
      message.value.errorMessage = `Erreur ${status}: Une erreur est survenue`;
    }
  } 
  // Si data est une string
  else if (typeof data === 'string') {
    message.value.errorMessage = data;
  } else {
    message.value.errorMessage = `Erreur ${status}: Une erreur est survenue`;
  }
};

    return { firstPassword, message, isLoading, formData, submitForm };
  }
};
</script>

<style>
.errorMessage {
  color: red;
  font-size: 0.8rem;
}

.succesMessage {
  color: var(--primary-color);
  font-size: 0.8rem;
}

@media (min-width: 1024px) {
  .input__group {
    width: 100%;
  }
}
</style>
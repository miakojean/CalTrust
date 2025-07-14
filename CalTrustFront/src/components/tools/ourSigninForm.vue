<template>
  <form @submit.prevent="handleClick" action="">
    <inputfamily__2 
      label="email"
      type = "email"
      placeholder="Entrer votre email"
      v-model="email"
    />
    <inputfamily__2 
      label="mot de passe"
      type = "password"
      placeholder="Entrer votre mot de passe"
      v-model="password"
    />
    <mainButton 
      label="Connexion"
      @click="handleClick"
      :isLoading="isLoading"
    />
    <Transition>
      <p v-if="message.errorMessages">{{ message.errorMessages }}</p>
    </Transition>
  </form>
</template>

<script>
import inputfamily__2 from './inputFamily__2.vue';
import mainButton from '../button/mainButton.vue';
import mainButton_2 from '../button/mainButton_2.vue';
import { ref } from 'vue';
export default {

  components:{
    inputfamily__2,mainButton, mainButton_2
  },

  setup(){

    const message = ref({
      errorMessages:'',
      succesMessage:''
    })
    const email = ref('')
    const password = ref('')

    const isLoading = ref(false);
    const handleClick = () => {
      isLoading.value = true;
      // Simule un chargement (ex: appel API)
      setTimeout(() => isLoading.value = false, 2000);
    };
    
    // La fonction ne prend plus d'arguments
    const submitForm = () => { 
      // On accède aux valeurs avec .value et on utilise toLowerCase()
      if (email.value.toLowerCase() === "miako@gmail.com" && password.value === "jeanyves")
      { isLoading.value = true
        console.log("✅ Connexion établie");
      } else {
        isLoading.value = true
        message.value.errorMessages = ("Connexion impossible. Email ou mot de passe incorrect")
        console.log("❌ Connexion impossible. Email ou mot de passe incorrect.")
        isLoading.value = false;
      }
    };

    return {
      message, email, password, isLoading, handleClick, submitForm,
    }
  }

}
</script>

<style scoped>

p{
  color: #e04a4a;
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
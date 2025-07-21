<template>
  <form action="" @submit.prevent="submitForm" class="regis__form">
    <h2>Inscription</h2>
    <Transition>
      <p class="errorMessage" v-if="message.errorMessage">
        {{ message.errorMessage }}
      </p>
    </Transition>
    <Transition>
      <p class="succesMessage" v-if="message.successMessage">
        {{ message.successMessage }}
      </p>
    </Transition>
    <div class="form__flex__center">
      <inputFamily__2
        label="nom d'entreprise"
        placeholder="Entre votre nom d'entrprise"
        v-model="formData.username"
      />
      <inputFamily__2
        label="addresse"
        placeholder="entrer votre adresse"
        v-model="formData.address"
      />
    </div>
    <inputFamily__2
      label="email"
      placeholder="enter votre email"
      v-model="formData.email"
    />
    <div class="form__flex__center">
      <inputFamily__2
        label="Mot de passe"
        placeholder="Entrer un mot de passe"
        type="password"
        v-model="firstPassword"
      />
      <inputFamily__2
        label="Confirmer mot de passe"
        placeholder="Confirmer le mot de passe"
        type="password"
        v-model="formData.password"
      />
    </div>
    <mainButton
      label="Inscription"
      @click="submitForm"
      :isLoading="isLoading"
    />
  </form>
</template>

<script>
import { ref } from 'vue';
import inputFamily__2 from '@/components/tools/inputFamily__2.vue';
import mainButton from '@/components/button/mainButton.vue';
import api from '@/_services/_authservices';
export default {

    components:{
        inputFamily__2, mainButton
    },
    setup(){
        const step = ref(1)

        const firstPassword = ref("")

        const message = ref({
            errorMessage: "",
            successMessage: ""
        })

        const formData = ref({
            username :"",
            email:"",
            password:"",
            user_type:"firm",
            company_name:"",
            company_category:"Commerce",
            siret: "12345678901234",
            address: "123 Tech Park, Innovation City"
        })

        async function submitForm() {
            // Validation basique
          if (!formData.value.username || !formData.value.email || !formData.value.password) {
              message.value.errorMessage = "Veuillez remplir tous les champs obligatoires"
              return
          }
          message.value.errorMessage = ""
          
          try {
          const payload = { 
            ...formData.value,
            username: formData.value.username.trim(),
            email: formData.value.email.trim().toLowerCase()
            }

          const response = await api.post('/account/', payload, {
            headers: {
                'Content-Type' : 'application/json',
            }
          })

          if (response.status === 201) {
            message.value.successMessage = "Inscription réussie"
            formData.value = {
                username :"",
                email:"",
                password:"",
                user_type:"",
                company_name:"",
                company_category:"",
                siret: "12345678901234",
                address: ""
            }
            setTimeout(() => {
                message.value.successMessage = "";
                step.value = 1 // Renvoie à la première étape après 2s
            }, 2000);
            router.push('/signin')
            }}
             catch (error) {
                if (error.response?.status === 400) {
                  message.value.errorMessage = "Données invalides : " + 
                      (error.response.data?.username?.[0] || "Vérifiez les champs")
              } else if (error.response?.status === 500) {
                  message.value.errorMessage = "Erreur serveur. Veuillez réessayer plus tard."
              } else {
                  message.value.errorMessage = "Erreur de connexion. Vérifiez votre réseau."
              }
            } finally {
              isLoading.value = false
          }

        }

        return {step, firstPassword, message, formData, submitForm}
    }
}
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
<template>

    <form @submit.prevent="submitForm" action="">

        <div class="fims__form flex__center">

            <second-stepper/>

            <Transition>
                <p class="errorMessage" v-if="message.errorMessage">{{ message.errorMessage }}</p>
            </Transition>
            <Transition>
                <p class="succesMessage" v-if="message.successMessage">{{ message.successMessage }}</p>
            </Transition>

            <inputFamily__2 
                label="Nom d'utilisateur"
                v-model="formData.username"
            />
            <inputFamily__2 
                label="Email"
                type="email"
                v-model="formData.email"
                placeholder="Entrer votre email"
            />
            <div class="form__flex__center">
                <inputFamily__2 
                    label="Mot de pase"
                    type="password"
                    v-model="formData.password"
                    placeholder="Entrer votre mot de passe"
                />
                <inputFamily__2 
                    label="Confirmer mot de passe"
                    type="password"
                    v-model="confirmPassword"
                    placeholder="Entrer votre mot de passe"
                />
            </div>
        </div>
        <stepper
          title="Conditions d'utilisations appliquées"
        />
        <div class="regis__btn">
            <mainButton
              label="Inscription" 
              @click="submitForm"
              :isLoading = isLoading
            />
        </div>
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
import inputFamily__2 from '@/components/tools/inputFamily__2.vue';
import mainButton from '@/components/button/mainButton.vue';
import stepper from '@/components/cards/stepper.vue';
import api from '@/_services/_authservices';
import newNavbar  from '@/layout/newNavbar.vue';
import { useRouter } from 'vue-router';
import secondStepper from '@/components/cards/secondStepper.vue';

export default {
    components:{ 
        inputFamily__2, 
        mainButton, 
        stepper,
        newNavbar,
        secondStepper
    },

    setup(){
    
        const router = useRouter();
        const message = ref({
            errorMessage : "",
            successMessage: ""
        })

        const confirmPassword = ref("")

        const isLoading = ref(false)

        // Données utilisateur
        const formData = ref({
            username: "",
            email: "",
            password: "",
            user_type: "customer", // Valeur par défaut
            phone: "",
            birth_date: null
        })

        // Nouvelle méthode submitForm optimisée
        const submitForm = async () => {
            // Validation basique
            if (!formData.value.username || !formData.value.email || !formData.value.password) {
            message.value.errorMessage = "Veuillez remplir tous les champs obligatoires"
            return
            }

            if (confirmPassword.value != formData.value.password){
                message.value.errorMessage = "Les mots de passes sont différents"
                return
            }

            isLoading.value = true
            message.value.errorMessage = ""
            

            try {
                const payload = { 
                    ...formData.value,
                    username: formData.value.username.trim(),
                    email: formData.value.email.trim().toLowerCase()
                }

                const response = await api.post('/account/', payload, {
                    headers: {
                        'Content-Type': 'application/json',
                    }
                })

                // Gestion de la réponse
                if (response.status === 201) {
                    message.value.successMessage = "Inscription réussie !"
                    // Réinitialisation du formulaire
                    formData.value = {
                        username: "",
                        email: "",
                        password: "",
                        user_type: "customer",
                        phone: "",
                        birth_date: null
                    }
                    setTimeout(() => {
                        message.value.successMessage = "";
                    }, 2000);
                    router.push('/signin')
                    
                }

            } catch (error) {
                // Gestion d'erreur améliorée
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
        
        return {
            message, confirmPassword, isLoading,
            formData, submitForm
        }
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
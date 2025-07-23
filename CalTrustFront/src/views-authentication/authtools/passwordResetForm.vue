<template>

    <form @submit.prevent="submitForm" action="">

        <div class="fims__form flex__center" v-if="step === 1">

            <second-stepper title="Réinitialiser mon mot de passe"/>

            <Transition>
                <p class="errorMessage" v-if="message.errorMessage">{{ message.errorMessage }}</p>
            </Transition>
            <Transition>
                <p class="succesMessage" v-if="message.successMessage">{{ message.successMessage }}</p>
            </Transition>

            <inputFamily__2 
                label="Email"
                placeholder="Entrer votre email"
                v-model="formData.email"
            />
        </div>
        <div class="fims__form flex__center"  v-if="step === 2">

            <second-stepper title="Réinitialiser mon mot de passe"/>

            <Transition>
                <p class="errorMessage" v-if="message.errorMessage">{{ message.errorMessage }}</p>
            </Transition>
            <Transition>
                <p class="succesMessage" v-if="message.successMessage">{{ message.successMessage }}</p>
            </Transition>

            <inputFamily__2 
                label="Mon code"
                placeholder="Coller le code réçu"
                v-model="formData.username"
            />
        </div>
        <stepper
          title="Conditions d'utilisations appliquées"
        />
        <div class="regis__btn">
            <mainButton v-if="step === 1"
                label="Suivant" 
                @click="submitForm"
                :isLoading = isLoading
            />
            <mainButton v-if="step === 2"
                label="Réinitaliser" 
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

        const step = ref(1)

        const message = ref({
            errorMessage : "",
            successMessage: ""
        })

        const isLoading = ref(false)

        // Données utilisateur
        const formData = ref({
            email: ""
        })

        // Nouvelle méthode submitForm optimisée
        const submitForm = async () => {
            // Validation basique
            if (!formData.value.email) {
            message.value.errorMessage = "Veuillez remplir tous les champs obligatoires"
            return
            }
            isLoading.value = true
            message.value.errorMessage = ""
            

            try {
                const payload = { 
                    ...formData.value,
                    email: formData.value.email.trim().toLowerCase()
                }

                const response = await api.post('/account/', payload, {
                    headers: {
                        'Content-Type': 'application/json',
                    }
                })

                // Gestion de la réponse
                if (response.status === 201) {
                    message.value.successMessage = "Email envoy !"
                    // Réinitialisation du formulaire
                    formData.value = {
                        email: "",
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
            message, step, isLoading,
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
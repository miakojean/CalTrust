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
                label="suivant" 
                @click="submitForm"
                :isLoading = isLoading
            />
        </div>
        <stepper
          title="J'ouvre mon compte"
        />
        <RouterLink to="/registration">
            J'ouvre un compte
        </RouterLink>
    </form>
</template>

<script>
import { ref } from 'vue';
import inputFamily__2 from '@/components/tools/inputFamily__2.vue';
import mainButton from '@/components/button/mainButton.vue';
import stepper from '@/components/cards/stepper.vue';
import newNavbar  from '@/layout/newNavbar.vue';
import { useRouter } from 'vue-router';
import secondStepper from '@/components/cards/secondStepper.vue';
import passwordReseting from '../passwordReseting';

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

        const step = ref(2)

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
            // Validation
            if (!formData.value.email?.trim()) {
                message.value.errorMessage = "L'email est obligatoire"
                return
            }

            isLoading.value = true
            message.value.errorMessage = ""
    
            try {
                const payload = {
                    email: formData.value.email.trim().toLowerCase()
                }
                
                const success = await passwordReseting(payload)  // <-- Attendre la réponse
                
                if (success) {
                    message.value.successMessage = "Email envoyé avec succès !"
                    formData.value.email = "" // Reset du champ si besoin
                    step.value = 2
                } else {
                    message.value.errorMessage = "Échec d'envoi. Veuillez réessayer."
                }
            } catch (error) {
                message.value.errorMessage = "Erreur réseau. Veuillez réessayer plus tard."
                console.error("Erreur submitForm:", error)
            } finally {
                isLoading.value = false // <-- Important pour désactiver le loading
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
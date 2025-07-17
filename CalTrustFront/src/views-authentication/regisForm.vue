<template>
    <form @submit.prevent="submitForm" action="">
        <Transition>
            <p class="errorMessage" v-if="message.errorMessage">{{ message.errorMessage }}</p>
        </Transition>
        <checkBoxDbChoices v-if="step === 1"
            @selection-changed="onUserTypeChange"
        />

        <Transition>
            <div class="fims__form flex__center" v-if="step === 2 && userTypeSelected === 'consumer'">
                <inputFamily__2 
                    label="nom d'utilisateur"
                    v-model="user.username"
                />
                <inputFamily__2 
                    label="email"
                    type="email"
                    v-model="user.email"
                    placeholder="Entrer votre email"
                />
                <inputFamily__2 
                    label="Mot de pase"
                    type="password"
                    v-model="user.password"
                    placeholder="Entrer votre mot de passe"
                />
            </div>
        </Transition>
        <Transition>
            <div class="fims__form flex__center" v-if="step === 2 && userTypeSelected === 'company'">
                <inputFamily__2 
                    label="nom d'entrprise"
                    v-model="user.username"
                    placeholder="Entrer le nom de votre entreprise"
                />
                <inputFamily__2 
                    label="email"
                    type="email"
                    v-model="user.email"
                    placeholder="Entrer votre email"
                />
                <inputFamily__2 
                    label="Mot de pase"
                    type="password"
                    v-model="user.password"
                    placeholder="Entrer votre mot de passe"
                />
            </div>
        </Transition>
        <div class="regis__btn">
            <prevButton
                label="Précédent" 
                @click="prev"
                v-if="step > 1"
            />
            <moreButton 
                label="Suivant" 
                @click="next"
                width="100%"
            />
        </div>
        <stepper
            title="Conditions d'utilisations appliquées"
        />
    </form>
</template>

<script>
import { ref } from 'vue';
import checkBoxDbChoices from '../components/tools/checkBoxDbChoices.vue';
import moreButton from '../components/button/moreButton.vue';
import inputFamily__2 from '@/components/tools/inputFamily__2.vue';
import prevButton from '@/components/button/prevButton.vue';

export default {
    components:{ 
        checkBoxDbChoices, moreButton, 
        inputFamily__2, prevButton 
    },

    setup(){
        
        const userTypeSelected = ref('')
        
        function onUserTypeChange(optionRecue) {
        console.log(`Choix reçu de l'enfant : ${optionRecue}`);
        userTypeSelected.value = optionRecue;
        }
        
        const step = ref (1)
        const message = ref({
            errorMessage : "",
            successMessage: ""
        })
        const next = () => {
            if(userTypeSelected.value === ""){
                message.value.errorMessage = "Veuillez cocher une option"
                return
            }
            message.value.errorMessage= ""
            step.value++
        }
        
        const prev = () => {
            userTypeSelected.value = ""
            step.value--
        }

        const user = ref ({
            username: "",
            email: "",
            password: "",
            user_type: "customer"
        })

        const company = {
            user_type : "firm",
            username : "",
            email: "",
            password: "",
            company_name: "",
            company_category: "",
            siret: "12345678901234",
            adress: ""

        }

        return {
            userTypeSelected, onUserTypeChange,
            message, 
            step, next, prev, user, company
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

.regis__btn{
    display: flex;
    justify-content: center;
    width: 100%;
    gap: 1rem;
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
</style>
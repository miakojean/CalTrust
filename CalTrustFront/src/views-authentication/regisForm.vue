<template>
    <form @submit.prevent="next" action="">
        <Transition>
            <p class="errorMessage" v-if="message.errorMessage">{{ message.errorMessage }}</p>
        </Transition>
        <Transition>
            <p class="succesMessage" v-if="message.successMessage">{{ message.successMessage }}</p>
        </Transition>
        <checkBoxDbChoices
            @selection-changed="onUserTypeChange"
        />
        <stepper
            title="Conditions d'utilisations appliquées"
        />
        <mainButton @click="next"/>
    </form>
</template>

<script>
import { ref } from 'vue';
import checkBoxDbChoices from '../components/tools/checkBoxDbChoices.vue';
import moreButton from '../components/button/moreButton.vue';
import inputFamily__2 from '@/components/tools/inputFamily__2.vue';
import prevButton from '@/components/button/prevButton.vue';
import mainButton from '@/components/button/mainButton.vue';
import stepper from '@/components/cards/stepper.vue';
import { useRouter } from 'vue-router';

export default {
    components:{ 
        checkBoxDbChoices, moreButton, 
        inputFamily__2, prevButton, mainButton, stepper
    },

    setup(){
        
        const userTypeSelected = ref('')
        
        function onUserTypeChange(optionRecue) {
        console.log(`Choix reçu de l'enfant : ${optionRecue}`);
        userTypeSelected.value = optionRecue;
        }
        const message = ref({
            errorMessage : "",
            successMessage: ""
        })
        const router = useRouter();
        const next = () => {
            if(userTypeSelected.value === ""){
                message.value.errorMessage = "Veuillez choisir une option"
                return
            }
            message.value.errorMessage= ""
            router.push(`/registration/${userTypeSelected.value}`); 
        }
        
        const isLoading = ref(false)

        return {
            userTypeSelected, onUserTypeChange,
            message, next,isLoading, router
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

.succesMessage{
    color: var(--primary-color);
    font-size: 0.8rem;
}
</style>
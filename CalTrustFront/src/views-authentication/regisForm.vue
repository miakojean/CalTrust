<template>
    <form @submit.prevent="submitForm" action="">
        <checkBox v-if="step === 1"
            option1="Une entreprise"
            option2="Un consommateur"
        />

        <div class="fims__form flex__center" v-if="step === 2">
            <inputFamily__2 label="nom d'utilisateur"/>
        </div>
        <div class="regis__btn">
            <prevButton 
                label="Précédent" 
                @click="prev"
                v-if="step > 1"
            />
            <moreButton label="Suivant" @click="next"/>
        </div>
    </form>
</template>

<script>
import { ref } from 'vue';
import checkBox from '../components/tools/checkBoxDbChoices.vue';
import moreButton from '../components/button/moreButton.vue';
import inputFamily__2 from '@/components/tools/inputFamily__2.vue';
import prevButton from '@/components/button/prevButton.vue';

export default {
  components: { checkBox, moreButton, inputFamily__2, prevButton },

    setup(){
        const step = ref (1)
        const next = () => {
            step.value++
        }
        const prev = () => {
            step.value--
        }

        const company = {
            user_type : "",
            username : "",
            email: "",
            password: "",
            company_name: "",
            company_category: "",
            siret: "12345678901234",
            adress: ""

        }

        return {step, next, prev, company}
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
</style>
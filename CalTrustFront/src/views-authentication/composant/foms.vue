<template>
<main>
    <newNavbar />
    <h1>Inscription</h1>
    <form @submit.prevent="submitForm" action="">
    <Transition>
        <p class="errorMessage" v-if="message.errorMessage">{{ message.errorMessage }}</p>
    </Transition>
    <Transition>
        <p class="succesMessage" v-if="message.successMessage">{{ message.successMessage }}</p>
    </Transition>

    <Transition>
        <div class="fims__form flex__center">
            <inputFamily__2 
                label="nom d'utilisateur"
                v-model="formData.username"
            />
            <inputFamily__2
                label="nom de l'entreprise"
                v-model="formData.company_name"
                placeholder="Entrer le nom de votre entreprise"
            />
            <inputFamily__2 
                label="adresse"
                v-model="formData.address"
                placeholder="Entrer l'adresse de votre entreprise"
            />
            <inputFamily__2
                label="numéro de siret"
                type="tel"
                v-model="formData.siret"
                placeholder="Entrer votre numéro de siret"
            />
            <inputFamily__2 
                label="email professionnel"
                type="email"
                v-model="formData.email"
                placeholder="Entrer votre email"
            />
            <inputFamily__2 
                label="Mot de pase"
                type="password"
                v-model="formData.password"
                placeholder="Entrer votre mot de passe"
            />
            <selectFamily
                label="Secteur d'activité"
                :options="['Commerce', 'Restauration', 'Santé', 'Éducation', 'Autre']"
            />
        </div>
    </Transition>
    <div class="regis__btn">
        <mainButton
            label="Inscription" 
            @click="submitForm"
            :isLoading = isLoading
        />
    </div>
    <stepper
        title="Conditions d'utilisations appliquées"
    />
</form>
<footerSection/>
</main>
</template>

<script>
import { ref } from 'vue';
import checkBoxDbChoices from '@/components/tools/checkBoxDbChoices.vue';
import moreButton from '@/components/button/moreButton.vue';
import inputFamily__2 from '@/components/tools/inputFamily__2.vue';
import prevButton from '@/components/button/prevButton.vue';
import mainButton from '@/components/button/mainButton.vue';
import stepper from '@/components/cards/stepper.vue';
import api from '@/_services/_authservices';
import footerSection from '@/layout/footerSection.vue';
import newNavbar  from '@/layout/newNavbar.vue';
import { useRouter } from 'vue-router';
import selectFamily from '@/components/tools/selectFamily.vue';
export default {
components:{ 
    checkBoxDbChoices, 
    moreButton, 
    inputFamily__2, 
    prevButton, 
    mainButton, 
    stepper,
    newNavbar,
    selectFamily,
    footerSection
},

setup(){
    
    const userTypeSelected = ref('')
    
    function onUserTypeChange(optionRecue) {
    console.log(`Choix reçu de l'enfant : ${optionRecue}`);
    userTypeSelected.value = optionRecue;
    }
    const router = useRouter();
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

    const isLoading = ref(false)

    // Données utilisateur
    const formData = ref({
        username: "",
        email: "",
        password: "",
        user_type: "firm", // Valeur par défaut
        company_name: "",
        siret: "",
        address: "",
    })

    // Nouvelle méthode submitForm optimisée
    const submitForm = async () => {
        // Validation basique
        if (!formData.value.username || !formData.value.email || !formData.value.password) {
            message.value.errorMessage = "Veuillez remplir tous les champs obligatoires"
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
                    user_type: "",
                    company_name: "",
                    siret: "",
                    address: "",
                }
                setTimeout(() => {
                    message.value.successMessage = "";
                    step.value = 1 // Renvoie à la première étape après 2s
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
        userTypeSelected, onUserTypeChange,
        message, step, next, prev,isLoading,
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
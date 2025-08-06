<template>
    <article class="testimonial-card">
        <div class="profile">
            <div class="pp">
                <span>CA</span>
            </div>
            <div class="profile__info">
                <span>{{ firm }}</span>
                <p class="message__body">{{ category }}</p>
                <p></p>
            </div>
        </div>
        <div class="divider"></div>
        <rating-component/>
        <div class="btn__frame">
            <cardMainButton 
                @click="openModal"
            />
            <cardMoreButton/>
        </div>
            
        <modal-section 
            v-model="showModal" 
            :title="`Poster un avis sur`"
            :firm = firm
            :firmId = user
            @submit="handleSubmit"
        />
        
    </article>
</template>

<script>
import { ref, watch } from 'vue';
import { useRouter } from 'vue-router';
import fakeRating from '@/components/tools/fakeRating.vue';
import cardMainButton from '@/components/button/cardMainButton.vue';
import cardMoreButton from '@/components/button/cardMoreButton.vue';
import ratingComponent from '@/components/tools/ratingComponent.vue';
import modalSection from '@/section/modalSection.vue';

const defaultPic = new URL('@/assets/pictures/devnomicus.png', import.meta.url).href;

export default {
    props:{
        firm:{
            type: String,
            default:"Caladrius"
        },
        category:{
            type: String,
            default: 'fintech'
        },
        pic:{
            type: String,
            default: defaultPic
        },
        user:{
            type:Number
        }
    },

    components: {
        fakeRating, 
        cardMainButton, 
        cardMoreButton, 
        ratingComponent,
        modalSection
    },

    setup(props) {
        const showModal = ref(false);
        
        const router = useRouter()
        
        const openModal = async () => {  // <-- Ajout de async
            const accessToken = localStorage.getItem('userToken');
            const refreshToken = localStorage.getItem('userTokenRefresh');
            
            if (!accessToken || !refreshToken) {
                try {
                    await router.push('/signin'); // <-- Ajout de await
                    return; // S'assure qu'aucun code ne s'exécute après la navigation
                } catch (error) {
                    console.error("Échec de la navigation:", error);
                    return;
                }
            }
            showModal.value = true;
            console.log('Modal ouverte');
        };

        const handleSubmit = () => {
            console.log('Formulaire soumis pour', props.firm);
            // Ajoutez ici la logique de soumission
        };

        return { 
            showModal,
            openModal,
            handleSubmit
        };
    }

}
</script>

<style scoped>
.testimonial-card {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 0.5rem;
  border-radius: 1rem;
  background: white;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  width: 100%;
  max-width: 400px;
}

.divider {
  height: 2px;
  background: var(--primary-color); /* Couleur grise légère */
  margin: 1rem 0; /* Espacement vertical */
}

.profile{
    width: 100%;
    display: flex;
    justify-content: start;
    gap: 2rem;
}

.pp{
    height: 60px;
    width: 60px;
    border-radius: 50%;
    background: #d87422;
    display: flex;
    justify-content: center;
    align-items: center;
}

.pp span{
    color: white;
    font-weight: 600;
}

.profile__info{
    display: flex;
    flex-direction: column;
    justify-content: start;
    gap: 0.5rem;
}

.profile__info span{
    font-weight: 600;
    font-size: 1rem;
    color: var(--primary-color);
}

.btn__frame{
    width: 100%;
    display: flex;
    justify-content: start;
    align-items: center;
    gap: 0.5rem;
}

@media (min-width: 766px) {
    .message__body{
        font-size: 0.8rem;
        text-align: start;
    }
}

@media (min-width: 1260px) {
    .message__body{
        font-size: 0.8rem;
        text-align: start;
    }
}
</style>
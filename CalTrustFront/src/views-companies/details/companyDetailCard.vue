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
        <div class="company_info flex__center">
            <h4>Informations de l'entreprise</h4>
            <infofamily/>
            <infofamily
                icon="ri-mail-line"
                label="Email"
                :info = "email"
            />
            <infofamily
                icon="fa-solid fa-globe"
                label="Site internet"
                :info = "website"
            />
        </div>

        <div class="divider"></div>
        <div class="company_info flex__center">
            <h4>Adresse de l'entreprise</h4>
            <infofamily
                icon="fa-solid fa-location-dot"
                label="Addresse"
                :info = "addresse"
            />
            <infofamily
                icon="ri-home-4-line"
                label="Pays"
                info = "Côte d'Ivoire"
            />
        </div>
        
    </article>
</template>

<script>
import { ref, watch } from 'vue';
import { useRouter } from 'vue-router';
import infofamily from '@/components/tools/infoFamily.vue';

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
        },
        email:{
            type:String,
            default:"Caladrius@gmail.com"
        },
        website:{
            type:String,
            default:"www.caladrius.com"
        },
        addresse:{
            type:String,
            default:"04 Virtual Street, Network City"
        }
    },

    components: {
        infofamily
    },

    setup(props) {
        const showModal = ref(false);
        
        const router = useRouter()

        return { 
            showModal,
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
  /* box-shadow: 0 2px 8px rgba(0,0,0,0.1);*/
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
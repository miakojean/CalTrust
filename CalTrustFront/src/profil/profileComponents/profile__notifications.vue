<template>
  <div class="profile__container">
    <h4>{{ title }}</h4>
    <p>{{ description }}</p>

    <div class="divider"></div>
    <div class="notif__frame">
        <notification__card
            v-for="(notif, index) in notifications"
            :key="index"
            :username="notif.customer_username"
            :message="notif.message"
            :time="notif.created_at"
            :isRead="notif.is_read"
            :rating="notif.rating"
            :notificationId="notif.id"
        />
    </div>
    
  </div>
</template>

<script>
import notification__card from '@/components/cards/notification__card.vue';
import {ref, onMounted} from 'vue'
import { getMyNotifications } from '../_profileServices/callToApi';

export default {
    components:{
        notification__card,
    },

    props:{
        title:{
            type:String,
            default:'Informations de base'
        },
        description:{ 
            /* This is description of the block */
            type:String,
            default:'Cette section présente les différentes information de base de votre entreprise '
        },
        
    },

    setup() {
    
        const notifications = ref([])

        const loadNotifcations = async () => {
            try{
                const response = await getMyNotifications();
                console.log("Réponse API", response)
                notifications.value = response.results
            }   catch (error) {
                console.log(error)
            }
        };
    
        onMounted(
            () => {
                loadNotifcations();
            }
        )

        const selectedNotif = ref(null); // <-- Ajoute cette ligne
        
        //Cette fonction va aussi marquer la notification comme lu!!!
        function getNotif(notif){
            selectedNotif.value = notif;
            console.log(notif)
        }

        return {
            notifications, loadNotifcations,
            selectedNotif, getNotif
        };
    }
}
</script>

<style scoped>
.profile__container{
    display: flex;
    flex-direction: column;
    justify-content: start;
    gap: 0.5rem;
    width: 100%;
}

.profile__container h4,p{
    text-align: start;
}

h4{
    font-size: 1rem;
}

p{
    font-size: 0.9rem;
    font-weight: 400;
}

.divider {
  height: 2px;
  background: #d8d8d8; /* Couleur grise légère */
  margin: 1rem 0; /* Espacement vertical */
}

.notif__frame{
    display: flex;
    flex-direction: column;
    gap:0.5rem;
    justify-content: start;
}
</style>
<template>
  <div class="profile__container">
    <h4>{{ title }}</h4>
    <div class="description__container">
        <p>{{ description }}</p>
        <span @click="markallNotif" :class="{ 'disabled': allNotificationsRead }">
            {{ allNotificationsRead ? 'Toutes lues' : 'Marquer comme lues' }}
        </span>
    </div>

    <div class="divider"></div>
    
    <div class="notif__frame">
        <notification__card
            v-for="(notif, index) in notifications"
            :key="index"
            :username="notif.customer_username"
            :message="notif.message"
            :comment="notif.comment"
            :time="notif.created_at"
            :isRead="notif.is_read"
            :rating="notif.rating"
            :notificationId="notif.id"
            :ref="setNotificationRef"
            @marked-as-read="handleNotificationRead"
        />
    </div>
    
  </div>
</template>

<script>
import notification__card from '@/components/cards/notification__card.vue';
import {ref, onMounted, computed} from 'vue'
import { getMyNotifications, markAllNotificationsAsRead } from '../_profileServices/callToApi';

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
        const notificationRefs = ref([])

        const setNotificationRef = (el) => {
            if (el) {
                notificationRefs.value.push(el)
            }
        }

        const allNotificationsRead = computed(() => {
            return notifications.value.length > 0 && 
                   notifications.value.every(notif => notif.is_read)
        })

        const loadNotifcations = async () => {
            try{
                const response = await getMyNotifications();
                console.log("Réponse API", response)
                notifications.value = response.results
            }   catch (error) {
                console.log(error)
            }
        };

        const markallNotif = async () => {
            if (allNotificationsRead.value) return;
            
            try{
                const response = await markAllNotificationsAsRead();
                console.log("Réponse API", response)
                
                // Mettre à jour localement toutes les notifications comme lues
                notifications.value = notifications.value.map(notif => ({
                    ...notif,
                    is_read: true
                }))
                
                // Déclencher manuellement le marquage comme lu pour chaque notification
                notificationRefs.value.forEach(ref => {
                    if (ref.markAsRead) {
                        ref.markAsRead()
                    }
                })
            }   catch (error) {
                console.log(error)
            }
        };

        const handleNotificationRead = (notificationId) => {
            // Mettre à jour localement la notification comme lue
            const index = notifications.value.findIndex(n => n.id === notificationId)
            if (index !== -1) {
                notifications.value[index].is_read = true
            }
        }
    
        onMounted(
            () => {
                loadNotifcations();
            }
        )

        const selectedNotif = ref(null);
        
        function getNotif(notif){
            selectedNotif.value = notif;
            console.log(notif)
        }

        return {
            notifications, loadNotifcations,
            selectedNotif, getNotif, markallNotif,
            allNotificationsRead,
            setNotificationRef,
            handleNotificationRead
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

span{
    font-size: 0.9rem;
    font-weight: 500;
    color: var(--primary-color);
    cursor: pointer;
    transition: 0.7s ease;
}

span:hover{
    text-decoration: underline;
    transition: 0.5s ease;
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

.description__container{
    display: flex;
    width: 100%;
    justify-content: space-between;
    align-items: center;
}
</style>
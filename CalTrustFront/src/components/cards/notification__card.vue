<template>
    
    <div class="notification__container">
        <div @click="openModal" class="notification__content">
            <div class="notification__information">
                <div class="notification__header">
                    <span>{{ info }} </span>
                    <span class="time">{{ formattedTime }}</span>
                </div>

                <div class="open__notifications">
                    <span 
                        class="notification-dot"
                        :class="{ 'notification__container--read': isRead || hasBeenRead }"
                        v-if="!isRead && !hasBeenRead"
                    ></span>
                </div>
            </div>

            <div class="notif__message">
                <p>
                    {{ message }}
                </p>

                <ratingTools
                    :rating=rating
                />
            </div>
        </div>

        <notifications__modal
            v-model="isModalOpen"
            :title="'Répondre à l\'avis de'"
            :firm="'Entreprise'"
            :notifComment="comment"
            :firmId="123"
            :postReviewId="456"
            :username="username"
            @opened="markAsRead"
        />
    </div>
    
</template>

<script>

const defaultPic = new URL('@/assets/Pictures/fakepropfilepic.jpg', import.meta.url).href;
import { ref, onMounted, computed } from 'vue';
import ratingTools from '../rating/ratingTools.vue';
import notifications__modal from '@/profil/profileComponents/notifications__modal.vue';
import { markNotificationsAsRead } from '@/profil/_profileServices/callToApi';

export default {
    props:{
        pic:{
            type: String,
            default: defaultPic
        },
        info:{
            type:String,
            default:"Nouvel avis posté"
        },
        username:{
            type:String,
            default: "Le roi des pirates"
        },
        comment:{
            type:String,
            default:"On vient just tester le système de notifications"
        },
        message:{
            type:String,
            default:"Lorem ipsum dolor sit amet consectetur adipisicing elit. Eos soluta eveniet minus."
        },
        time:{
            type:String,
            default:"1h ago"
        },
        isRead:{
            type:Boolean,
            default: false
        },
        rating:{
            type:Number,
        },
        notificationId: {
            type: Number,
            required: true
        }
    },

    components:{
        ratingTools, notifications__modal
    },

    emits: ['marked-as-read'],

    setup(props, { emit }) {
        const isModalOpen = ref(false);
        const hasBeenRead = ref(false);

        const openModal = () => {
            isModalOpen.value = true;
        };

        // Formater la date pour l'affichage
        const formattedTime = computed(() => {
            try {
                const date = new Date(props.time);
                return date.toLocaleDateString('fr-FR', {
                    day: '2-digit',
                    month: '2-digit',
                    year: 'numeric',
                    hour: '2-digit',
                    minute: '2-digit'
                });
            } catch (error) {
                return props.time; // Retourner la valeur originale en cas d'erreur
            }
        });

        const markAsRead = async () => {
            if (props.isRead || hasBeenRead.value) return;
            
            try {
                await markNotificationsAsRead(props.notificationId);
                hasBeenRead.value = true;
                emit('marked-as-read', props.notificationId); // Émettre l'événement
                console.log("Notification marquée comme lue avec succès");
            } catch (error) {
                console.error("Erreur lors du marquage comme lu:", error);
            }
        };

        // Exposer la méthode pour qu'elle puisse être appelée depuis le parent
        return {
            isModalOpen, 
            openModal,
            hasBeenRead,
            formattedTime,
            markAsRead // Exposition de la méthode
        };
    }
}
</script>

<style scoped>

.notification__container {
    width: 100%;
    position: relative; /* Important pour le positionnement de la modale */
}

.notification__content {
    display: flex;
    flex-direction: column;
    justify-content: start;
    gap: 1rem;
    background: #f6f8fa;
    padding: 0.5rem;
    border-radius: 0.2rem;
    transition: transform 0.3s ease, background 0.3s ease;
    cursor: pointer;
}

.notification__content:hover {
    background: #e4e4e4;
    transform: translateY(-2px);
}

.notification__container--read {
    background: #e9ecef;
}

.notification__header{
    display: flex;
    justify-content: start;
    align-items: center;
    gap: 1rem;
    width: 100%;
}

.notification__header span{
    font-weight: 400;
    font-size: 1rem;
    color: var(--primary-color);
}

.notification__header .time{
    font-size: 400;
    color: #868686;
    font-size: 0.9rem;
}

.notification__information{
    display: flex;
    justify-content: space-between;
    width: 100%;
}

.notification-dot {
    height: 8px;
    width: 8px;
    background-color: red;
    border-radius: 50%;
    display: inline-block;
}

.notif__message{
    display: flex;
    justify-content: start;
}

.notif__message p{
    font-size: 0.9rem;
    text-align: left;
    font-weight: 400;
    width: 100%;
}
</style>
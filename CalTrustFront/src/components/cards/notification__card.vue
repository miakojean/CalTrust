<template>
    
    <div class="notification__container">
        <div @click="openModal" class="notification__content">
            <div class="notification__information">
                <div class="notification__header">
                    <span>{{ info }} </span>
                    <span class="time">{{ time }}</span>
                </div>

                <div class="open__notifications">
                    <span 
                        class="notification-dot"
                        :class="{ 'notification__container--read': isRead }"
                        v-if="isRead === false"
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
            :firmId="123"
            :postReviewId="456"
            :username="username"
        />
    </div>
    
</template>

<script>

const defaultPic = new URL('@/assets/Pictures/fakepropfilepic.jpg', import.meta.url).href;
import { ref } from 'vue';
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

        }
    },

    components:{
        ratingTools, notifications__modal
    },

    setup() {

        const isModalOpen = ref(false)

        const openModal = () => {
            isModalOpen.value = true
        }

        return {isModalOpen, openModal}
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
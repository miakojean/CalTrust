<template>
    
    <div class="notification__container">
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
                :rating=3
            />
        </div>
    </div>
    
</template>

<script>

const defaultPic = new URL('@/assets/Pictures/fakepropfilepic.jpg', import.meta.url).href;
import ratingTools from '../rating/ratingTools.vue';

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
        }
    },

    components:{
        ratingTools
    },

    setup() {

        

        return 
    }
}
</script>

<style scoped>

.notification__container {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: start;
    gap: 1rem;
    background: #f6f8fa;
    padding: 0.5rem;
    border-radius: 0.2rem;
    transition: transform 0.3s ease, background 0.3s ease; /* Ajout d'une transition pour le transform */
}

.notification__container:hover {
    background: #e4e4e4;
    cursor: pointer;
    transform: translateY(-2px); /* Ce mouvement sera maintenant animé */
}

.notification__container--read {
    background: #e9ecef; /* Une couleur de fond plus claire ou plus neutre */
    /* Vous pouvez également ajuster d'autres styles ici si nécessaire */
}

/* Modifiez l'état de survol pour ne pas écraser le style de fond */
.notification__container:hover {
    background: #e4e4e4;
    cursor: pointer;
    transform: translateY(-2px);
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
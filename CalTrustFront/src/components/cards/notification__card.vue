<template>
    
    <div class="notification__container">
        <img class="pp" :src="pic" alt="fake profile picture">
        <div class="notification__information">
            <div class="notification__header">
                <span>{{ info }} </span>
                <span class="time">{{ time }}</span>
            </div>

            <div class="open__notifications">
                <span>Ouvrir</span>
            </div>
        </div>
    </div>
    
</template>

<script>

const defaultPic = new URL('@/assets/Pictures/fakepropfilepic.jpg', import.meta.url).href;

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
        time:{
            type:String,
            default:"1h ago"
        }
    }
}
</script>

<style scoped>

.notification__container{
    width: 100%;
    display: flex;
    justify-content: start;
    align-items: center;
    gap: 1rem;
    background: #f3f8fd;
    padding: 0.2rem;
    border-radius: 1rem;
    transition: 0.7s ease-in-out;
}

.notification__container:hover{
    background: #b3dbff;
    transition: 0.5s ease-in-out;
    cursor: pointer;
}

.pp{
    height: 60px;
    width: 60px;
    border-radius: 50%;
}

.notification__header{
    display: flex;
    justify-content: start;
    align-items: center;
    gap: 1rem;
    width: 100%;
}

.notification__header span{
    font-weight: 600;
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

.notification__body{
    display: flex;
    justify-content: space-between;
}

.notification__body p{
    font-size: 0.9rem;
}
</style>
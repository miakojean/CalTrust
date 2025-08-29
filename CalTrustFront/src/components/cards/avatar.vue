<template>
    <div class="pp__wrapper">
        <img v-if="hasValidPic" class="pp" :src="pic" alt="profile picture">
        <div v-else class="cc__firm">
            <span>{{ customerInitial }}</span>
        </div>
        <div class="profile__info"> 
            <span>{{ info }}</span> 
            <p class="message__body">@{{username}}</p> 
        </div>
    </div>
</template>

<script>
import { computed } from 'vue';
export default {

    props:{
        pic:{
            type: String,
            default: null
        },
        info:{
            type: String,
            default: "Utilisateur"
        },
        username:{
            type: String,
            default: "username"
        },
        customerInitial:{
            type: String,
            default: "U"
        },
    },

    setup(props){

        const hasValidPic = computed(() => {
            return props.pic && props.pic.trim() !== '';
        });

        return { hasValidPic };
    }

}
</script>

<style scoped>
.pp__wrapper{
    display: flex;
    align-items: center;
    gap: 10px;
    margin-top: 10px;
}
</style>
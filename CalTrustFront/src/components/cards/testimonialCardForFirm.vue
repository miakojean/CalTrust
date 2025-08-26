<template>
  <article class="testimonial-card">
    
    <ratingComponent 
        :rating="rating" 
        :max="5"
        size="small"
    />

    <div class="message" @click="reviewDetail()">
        <p class="message__body">
            {{ message }}
        </p>
    </div>

    <div class="divider"></div>
    
    <div class="profile">
        <img class="pp" :src="pic" alt="fake profile picture">
        <div class="profile__info">
            <span>{{ info }}</span>
            <p class="message__body">@{{username}}</p>
        </div>
    </div>
    
    <div class="divider__two"></div>

    <div class="utility">
        <p class="is_right">Trouvez-vous cet avis utile?</p>
        <i @click="iLikeIt()" 
            class="ri-thumb-up-line"
            v-if="isUseful === false"
        ></i>

        <i class="ri-thumb-up-fill"
            @click="iLikeIt()"
            v-else 
        ></i>

    </div>

  </article>
</template>

<script>
import { computed, ref } from 'vue';
import ratingComponent from '../tools/ratingComponent.vue';
import { likeReview } from '@/_services/_fetchreviews';

const defaultPic = new URL('@/assets/Pictures/fakepropfilepic.jpg', import.meta.url).href;

export default {
    props:{

        company:{
            type:String,
            default:'anonymous'
        },
        message:{
            type: String,
            default:"Bienvenu au pays mon fils"
        },
        info:{
            type: String,
            default:"John Doe"
        },
        username:{
            type: String,
            default: 'unknown'
        },
        pic:{
            type: String,
            default: defaultPic
        },
        rating: { 
            type: Number,
            default: 4,  // Valeur par défaut
            validator: (value) => {
                return value >= 0 && value <= 5;  // Validation entre 0 et 5
            }
        },
        isUseFull:{
            type: Boolean,
            default:false
        }
    },

    emits:['review-details'],

    components:{
        ratingComponent
    },

    setup(props, {emit}) {
        const defaultPic = new URL('@/assets/Pictures/fakepropfilepic.jpg', import.meta.url).href;
        const profilePic = computed(() => props.pic || defaultPic);

        const isUseful = ref(false)

        function iLikeIt () {
            if (isUseful.value === false){
                isUseful.value = true
            } else if (isUseful.value === true){
                isUseful.value = false
            }
        }

        const reviewDetail = () => {
            emit('review-details')
        }

        return { profilePic, isUseful, iLikeIt, reviewDetail };
    }

}
</script>

<style scoped>

</style>
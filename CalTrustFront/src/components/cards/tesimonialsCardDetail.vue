<template>
  <article class="testimonial-card">
    
    <ratingComponent 
      :rating="rating" 
      :max="5"
      size="small"
    />

    <div class="message">
      <p class="message__body">
        {{ message }}
      </p>
    </div>

    <div class="divider"></div>
    
    <div class="profile">
      <img class="pp" :src="pic" alt="fake profile picture">
      <div class="profile__info">
        <span>{{username}}</span>
        <span class="date__info"> avis publié le 26/08/2025 à 15h52</span>
      </div>
    </div>

    <answerCards />
  </article>
</template>

<script>
import { computed, ref, onUnmounted } from 'vue';
import ratingComponent from '../tools/ratingComponent.vue';
import answerCards from './answerCards.vue';

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
        }
    },

    components:{
        ratingComponent, answerCards
    },

    setup(props) {
        const defaultPic = new URL('@/assets/Pictures/fakepropfilepic.jpg', import.meta.url).href;
        const profilePic = computed(() => props.pic || defaultPic);

        const isUseful = ref(false);
        const showAnswer = ref(false);

        function iLikeIt () {
            if (isUseful.value === false){
                isUseful.value = true
            } else if (isUseful.value === true){
                isUseful.value = false
            }
        }

        function toggleAnswer() {
            showAnswer.value = !showAnswer.value;
        }

        return { profilePic, isUseful, iLikeIt, showAnswer, toggleAnswer };
    }

}
</script>

<style scoped>
.testimonial-card {
  display: flex;
  flex-direction: column;
  align-items: normal;
  gap: 1rem;
  padding: 1.5rem;
  border-radius: 1rem;
  background: white;
  width: 100%;
  max-width: 600px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.divider {
  height: 2px;
  background: var(--primary-color);
  margin: 12px 0;
}

.profile{
    width: 100%;
    display: flex;
    justify-content: start;
    align-items: center;
    gap: 1rem;
}

.pp{
    height: 60px;
    width: 60px;
    border-radius: 50%;
}

.profile__info{
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    justify-content: start;
}

.profile__info span{
    font-weight: 500;
    font-size: 1rem;
    color: var(--primary-color);
}

.profile__info .date__info{
  font-size: 0.9rem;
  font-weight: 400;
  color: #6c757d;
}

@media (min-width: 766px) {
    .message__body{
        font-size: 0.9rem;
        text-align: start;
    }
}

@media (min-width: 1260px) {
    .message__body{
        font-size: 0.9rem;
        text-align: start;
    }
}
</style>
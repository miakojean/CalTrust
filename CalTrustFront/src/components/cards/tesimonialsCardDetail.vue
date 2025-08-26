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
        </div>
    </div>

    <!-- Nouvelle section de réponse avec accordéon -->
    <div class="answer-toggle" @click="toggleAnswer">
      <span>Voir la réponse de l'entreprise</span>
      <i :class="['toggle-icon', { 'expanded': showAnswer }]">▼</i>
    </div>
    
    <transition name="slide">
      <div class="answer-section" v-if="showAnswer">
        <div class="answer-header">
          <h4>Réponse de l'entreprise</h4>
          <span class="answer-date">15 mars 2023</span>
        </div>
        <div class="answer-content">
          <p>Nous vous remercions d'avoir pris le temps de partager votre expérience. Nous sommes ravis que vous ayez apprécié nos services et nous espérons vous revoir bientôt !</p>
        </div>
        <a href="#" class="view-all-link">Voir toutes les réponses</a>
      </div>
    </transition>

  </article>
</template>

<script>
import { computed, ref, onUnmounted } from 'vue';
import ratingComponent from '../tools/ratingComponent.vue';

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
        ratingComponent
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

/* Styles pour la section d'accordéon */
.answer-toggle {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem;
  margin-top: 1rem;
  background-color: #f8f9fa;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.answer-toggle:hover {
  background-color: #e9ecef;
}

.answer-toggle span {
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--primary-color);
}

.toggle-icon {
  transition: transform 0.3s ease;
  font-size: 0.8rem;
}

.toggle-icon.expanded {
  transform: rotate(180deg);
}

.answer-section {
  padding: 1rem;
  background-color: #f8f9fa;
  border-radius: 0 0 0.5rem 0.5rem;
  border-left: 3px solid var(--primary-color);
  margin-top: -0.5rem;
}

.answer-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
}

.answer-header h4 {
  margin: 0;
  font-size: 0.9rem;
  color: var(--primary-color);
  font-weight: 600;
}

.answer-date {
  font-size: 0.75rem;
  color: #6c757d;
}

.answer-content {
  margin-bottom: 0.75rem;
}

.answer-content p {
  margin: 0;
  font-size: 0.85rem;
  line-height: 1.5;
  color: #495057;
  text-align: start;
}

.view-all-link {
  font-size: 0.8rem;
  color: var(--primary-color);
  text-decoration: none;
  font-weight: 500;
}

.view-all-link:hover {
  text-decoration: underline;
}

/* Animation pour l'accordéon */
.slide-enter-active, .slide-leave-active {
  transition: all 0.3s ease;
  max-height: 300px;
  overflow: hidden;
}

.slide-enter-from, .slide-leave-to {
  max-height: 0;
  opacity: 0;
  transform: translateY(-10px);
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
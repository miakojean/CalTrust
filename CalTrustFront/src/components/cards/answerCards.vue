<template>
  <div class="answer-card">

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

  </div>
</template>

<script>
import { computed, ref, onUnmounted } from 'vue';
import ratingComponent from '../tools/ratingComponent.vue';

export default {
    props:{
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
    },

    components:{
        ratingComponent
    },

    setup() {
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

        return { isUseful, iLikeIt, showAnswer, toggleAnswer };
    }

}
</script>

<style scoped>
.answer-card {
  display: flex;
  flex-direction: column;
  align-items: normal;
  gap: 1rem;
  border-radius: 1rem;
  background: white;
  width: 100%;
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
  width:100%;
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